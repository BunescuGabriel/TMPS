
# Utilizarea unui Factory pentru a crea obiecte de tip Carte, Filme sau Muzica în
# funcție de tipul de resursă pe care îl caută utilizatorii bibliotecii.
from builder import AutorBuilder
from abc import ABC, abstractmethod


class Resursa(ABC):
    @abstractmethod
    def afisare(self):
        pass


class Carte(Resursa):
    def __init__(self, denumire, autor):
        self.denumire = denumire
        self.autor = autor

    def afisare(self):
        print(
            f"Aceasta este cartea '{self.denumire}' scrisă de {self.autor}")


class Film(Resursa):
    def __init__(self, denumire, autor):
        self.denumire = denumire
        self.autor = autor

    def afisare(self):
        print(
            f"Acesta este filmul '{self.denumire}' regizat de {self.autor}")


class Muzica(Resursa):
    def __init__(self, denumire, autor):
        self.denumire = denumire
        self.autor = autor

    def afisare(self):
        print(
            f"Acesta este un album muzical '{self.denumire}' creat de {self.autor}")


class ResursaFactory:
    def creare_resursa(self, tip):
        if tip == "carte":
            denumire = input("Introduceti denumirea cartii: ")
            autor_builder = AutorBuilder()
            autor_builder.set_nume(
                input("Introduceti numele autorului: "))
            autor_builder.set_prenume(
                input("Introduceti prenumele autorului: "))
            autor_builder.set_nationalitate(
                input("Introduceti nationalitatea autorului: "))
            autor_builder.set_an_nastere(
                int(input("Introduceti anul nasterii al autorului: ")))
            autor = autor_builder.build()
            return Carte(denumire, autor)
        elif tip == "film":
            denumire = input("Introduceti denumirea filmului: ")
            autor_builder = AutorBuilder()
            autor_builder.set_nume(input("Introduceti numele regizorului: "))
            autor_builder.set_prenume(input("Introduceti prenumele regizorului: "))
            autor_builder.set_nationalitate(
                input("Introduceti nationalitatea regizorului: "))
            autor_builder.set_an_nastere(
                int(input("Introduceti anul nasterii al regizorului: ")))
            autor = autor_builder.build()
            return Film(denumire, autor)
        
        elif tip == "muzica":
            denumire = input("Introduceti denumirea albumului muzical: ")
            autor_builder = AutorBuilder()
            autor_builder.set_nume(input("Introduceti numele artistului: "))
            autor_builder.set_prenume(input("Introduceti prenumele artistului: "))
            autor_builder.set_nationalitate(
                input("Introduceti nationalitatea artistului: "))
            autor_builder.set_an_nastere(
                int(input("Introduceti anul nasterii al artistului: ")))
            autor = autor_builder.build()
            return Muzica(denumire, autor)

factory = ResursaFactory()


carte = factory.creare_resursa("carte")
film = factory.creare_resursa("film")
album = factory.creare_resursa("muzica")


carte.afisare()  # Output: "Aceasta este cartea 'nume_carte'"
film.afisare()  # Output: "Acesta este filmul 'nume_film'"
album.afisare()  # Output: "Acesta este un album muzical"


# Clasa Resursa este o clasă abstractă care definește metoda afisare() pe care toate
# clasele care o moștenesc trebuie să o implementeze. Clasele Carte, Film și Muzica sunt
# clase concrete care moștenesc clasa Resursa și
# implementează metoda afisare() în mod specific pentru fiecare tip de resursă.

# Clasa ResursaFactory este o clasă Factory care are o metodă creare_resursa() care primește
# un parametru tip și returnează o instanță a clasei corespunzătoare tipului de resursă. Astfel,
# în funcție de tipul de resursă cerut de utilizator, se poate crea obiectul
# corespunzător folosind Factory-ul.
