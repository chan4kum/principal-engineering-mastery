# Independent project · Transactional order ledger with migrations and recovery

Build a PostgreSQL order intake ledger and keep the old caller working as its schema expands.

```text
tenant + request key + integer cents → unique order entry
                                    → same ID on retry or conflict on changed cents
```

Create an `order_entries` table with `id`, `tenant`, `request_key`, `cents`, and `created_at`. Expose `submit_order(tenant text, key text, cents bigint)` returning the ID. Enforce positive cents and unique tenant/key. Equal retries return the original ID, including across restart. Changed amounts for the same key fail with SQLSTATE `22023`. Same keys across tenants are independent.

Add an `origin` field in a second migration. Migrate existing rows and support the old caller with a default. Reapplying the migration should succeed. Use the [acceptance SQL](check.sql) and test two concurrent connections. Save the replay result, SQLSTATE, aggregate total, old and new read results, and proof that the replay persists across an abrupt restart.

<details>
<summary>Reference implementation for review after the independent gate</summary>

- [Initial ledger and function](001_ledger.sql)
- [Compatible migration](002_origin.sql)

```sh
LAB=01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/labs
bash "$LAB/run.sh" ledger
```

The runner is designed for PostgreSQL Read Committed. The calling application is responsible for authenticating the tenant. Production workloads also need deliberate grants, retry rules and a bounded online backfill.

</details>
