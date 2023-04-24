from abc import ABC, abstractmethod
from Creational.builder import AutorBuilder


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    def __init__(self, resursa):
        self.resursa = resursa

    def operation(self):
        self.resursa.afisare()


class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def get_child(self, index):
        return self._children[index]

    def operation(self):
        for child in self._children:
            child.operation()


class Carte(Leaf):
    def __init__(self):
        self.titlu = input("Introduceti titlul cartii: ")
        self.autor = AutorBuilder().set_nume(input("Introduceti numele autorului: ")).set_prenume(
            input("Introduceti prenumele autorului: ")).build()
        self.editura = input("Introduceti numele editurii: ")
        super().__init__(self)

    def afisare(self):
        print(f"Titlu: {self.titlu}")
        print(f"Autor: {self.autor}")
        print(f"Editura: {self.editura}")


class Film(Leaf):
    def __init__(self):
        self.titlu = input("Introduceti titlul filmului: ")
        self.regizor = AutorBuilder().set_nume(input("Introduceti numele regizorului: ")).set_prenume(
            input("Introduceti prenumele regizorului: ")).build()
        self.an_aparitie = int(input("Introduceti anul aparitiei: "))
        super().__init__(self)

    def afisare(self):
        print(f"Titlu: {self.titlu}")
        print(f"Regizor: {self.regizor}")
        print(f"An aparitie: {self.an_aparitie}")


class Muzica(Leaf):
    def __init__(self):
        self.titlu = input("Introduceti titlul albumului muzical: ")
        self.artist = AutorBuilder().set_nume(input("Introduceti numele artistului: ")).set_prenume(
            input("Introduceti prenumele artistului: ")).build()
        self.an_aparitie = int(input("Introduceti anul aparitiei: "))
        super().__init__(self)

    def afisare(self):
        print(f"Titlu: {self.titlu}")
        print(f"Artist: {self.artist}")
        print(f"An aparitie: {self.an_aparitie}")


class Biblioteca(Composite):
    def afisare(self):
        for child in self._children:
            child.operation()


# Exemplu de utilizare a pattern-ului Composite
biblioteca = Biblioteca()

# adaugam obiecte Leaf (Carte, Film, Muzica) in biblioteca
biblioteca.add(Carte())
biblioteca.add(Carte())
biblioteca.add(Film())
biblioteca.add(Muzica())

# apelam metoda afisare a obiectului Composite (Biblioteca) pentru a afisa 
# informatiile despre toate obiectele adaugate
biblioteca.afisare()

# ResursaPrototype astfel incat sa devina clasa abstracta Component, clasa CartePrototype,
# FilmPrototype si MuzicaPrototype sa devina clase Leaf si clasa Biblioteca sa devina clasa Composite.
