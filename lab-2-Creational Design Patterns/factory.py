
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
        

class ResursaDecorator(Resursa):
    def __init__(self, resursa, pret):
        self.resursa = resursa
        self.pret = pret

    def afisare(self):
        self.resursa.afisare()
        print(f"Pret: {self.pret} USD")
        
class ReducereDecorator(Resursa):
    def __init__(self, resursa, procentaj_reducere):
        self.resursa = resursa
        self.procentaj_reducere = procentaj_reducere

    def afisare(self):
        self.resursa.afisare()
        pret_redus = self.resursa.pret * (1 - self.procentaj_reducere / 100)
        print(f"Pret cu reducere de {self.procentaj_reducere}%: {pret_redus:.2f} RON")
        
class CodUnicDecorator(Resursa):
    _contor = 0

    def __init__(self, resursa):
        self.resursa = resursa
        CodUnicDecorator._contor += 1
        self.cod_unic = f"CodProdus{CodUnicDecorator._contor}"

    def afisare(self):
        self.resursa.afisare()
        print(f"Cod unic produs: {self.cod_unic}")

class ResursaFactory:
    def creare_resursa(self, tip):
        if tip == "carte":
            denumire = input("Introduceti denumirea cartii: ")
            autor_builder = AutorBuilder().set_nume(
                input("Introduceti numele autorului: ")).set_prenume(
                input("Introduceti prenumele autorului: ")).set_nationalitate(
                input("Introduceti nationalitatea autorului: ")).set_an_nastere(
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





# Clasa ResursaFactory este o clasă Factory care are o metodă creare_resursa() care primește
# un parametru tip și returnează o instanță a clasei corespunzătoare tipului de resursă. Astfel,
# în funcție de tipul de resursă cerut de utilizator, se poate crea obiectul
# corespunzător folosind Factory-ul.

# Pentru a adăuga această funcționalitate, putem crea o clasă decorator care acceptă o resursă 
# ca argument și adaugă un preț la acea resursă. Noul decorator poate fi apoi utilizat pentru a 
# decora orice resursă existentă.
# Acest decorator primește o resursă și un preț ca argumente în constructorul său. Metoda afisare a 
# decoratorului afișează întâi informațiile despre resursă, apoi afișează prețul adăugat de decorator.

# Sigur! Am creat un decorator CodUnicDecorator care adaugă un cod unic la fiecare produs creat folosind
# un contor static care se mărește la fiecare produs creat.