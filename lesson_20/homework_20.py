"""
    Створіть базу даних для інтернет-магазину з наступними таблицями:

    products: таблиця для зберігання інформації про продукти, включаючи назву, опис, ціну тощо.
    products: повинна мати зовнішній ключ на таблицю categories.
    categories: таблиця для категорій продуктів.
    
    Напишіть функції:
    1. для створення зазначених таблиць.
    2. Для Внесення декілька рядків даних в кожну таблицю
    3. JOIN-запит для повернення інформації про продукти та назву їх категорій

    Здати ЯК ПР. 
    Файл бази в ПР не включати.
"""

import psycopg2

class PostgresDB:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def create(self, query, values):
        try:
            connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            print("Query successfully executed")
        except Exception as error:
            print("Error while executing query", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def insert_multiply(self, query, values):
        try:
            connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            cursor = connection.cursor()
            cursor.executemany(query, values)
            connection.commit()
            print("Query successfully executed")
        except Exception as error:
            print("Error while executing query", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def read(self, query, values):
        try:
            connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            cursor = connection.cursor()
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except Exception as error:
            print("Error while reading data", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


if __name__ == "__main__":

    db = PostgresDB(dbname='mydatabase', user='automation', password='automation')


    db.create('''CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY,
        title VARCHAR(70) UNIQUE NOT NULL,
        description VARCHAR(290)
    );''', None)

    db.create('''CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        article INTEGER UNIQUE NOT NULL,
        title VARCHAR(70) NOT NULL,
        category VARCHAR(70) REFERENCES categories(title),
        description VARCHAR(290),
        units VARCHAR(290) NOT NULL,
        price DECIMAL(5, 2)
    );''', None)

    categories_items = [("Bacary", "all bacary products"), ("Milk products", "all milk products"),
                  ("Meat", "all meat products"), ("Fruits&Vegetables", "all fresh products")]
    products_items = [(213221, "Bread", 'Bacary', 'fresh product', 'piece', 25.10),
                (215245, "Apple", 'Fruits&Vegetables', 'fresh product', 'kg', 42),
                (856974, "Pork", 'Meat', 'fresh product', 'kg', 125),
                (100245, "Cow milk", 'Milk products', 'fresh product', '1l', 26.8),
                (857485, "Cream cheese", 'Milk products', 'fresh product', '150g', 51)]

    db.insert_multiply("INSERT INTO categories (title, description) VALUES (%s, %s)", categories_items)
    db.insert_multiply("INSERT INTO products (article, title, category, description, units, price) "
              "VALUES (%s, %s, %s, %s, %s, %s)", products_items)

    users = db.read('''SELECT * FROM categories''', None)
    users2 = db.read('''SELECT * FROM products''', None)
    print(users)
    print(users2)

    users3 = db.read(
        '''SELECT products.* FROM products 
           LEFT JOIN categories ON products.category = categories.title 
           WHERE categories.title = %s''',
        ('Milk products',)
    )
    print(users3)