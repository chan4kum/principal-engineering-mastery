CREATE TABLE order_entries (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tenant text NOT NULL CHECK (length(tenant) BETWEEN 1 AND 80),
    request_key text NOT NULL CHECK (length(request_key) BETWEEN 1 AND 100),
    cents bigint NOT NULL CHECK (cents > 0),
    created_at timestamptz NOT NULL DEFAULT now(),
    UNIQUE (tenant, request_key)
);

CREATE FUNCTION submit_order(p_tenant text, p_key text, p_cents bigint)
RETURNS bigint
LANGUAGE plpgsql
AS $$
DECLARE
    result_id bigint;
    original_cents bigint;
BEGIN
    INSERT INTO order_entries (tenant, request_key, cents)
    VALUES (p_tenant, p_key, p_cents)
    ON CONFLICT (tenant, request_key) DO NOTHING
    RETURNING id INTO result_id;

    IF result_id IS NOT NULL THEN
        RETURN result_id;
    END IF;

    SELECT id, cents INTO STRICT result_id, original_cents
    FROM order_entries
    WHERE tenant=p_tenant AND request_key=p_key;

    IF original_cents IS DISTINCT FROM p_cents THEN
        RAISE EXCEPTION 'idempotency conflict' USING ERRCODE = '22023';
    END IF;
    RETURN result_id;
END;
$$;
