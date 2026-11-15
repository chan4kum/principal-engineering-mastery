#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
case "${1:-}" in L1|L2|L3|L4|guided|platform) ;; *) echo "Usage: bash run.sh L1|L2|L3|L4|guided|platform" >&2; exit 2;; esac
scenario=$1
scratch=$(mktemp -d)
cluster="pem-a09-$$"
builder=
cluster_requested=false
export KUBECONFIG="$scratch/kubeconfig"
cleanup() {
    local status=$?
    if [[ $cluster_requested == true ]]; then
        if (( status )); then kubectl get pod,service,endpointslice -A >&2 || true; fi
        kind delete cluster --name "$cluster" >/dev/null || true
    fi
    if [[ -n $builder ]]; then docker buildx rm "$builder" >/dev/null || true; fi
    rm -rf "$scratch"
}
trap cleanup EXIT

if [[ $scenario == L1 ]]; then
    builder="pem-a09-builder-$$"
    docker buildx create --name "$builder" --driver docker-container >/dev/null
    docker buildx build --builder "$builder" --platform linux/amd64,linux/arm64 \
        --provenance=false --output "type=oci,dest=$scratch/image.tar" .
    python3 inspect_oci.py "$scratch/image.tar"
    docker build -t pem-a09:local .
    docker run --rm --network none --read-only pem-a09:local python -c 'import os; assert os.getuid() == 10001'
    if docker run --rm --network none pem-a09:local python /app/missing.py; then
        echo "expected broken startup command to fail" >&2
        exit 1
    fi
    docker run --rm --network none --read-only pem-a09:local python -c 'import sys; sys.path.insert(0, "/app"); import server; print("startup module recovered")'
    exit
fi

docker build -t pem-a09:local .
cluster_requested=true
if [[ "$scenario" == L3 || "$scenario" == platform ]]; then
    kind create cluster --name "$cluster" --kubeconfig "$KUBECONFIG" --config policy-cluster.yaml
    kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.33.0/manifests/calico.yaml
    kubectl rollout status -n kube-system daemonset/calico-node --timeout=240s
    kubectl wait node --all --for=condition=Ready --timeout=180s
else
    kind create cluster --name "$cluster" --kubeconfig "$KUBECONFIG" --wait 120s
fi
kind load docker-image pem-a09:local --name "$cluster"
kubectl label namespace default pod-security.kubernetes.io/enforce=restricted --overwrite
kubectl apply -f ../projects/guided/platform.yaml
kubectl rollout status deployment/api --timeout=120s

probe() {
    kubectl exec client -- python -c 'import json,sys,urllib.request; data=json.load(urllib.request.urlopen(sys.argv[1], timeout=3)); assert data["release"] == sys.argv[2]; print(data)' "$1" "$2"
}

case "$scenario" in
    L2|guided)
        old=$(kubectl get pod -l component=api -o jsonpath='{.items[0].metadata.name}')
        kubectl delete pod "$old" --timeout=60s
        kubectl rollout status deployment/api --timeout=120s
        kubectl wait --for=jsonpath='{.status.readyReplicas}'=2 deployment/api --timeout=120s
        test "$(kubectl get pod "$old" --ignore-not-found -o name)" = ""
        kubectl get events --sort-by=.metadata.creationTimestamp
        kubectl patch deployment api --type strategic -p '{"spec":{"template":{"spec":{"containers":[{"name":"api","readinessProbe":{"httpGet":{"path":"/missing","port":8080},"periodSeconds":2}}]}}}}'
        if kubectl rollout status deploy/api --timeout=20s; then
            echo "expected bad readiness path to stop rollout" >&2
            exit 1
        fi
        kubectl apply -f ../projects/guided/platform.yaml
        kubectl rollout status deploy/api --timeout=120s
        ;;
    L3|L4|platform)
        kubectl apply -f ../projects/independent/client.yaml
        kubectl wait --for=condition=Ready pod/client --timeout=120s
        probe http://api:8080 baseline
        ;;
esac

case "$scenario" in
    L3|platform)
        kubectl get endpointslice -l kubernetes.io/service-name=api
        kubectl apply -f ../projects/independent/deny-ingress.yaml
        failed=false
        for _ in $(seq 1 10); do
            if ! probe http://api:8080 baseline; then failed=true; break; fi
            sleep 1
        done
        test "$failed" = true
        kubectl apply -f ../projects/independent/allow-client.yaml
        recovered=false
        for _ in $(seq 1 10); do
            if probe http://api:8080 baseline; then recovered=true; break; fi
            sleep 1
        done
        test "$recovered" = true
        if [[ "$scenario" == L3 ]]; then echo "L3 verified"; exit 0; fi
        ;;
    L4)
        kubectl set env deploy/api RELEASE=drift
        kubectl rollout status deploy/api --timeout=120s
        probe http://api:8080 drift
        kubectl diff -f ../projects/guided/platform.yaml || test "$?" = 1
        kubectl apply -f ../projects/guided/platform.yaml
        kubectl rollout status deploy/api --timeout=120s
        probe http://api:8080 baseline
        ;;
esac

if [[ "$scenario" == platform ]]; then
        kubectl apply -f ../projects/independent/disruption.yaml
        test "$(kubectl get pod client -o jsonpath='{.spec.automountServiceAccountToken}')" = false
        kubectl exec client -- python -c 'import os; assert os.getuid() == 10001'
        test "$(kubectl get pdb api -o jsonpath='{.spec.minAvailable}')" = 1
        if kubectl run rejected --image=pem-a09:local --restart=Never --dry-run=server >/dev/null 2>"$scratch/rejection"; then
            echo 'expected restricted admission to reject an unsafe pod' >&2
            exit 1
        fi
        grep -i 'PodSecurity' "$scratch/rejection"
fi
printf '%s verified\n' "$scenario"
