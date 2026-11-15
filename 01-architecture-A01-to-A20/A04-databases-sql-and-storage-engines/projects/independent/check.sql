DO $$
DECLARE
    original bigint;
    replay bigint;
    other bigint;
BEGIN
    original := submit_order('alpha', 'a', 1200);
    replay := submit_order('alpha', 'a', 1200);
    other := submit_order('beta', 'a', 1200);
    IF original <> replay OR original = other THEN
        RAISE EXCEPTION 'replay or tenant scope failed';
    END IF;
    BEGIN
        PERFORM submit_order('alpha', 'a', 1300);
        RAISE EXCEPTION 'conflict was accepted';
    EXCEPTION WHEN invalid_parameter_value THEN NULL;
    END;
    BEGIN
        PERFORM submit_order('alpha', 'invalid', -1);
        RAISE EXCEPTION 'invalid amount was accepted';
    EXCEPTION WHEN check_violation THEN NULL;
    END;
    IF (SELECT sum(cents) FROM order_entries) <> 3000 THEN
        RAISE EXCEPTION 'failed commands changed committed total';
    END IF;
    IF (SELECT count(*) FROM order_entries WHERE origin='legacy') <> 3 THEN
        RAISE EXCEPTION 'old writer contract failed after migration';
    END IF;
END;
$$;
