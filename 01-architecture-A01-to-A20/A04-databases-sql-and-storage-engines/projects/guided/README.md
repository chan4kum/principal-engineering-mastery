# Guided project · PostgreSQL indexes, WAL and transaction sandbox

```text
SQL fixture → heap and index plans → transaction commit or rollback → crash and restart
```

```sh
LAB=01-architecture-A01-to-A20/A04-databases-sql-and-storage-engines/labs
bash "$LAB/run.sh" guided
```

Compare scan and index plans using the [fixture data](../../labs/plans.sql), then predict the balances in the [transfer](sandbox.sql). Verify the total is 60 after the deliberate rollback. Finally, restart after a controlled crash and verify the committed versus incomplete markers. Save the buffer evidence, balance invariant, and failure and recovery results. Explain when an index slows writes and why retaining the volume matters.

The runner removes the private PostgreSQL container and its anonymous volume when it exits.
