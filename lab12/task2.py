# task2_database.py
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def close(self):
        pass


class SQLiteDatabase(DatabaseInterface):
    def connect(self):
        return "Подключено к SQLite базе данных."

    def execute_query(self, query):
        return f"SQLite выполнила запрос: {query}"

    def close(self):
        return "Соединение SQLite закрыто."


class PostgreSQLDatabase(DatabaseInterface):
    def connect(self):
        return "Подключено к PostgreSQL базе данных."

    def execute_query(self, query):
        return f"PostgreSQL выполнила запрос: {query}"

    def close(self):
        return "Соединение PostgreSQL закрыто."


if __name__ == "__main__":
    sqlite_db = SQLiteDatabase()
    postgres_db = PostgreSQLDatabase()

    print("SQLite:")
    print(" -", sqlite_db.connect())
    print(" -", sqlite_db.execute_query("SELECT * FROM users"))
    print(" -", sqlite_db.close())

    print("\nPostgreSQL:")
    print(" -", postgres_db.connect())
    print(" -", postgres_db.execute_query("SELECT * FROM orders"))
    print(" -", postgres_db.close())
