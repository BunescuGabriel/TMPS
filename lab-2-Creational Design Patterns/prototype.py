import copy
from builder import AutorBuilder

# vom crea clasa ResursaPrototype care va fi prototipul 
# pentru obiectele de tip Resursa. Vom utiliza metoda clone pentru a crea o 
# copie identica a prototipului.


class ResursaPrototype:
    def clone(self):
        return copy.deepcopy(self)

class CartePrototype(ResursaPrototype):
    def __init__(self):
        self.titlu = input("Introduceti titlul cartii: ")
        self.autor = AutorBuilder().set_nume(input("Introduceti numele autorului: ")).set_prenume(
            input("Introduceti prenumele autorului: ")).build()
        self.editura = input("Introduceti numele editurii: ")

    def afisare(self):
        print(f"Titlu: {self.titlu}")
        print(f"Autor: {self.autor}")
        print(f"Editura: {self.editura}")

class FilmPrototype(ResursaPrototype):
    def __init__(self):
        self.titlu = input("Introduceti titlul filmului: ")
        self.regizor = AutorBuilder().set_nume(input("Introduceti numele regizorului: ")).set_prenume(
            input("Introduceti prenumele regizorului: ")).build()
        self.an_aparitie = int(input("Introduceti anul aparitiei: "))

    def afisare(self):
        print(f"Titlu: {self.titlu}")
        print(f"Regizor: {self.regizor}")
        print(f"An aparitie: {self.an_aparitie}")

class MuzicaPrototype(ResursaPrototype):
    def __init__(self):
        self.titlu = input("Introduceti titlul albumului muzical: ")
        self.artist = AutorBuilder().set_nume(input("Introduceti numele artistului: ")).set_prenume(
            input("Introduceti prenumele artistului: ")).build()
        self.an_aparitie = int(input("Introduceti anul aparitiei: "))

    def afisare(self):
        print(f"Titlu: {self.titlu}")
        print(f"Artist: {self.artist}")
        print(f"An aparitie: {self.an_aparitie}")

carte_prototype = CartePrototype()
carte_prototype.afisare()

film_prototype = FilmPrototype()
film_prototype.afisare()

muzica_prototype = MuzicaPrototype()
muzica_prototype.afisare()
