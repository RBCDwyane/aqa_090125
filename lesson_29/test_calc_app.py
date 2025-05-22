import logging

def test_operations(calc_app_instance):
    app = calc_app_instance

    logging.info("add(1, 2) == 3")
    assert app.add(1, 2) == 3
    logging.info("subtract(5, 3) == 2")
    assert app.subtract(5, 3) == 2
    logging.info("multiply(4, 3) == 12")
    assert app.multiply(4, 3) == 12
    logging.info("divide(10, 2) == 5")
    assert app.divide(10, 2) == 5
    logging.info("divide(5, 0) == None")
    assert app.divide(5, 0) is None

def test_db_connection(calc_app_instance):
    logging.info("succes db connection")
    assert calc_app_instance.conn is not None

def test_insert(calc_app_instance):
    app = calc_app_instance
    app.save_result(2, 2, 'add', 4.0)
    logging.info("recording added (2, 2, 'add', 4.0)")

    with app.conn.cursor() as cur:
        cur.execute("SELECT * FROM results ORDER BY id DESC LIMIT 1")
        result = cur.fetchone()
    logging.info(f"check new item: {result}")
    assert result[1:] == (2, 2, 'add', 4.0)

def test_update(calc_app_instance):
    app = calc_app_instance
    with app.conn.cursor() as cur:
        cur.execute("UPDATE results SET result = 7.0 WHERE id = (SELECT MAX(id) FROM results)")
        logging.info("last rec changed -> result = 7.0")
        cur.execute("SELECT result FROM results WHERE id = (SELECT MAX(id) FROM results)")
        result = cur.fetchone()[0]
    assert result == 7.0

def test_delete(calc_app_instance):
    app = calc_app_instance
    with app.conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM results")
        before = cur.fetchone()[0]

        cur.execute("DELETE FROM results WHERE id = (SELECT MAX(id) FROM results)")
        app.conn.commit()

        cur.execute("SELECT COUNT(*) FROM results")
        after = cur.fetchone()[0]

        assert after == before - 1