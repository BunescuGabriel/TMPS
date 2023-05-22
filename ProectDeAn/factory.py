from abc import ABC, abstractmethod

from faker.generator import random

from builder import AutorBuilder
from generator_of_observator import fake, nume_generare


class Resursa(ABC):
    @abstractmethod
    def afisare(self):
        pass


class Carte:
    def __init__(self, titlu, autor, editura):
        self.tip = "carte"
        self.titlu = titlu
        self.autor = autor
        self.editura = editura
        self.observers = []
        self.pret = None
        self.procentaj_reducere = None
        self.cod_unic = None

    def set_pret(self, pret):
        self.pret = pret

    def set_procentaj_reducere(self, procentaj_reducere):
        self.procentaj_reducere = procentaj_reducere

    def set_cod_unic(self, cod_unic):
        self.cod_unic = cod_unic

    def afisare(self):
        print(f"Tip resursa: {self.tip}")
        print(f"Aceasta este titlul cartii: '{self.titlu}'.")
        print(f"Scrisă de: '{self.autor}'.")
        print(f"Editată de: '{self.editura}'. ")
        print()

        if self.pret is not None:
            print(f"Pret: {self.pret}")
        if self.procentaj_reducere is not None:
            pret_redus = self.pret * (1 - self.procentaj_reducere / 100)
            print(f"Pret cu reducere de {self.procentaj_reducere}%: {pret_redus:.2f} USD")
        if self.cod_unic is not None:
            print(f"Procentaj reducere: {self.cod_unic}")

    def modifica_titlu(self, titlu_nou):
        titlu_vechi = self.titlu
        self.titlu = titlu_nou
        self.notify_observers("Titlu", titlu_vechi, titlu_nou)

    def modifica_autor(self, autor_nou):
        autor_vechi = self.autor
        self.autor = autor_nou
        self.notify_observers("Autor", autor_vechi, autor_nou)

    def notify_observers(self, attribute, vechi, nou):
        for observer in self.observers:
            observer.update(attribute, self, vechi, nou)
        print(f"Modificarea atributului '{attribute}' a fost notificată observatorilor.")
        print()

    def register_observer(self, observer):
        nume_observator = random.choice(nume_generare)  # Generate a random name from nume_generare
        # nume_observator = input("Introduceți numele observatorului: ")
        observer.nume = nume_observator
        self.observers.append(observer)
        print(f"Observatorul '{nume_observator}' a fost înregistrat cu succes.")


class Film(Resursa):
    def __init__(self, titlu, regizor, an_aparitie):
        self.tip = "Film"
        self.titlu = titlu
        self.autor = regizor
        self.an_aparitie = an_aparitie
        self.observers = []
        self.pret = None
        self.procentaj_reducere = None
        self.cod_unic = None

    def set_pret(self, pret):
        self.pret = pret

    def set_procentaj_reducere(self, procentaj_reducere):
        self.procentaj_reducere = procentaj_reducere

    def set_cod_unic(self, cod_unic):
        self.cod_unic = cod_unic

    def modifica_titlu(self, titlu_nou):
        titlu_vechi = self.titlu
        self.titlu = titlu_nou
        self.notify_observers("Titlu", titlu_vechi, titlu_nou)
        print(f"Titlul a fost modificat cu succes. Notificare trimisă observatorilor.")

    def modifica_regizor(self, regizor_nou):
        regizor_vechi = self.autor
        self.autor = regizor_nou
        self.notify_observers("Regizor", regizor_vechi, regizor_nou)
        print(f"Regizorul a fost modificat cu succes. Notificare trimisă observatorilor.")

    def afisare(self):
        print(f"Tip resursa: {self.tip}")
        print(f"Aceasta este titlul filmul: '{self.titlu}'.")
        print(f"regizat de: '{self.autor}'.")
        print(f"anul aparitii este: '{self.an_aparitie}'. ")
        print()

        if self.pret is not None:
            print(f"Pret: {self.pret}")
        if self.procentaj_reducere is not None:
            pret_redus = self.pret * (1 - self.procentaj_reducere / 100)
            print(f"Pret cu reducere de {self.procentaj_reducere}%: {pret_redus:.2f} USD")
        if self.cod_unic is not None:
            print(f"Procentaj reducere: {self.cod_unic}")

    def notify_observers(self, attribute, vechi, nou):
        for observer in self.observers:
            observer.update(attribute, self, vechi, nou)
        print(f"Modificarea atributului '{attribute}' a fost notificată observatorilor.")
        print()

    def register_observer(self, observer):
        nume_observator = random.choice(nume_generare)  # Generate a random name from nume_generare
        # nume_observator = input("Introduceți numele observatorului: ")
        observer.nume = nume_observator
        self.observers.append(observer)
        print(f"Observatorul '{nume_observator}' a fost înregistrat cu succes.")


