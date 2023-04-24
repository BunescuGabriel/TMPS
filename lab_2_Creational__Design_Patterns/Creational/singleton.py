# Singleton este un model de design creațional, care asigură că există un 
# singur obiect de acest fel și oferă un singur punct de acces 
# la acesta pentru orice alt cod . Singleton are aproape aceleași avantaje și dezavantaje ca și 
# variabilele globale. Deși sunt super la îndemână, ele sparg modularitatea codului tău.

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
        cursor.execute("CREATE TABLE IF NOT EXISTS autor (id INTEGER PRIMARY KEY, nume TEXT, prenume TEXT, nationalitate TEXT, an_nastere INTEGER);")
        connection.commit()


# Creare instanță a conexiunii la baza de date
db_connection = DatabaseConnectionFactory.get_instance('mydatabases.db').connection


# Acesta se referă la o clasă care permite crearea unui singur obiect din ea,
# cu scopul de a limita numărul de instanțe ale unei clase și a asigura că există
# întotdeauna o singură instanță activă a acestei clase.

# În acest caz, clasa DatabaseConnectionFactory este clasa Singleton,
# iar metoda get_instance este cea care asigură că este creată o singură
# instanță a clasei DatabaseConnection.

# De fiecare dată când se apelează metoda get_instance, se verifică dacă
# instanța există deja. Dacă aceasta nu există, se creează o nouă instanță și se
# stochează în variabila __instance a clasei DatabaseConnectionFactory. În caz contrar,
# se returnează instanța existentă.

# Astfel, se asigură că există întotdeauna o singură conexiune la baza de date, evitând
# astfel crearea mai multor conexiuni inutile și neutilizate.
