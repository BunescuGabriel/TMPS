
#  pattern-ului Builder pentru clasa Autor în Python
#constructor

class AutorBuilder:
    def __init__(self):
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

    def build(self):
        return Autor(self.nume, self.prenume, self.nationalitate, self.an_nastere)


class Autor:
    def __init__(self, nume, prenume, nationalitate=None, an_nastere=None):
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