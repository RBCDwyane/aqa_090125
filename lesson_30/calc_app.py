import psycopg2

class CalcApp:
    def __init__(self, dbname, user, password, host, port="5432"):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self._create_table()

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b if b != 0 else None

    def _create_table(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS results (
                    id SERIAL PRIMARY KEY,
                    a INT,
                    b INT,
                    operation VARCHAR(10),
                    result FLOAT
                ); """)
            self.conn.commit()

    def save_result(self, a, b, operation, result):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO results (a, b, operation, result) VALUES (%s, %s, %s, %s)",
                (a, b, operation, result)
            )
            self.conn.commit()

    def close(self):
        self.conn.close()