ALTER TABLE order_entries ADD COLUMN IF NOT EXISTS origin text;
UPDATE order_entries SET origin='legacy' WHERE origin IS NULL;
ALTER TABLE order_entries ALTER COLUMN origin SET DEFAULT 'legacy';
