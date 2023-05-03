import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.create_db()

    def create_db(self):
        # Verificați dacă baza de date există și, în caz contrar, creați-o
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        if not tables:
            # Creați tabela "users" dacă nu există
            cursor.execute("CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY, nume TEXT, prenume TEXT, "
                           "nationalitate TEXT, an_nastere INTEGER);")
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()


class DatabaseConnectionFactory:
    __instance = None

    @staticmethod
    def get_instance(db_name):
        if not DatabaseConnectionFactory.__instance:
            connection = DatabaseConnection(db_name)
            connection.connect()
            DatabaseConnectionFactory.create_autor_table(connection.connection)
            DatabaseConnectionFactory.__instance = connection
        return DatabaseConnectionFactory.__instance

    @staticmethod
    def create_autor_table(connection):
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY, nume TEXT, prenume TEXT, nationalitate TEXT, an_nastere INTEGER);")
        connection.commit()


# Creare instanță a conexiunii la baza de date
db_connection = DatabaseConnectionFactory.get_instance('mydatabases.db').connection
