import pytest
import psycopg2
import logging
from calc_app import CalcApp
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "db"),
    database=os.getenv("DB_NAME", "testdb"),
    user=os.getenv("DB_USER", "user"),
    password=os.getenv("DB_PASSWORD", "password")
)

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        filename="test_log.log",
        filemode="w",
        force=True
    )

@pytest.fixture(scope="module")
def calc_app_instance():
    logging.info("item creation")
    app = CalcApp(
        dbname="testdb",
        user="user",
        password="password",
        host="db"
    )
    yield app
    app.close()
    logging.info("db dissconnect")