class Muzica(Resursa):
    def __init__(self, titlu, artist, an_aparitie):
        self.tip = "muzica"
        self.titlu = titlu
        self.autor = artist
        self.an_aparitie = an_aparitie
        self.observers = []
        self.pret = None
        self.procentaj_reducere = None
        self.cod_unic = None

    def set_pret(self, pret):
        self.pret = pret

    def set_procentaj_reducere(self, procentaj_reducere):
        self.procentaj_reducere = procentaj_reducere

    def set_cod_unic(self, cod_unic):
        self.cod_unic = cod_unic

    def afisare(self):
        print(f"Tip resursa: {self.tip}")
        print(f"Aceasta este titlul album muzical: '{self.titlu}'.")
        print(f"artistul este: '{self.autor}'.")
        print(f"anul aparitii este: '{self.an_aparitie}'. ")
        print()

        if self.pret is not None:
            print(f"Pret: {self.pret}")
        if self.procentaj_reducere is not None:
            pret_redus = self.pret * (1 - self.procentaj_reducere / 100)
            print(f"Pret cu reducere de {self.procentaj_reducere}%: {pret_redus:.2f} USD")
        if self.cod_unic is not None:
            print(f"Procentaj reducere: {self.cod_unic}")

    def notify_observers(self, attribute, vechi, nou):
        for observer in self.observers:
            observer.update(attribute, self, vechi, nou)
        print(f"Modificarea atributului '{attribute}' a fost notificată observatorilor.")
        print()

    def modifica_titlu(self, titlu_nou):
        titlu_vechi = self.titlu
        self.titlu = titlu_nou
        self.notify_observers("Titlu", titlu_vechi, titlu_nou)
        print(f"Titlul a fost modificat cu succes. Notificare trimisă observatorilor.")

    def modifica_artist(self, artist_nou):
        artist_vechi = self.autor
        self.autor = artist_nou
        self.notify_observers("Artistul", artist_vechi, artist_nou)
        print(f"Artistul a fost modificat cu succes. Notificare trimisă observatorilor.")

    def register_observer(self, observer):
        nume_observator = random.choice(nume_generare)  # Generate a random name from nume_generare
        # nume_observator = input("Introduceți numele observatorului: ")
        observer.nume = nume_observator
        self.observers.append(observer)
        print(f"Observatorul '{nume_observator}' a fost înregistrat cu succes.")


class ResursaDecorator:
    def __init__(self, resursa, pret):
        self.resursa = resursa
        self.pret = pret

    def afisare(self):
        self.resursa.afisare()
        # print(f"Pret: {self.pret} USD")


class ReducereDecorator:
    def __init__(self, resursa, procentaj_reducere):
        self.resursa = resursa
        self.procentaj_reducere = procentaj_reducere

    def afisare(self):
        self.resursa.afisare()
        pret_redus = self.resursa.pret * (1 - self.procentaj_reducere / 100)
        # print(f"Pret cu reducere de {self.procentaj_reducere}%: {pret_redus:.2f} USD")


class CodUnicDecorator:
    _contor = 0

    def __init__(self, resursa):
        self.resursa = resursa
        CodUnicDecorator._contor += 1
        self.cod_unic = f"CodProdus{CodUnicDecorator._contor}"
        self.tip = type(resursa).__name__

    def afisare(self):
        self.resursa.afisare()
        # print(f"Cod unic produs: {self.cod_unic}")


class ResursaFactory:
    def creare_resursa(self, tip):
        if tip == "carte":
            titlu = input("Introduceti titlu cartii: ")
            autor_builder = AutorBuilder().set_nume(
                input("Introduceti numele autorului: ")).set_prenume(
                input("Introduceti prenumele autorului: ")).set_nationalitate(
                input("Introduceti nationalitatea autorului: ")).set_an_nastere(
                int(input("Introduceti anul nasterii al autorului: ")))
            autor = autor_builder.build()
            editara = input("Introduceti numele editurii: ")
            return Carte(titlu, autor, editara)

        elif tip == "film":
            titlu = input("Introduceti titlu filmului: ")
            autor_builder = AutorBuilder()
            autor_builder.set_nume(input("Introduceti numele regizorului: "))
            autor_builder.set_prenume(input("Introduceti prenumele regizorului: "))
            autor_builder.set_nationalitate(
                input("Introduceti nationalitatea regizorului: "))
            autor_builder.set_an_nastere(
                int(input("Introduceti anul nasterii al regizorului: ")))
            regizor = autor_builder.build()
            an_aparitie = int(input("Introduceti anul aparitiei: "))
            return Film(titlu, regizor, an_aparitie)

        elif tip == "muzica":
            titlu = input("Introduceti titlu albumului muzical: ")
            autor_builder = AutorBuilder()
            autor_builder.set_nume(input("Introduceti numele artistului: "))
            autor_builder.set_prenume(input("Introduceti prenumele artistului: "))
            autor_builder.set_nationalitate(
                input("Introduceti nationalitatea artistului: "))
            autor_builder.set_an_nastere(
                int(input("Introduceti anul nasterii al artistului: ")))
            artist = autor_builder.build()
            an_aparitie = int(input("Introduceti anul aparitiei: "))
            return Muzica(titlu, artist, an_aparitie)


class Observer:
    def __init__(self):
        self.nume = ""

    def update(self, attribute, resource, vechi, nou):
        print(
            f"Observatorul '{self.nume}' a primit o notificare: atributul '{attribute}' al resursei '{resource.tip}' a fost modificat.")
        print(f"Valoarea veche: '{vechi}'. "
              f"Valoarea nouă: '{nou}'.")

