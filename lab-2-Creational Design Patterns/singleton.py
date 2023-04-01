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
            DatabaseConnectionFactory.__instance = connection
        return DatabaseConnectionFactory.__instance





# Clasa DatabaseConnection are o variabilă statică privată __instance care reține o singură 
# instanță a conexiunii la baza de date. Atunci când se apelează constructorul,
# se verifică dacă o instanță există deja și se returnează acea instanță în loc să se creeze una nouă. 
# Astfel, se asigură că este creată doar o singură conexiune la baza de date.

db_connection = DatabaseConnection('mydatabase.db').connection
cursor = db_connection.cursor()

