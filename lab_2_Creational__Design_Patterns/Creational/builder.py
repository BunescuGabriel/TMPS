from Creational.singleton import DatabaseConnectionFactory


#  pattern-ului Builder pentru clasa Autor în Python
# constructor

class AutorBuilder:
    def __init__(self):
        self.db_connection = DatabaseConnectionFactory.get_instance('mydatabases.db').connection
        self.nume = ""
        self.prenume = ""
        self.nationalitate = None
        self.an_nastere = None

    def set_nume(self, nume):
        self.nume = nume
        return self

    def set_prenume(self, prenume):
        self.prenume = prenume
        return self

    def set_nationalitate(self, nationalitate):
        self.nationalitate = nationalitate
        return self

    def set_an_nastere(self, an_nastere):
        self.an_nastere = an_nastere
        return self

    # def build(self):
    #     autor = Autor(self.nume, self.prenume, self.nationalitate, self.an_nastere)
    #     return autor
    def build(self):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO autor (nume, prenume, nationalitate, an_nastere) VALUES (?, ?, ?, ?);",
                       (self.nume, self.prenume, self.nationalitate, self.an_nastere))
        self.db_connection.commit()
        autor_id = cursor.lastrowid
        return Autor(autor_id, self.nume, self.prenume, self.nationalitate, self.an_nastere)


class Autor:

    def __init__(self, autor_id, nume, prenume, nationalitate, an_nastere):
        self.autor_id = autor_id
        self.nume = nume
        self.prenume = prenume
        self.nationalitate = nationalitate
        self.an_nastere = an_nastere

    def __str__(self):
        return f"{self.nume} {self.prenume} ({self.nationalitate}, {self.an_nastere})"

    def get_full_name(self):
        return f"{self.nume} {self.prenume}"

    def modifica_autor(self, autor_nou):
        self.autor = autor_nou

# Clasa AutorBuilder este un builder care ajută la crearea unui obiect de tip Autor prin setarea
# valorilor sale de-a lungul a mai multor apeluri de metode, în loc să le setezi într-un singur 
# apel de constructor. Clasa Autor este clasa principală pe care o vom construi cu ajutorul 
# AutorBuilder și conține atributele care vor fi setate în timpul procesului de construcție.
