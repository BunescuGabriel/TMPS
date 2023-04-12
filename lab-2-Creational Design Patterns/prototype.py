import copy
from builder import AutorBuilder

class ResursaPrototype:
    def __init__(self, tip):
        self.tip = tip
        
    def clone(self):
        return copy.deepcopy(self)

# am creat observatori pentru produsele

class CartePrototype(ResursaPrototype):
    def __init__(self):
        super().__init__("Carte")
        self.titlu = input("Introduceti titlul cartii: ")
        self.autor = AutorBuilder().set_nume(input("Introduceti numele autorului: ")).set_prenume(
            input("Introduceti prenumele autorului: ")).build()
        self.editura = input("Introduceti numele editurii: ")
        self.observers = []
            
    def afisare(self):
        print(f"Tip resursa: {self.tip}")
        print(f"Titlu: {self.titlu}")
        print(f"Autor: {self.autor}")
        print(f"Editura: {self.editura}")

    def notify_observers(self, attribute, vechi, nou):
        for observer in self.observers:
            observer.update(attribute, self, vechi, nou)
        print(f"Modificarea atributului '{attribute}' a fost notificată observatorilor.")

    def modifica_titlu(self, titlu_nou):
        titlu_vechi = self.titlu
        self.titlu = titlu_nou
        self.notify_observers("Titlu", titlu_vechi, titlu_nou)
        print(f"Titlul a fost modificat cu succes. Notificare trimisă observatorilor.")

    def modifica_autor(self, autor_nou):
        autor_vechi = self.autor
        self.autor = autor_nou
        self.notify_observers("Autor", autor_vechi, autor_nou)
        print(f"Autorul a fost modificat cu succes. Notificare trimisă observatorilor.")


    def register_observer(self, observer):
        nume_observator = input("Introduceti numele observatorului: ") # Adăugăm input pentru a introduce numele observatorului
        observer.nume = nume_observator # Setăm numele observatorului
        self.observers.append(observer)
        print(f"Observatorul '{nume_observator}' a fost înregistrat cu succes.")
        
class FilmPrototype(ResursaPrototype):
    def __init__(self):
        super().__init__("Film")
        self.titlu = input("Introduceti titlul filmului: ")
        self.regizor = AutorBuilder().set_nume(input("Introduceti numele regizorului: ")).set_prenume(
            input("Introduceti prenumele regizorului: ")).build()
        self.an_aparitie = int(input("Introduceti anul aparitiei: "))
        self.observers = []

    def afisare(self):
        print(f"Tip resursa: {self.tip}")
        print(f"Titlu: {self.titlu}")
        print(f"Regizor: {self.regizor}")
        print(f"An aparitie: {self.an_aparitie}")
    
    def notify_observers(self, attribute, vechi, nou):
        for observer in self.observers:
            observer.update(attribute, self, vechi, nou)
        print(f"Modificarea atributului '{attribute}' a fost notificată observatorilor.")

    def modifica_titlu(self, titlu_nou):
        titlu_vechi = self.titlu
        self.titlu = titlu_nou
        self.notify_observers("Titlu", titlu_vechi, titlu_nou)
        print(f"Titlul a fost modificat cu succes. Notificare trimisă observatorilor.")
        
    def modifica_regizor(self, regizor_nou):
        regizor_vechi = self.regizor
        self.regizor = regizor_nou
        self.notify_observers("Regizor", regizor_vechi, regizor_nou)
        print(f"Regizorul a fost modificat cu succes. Notificare trimisă observatorilor.")  

    def register_observer(self, observer):
        nume_observator = input("Introduceti numele observatorului de film: ")
        observer.nume = nume_observator
        self.observers.append(observer)
        print(f"Observatorul de film '{nume_observator}' a fost înregistrat cu succes.")
         
class MuzicaPrototype(ResursaPrototype):
    def __init__(self):
        super().__init__("albumului muzical")
        self.titlu = input("Introduceti titlul albumului muzical: ")
        self.artist = AutorBuilder().set_nume(input("Introduceti numele artistului: ")).set_prenume(
            input("Introduceti prenumele artistului: ")).build()
        self.an_aparitie = int(input("Introduceti anul aparitiei: "))
        self.observers = []

    def afisare(self):
        print(f"Tip resursa: {self.tip}")
        print(f"Titlu: {self.titlu}")
        print(f"Artist: {self.artist}")
        print(f"An aparitie: {self.an_aparitie}")
    
    def notify_observers(self, attribute, vechi, nou):
        for observer in self.observers:
            observer.update(attribute, self, vechi, nou)
        print(f"Modificarea atributului '{attribute}' a fost notificată observatorilor.")

    def modifica_titlu(self, titlu_nou):
        titlu_vechi = self.titlu
        self.titlu = titlu_nou
        self.notify_observers("Titlu", titlu_vechi, titlu_nou)
        print(f"Titlul a fost modificat cu succes. Notificare trimisă observatorilor.")
         
    def modifica_artist(self, artist_nou):
        artist_vechi = self.artist
        self.artist = artist_nou
        self.notify_observers("Regizor", artist_vechi, artist_nou)
        print(f"Artistul a fost modificat cu succes. Notificare trimisă observatorilor.")
        
    def register_observer(self, observer):
        nume_observator = input("Introduceti numele observatorului de film: ")
        observer.nume = nume_observator
        self.observers.append(observer)
        print(f"Observatorul de film '{nume_observator}' a fost înregistrat cu succes.")
            
class Observer:
    def __init__(self):
        self.nume = ""

    def update(self, attribute, resource, vechi, nou):
        print(f"Observatorul '{self.nume}' a primit o notificare: atributul '{attribute}' al resursei '{resource.tip}' a fost modificat.")
        print(f"Valoarea veche: '{vechi}'. Valoarea nouă: '{nou}'.")
      


carte_prototype = CartePrototype()
carte_prototype.afisare()
# Crearea obiectului de tip Observer
observer = Observer()
# Înregistrarea observatorului la obiectul de tip CartePrototype
carte_prototype.register_observer(observer)


film_prototype = FilmPrototype()
film_prototype.afisare()
# Crearea obiectului de tip Observer
observer = Observer()
film_prototype.register_observer(observer)

muzica_prototype = MuzicaPrototype()
muzica_prototype.afisare()

# Crearea obiectului de tip Observer
observer = Observer()
muzica_prototype.register_observer(observer)



# Acesta definește o clasă prototip care servește drept șablon pentru crearea 
# altor obiecte prin clonare. În acest caz, clasa ResursaPrototype este
# clasa prototip, iar clasele CartePrototype, FilmPrototype și MuzicaPrototype 
# sunt implementări ale acesteia care definesc obiecte specifice pe care le putem clona.

# Metoda clone definită în clasa ResursaPrototype este cea care face posibilă 
# clonarea obiectelor, utilizând funcția deepcopy din biblioteca copy.

# Astfel, putem crea noi obiecte de tip CartePrototype, FilmPrototype sau 
# MuzicaPrototype prin clonarea obiectelor existente, astfel evitând construirea 
# de la zero a fiecărui obiect.