CREATE TABLE plan_items(id int NOT NULL, rare boolean NOT NULL, payload text NOT NULL);
INSERT INTO plan_items
SELECT n, n=12345, repeat('x',100) FROM generate_series(1,30000) AS n;
ANALYZE plan_items;
EXPLAIN (ANALYZE, BUFFERS) SELECT payload FROM plan_items WHERE id=12345;
CREATE INDEX plan_item_id ON plan_items(id);
CREATE INDEX plan_item_rare ON plan_items(rare);
ANALYZE plan_items;
EXPLAIN (ANALYZE, BUFFERS) SELECT payload FROM plan_items WHERE id=12345;
EXPLAIN (ANALYZE, BUFFERS) SELECT payload FROM plan_items WHERE NOT rare;
