from Creational.prototype import muzica_prototype, carte_prototype, film_prototype

class ModificaTitluCarteCommand:
    def __init__(self, carte_prototype, titlu_nou):
        self.carte_prototype = carte_prototype
        self.titlu_nou = titlu_nou

    def execute(self):
        titlu_vechi = self.carte_prototype.titlu
        self.carte_prototype.modifica_titlu(self.titlu_nou)
        print(f"Titlul cărții a fost modificat cu succes! Titlu vechi: '{titlu_vechi}'. Titlu nou: '{self.titlu_nou}'.")

class ModificaAutorCarteCommand:
    def __init__(self, carte_prototype, autor_nou):
        self.carte_prototype = carte_prototype
        self.autor_nou = autor_nou

    def execute(self):
        autor_vechi = self.carte_prototype.autor
        self.carte_prototype.modifica_autor(self.autor_nou)
        print(f"Autorul cărții a fost modificat cu succes! Autorul vechi: '{autor_vechi}'. Autorul nou: '{self.autor_nou}'.")
        
class ModificaTitluFilmCommand:
    def __init__(self, film_prototype, titlu_nou):
        self.film_prototype = film_prototype
        self.titlu_nou = titlu_nou

    def execute(self):
        titlu_vechi = self.film_prototype.titlu
        self.film_prototype.modifica_titlu(self.titlu_nou)
        print(f"Titlul filmului a fost modificat cu succes! Titlu vechi: '{titlu_vechi}'. Titlu nou: '{self.titlu_nou}'.")

class ModificaRegizorFilmCommand:
    def __init__(self, film_prototype, regizor_nou):
        self.film_prototype = film_prototype
        self.regizor_nou = regizor_nou

    def execute(self):
        regizor_vechi = self.film_prototype.regizor
        self.film_prototype.modifica_regizor(self.regizor_nou)
        print(f"Regizor filmului a fost modificat cu succes! Regizor vechi: '{regizor_vechi}'. Regizor nou: '{self.regizor_nou}'.")

class ModificaTitluMuzicaCommand:
    def __init__(self, muzica_prototype, titlu_nou):
        self.muzica_prototype = muzica_prototype
        self.titlu_nou = titlu_nou

    def execute(self):
        titlu_vechi = self.muzica_prototype.titlu
        self.muzica_prototype.modifica_titlu(self.titlu_nou)
        print(f"Titlul albumului muzical a fost modificat cu succes! Titlu vechi: '{titlu_vechi}'. Titlu nou: '{self.titlu_nou}'.")

class ModificaArtistMuzicaCommand:
    def __init__(self, muzica_prototype, artist_nou):
        self.muzica_prototype = muzica_prototype
        self.artist_nou = artist_nou
        
    def execute(self):
        artist_vechi = self.muzica_prototype.artist
        self.muzica_prototype.modifica_artist(self.artist_nou)
        print(f"Artistul albumului muzical a fost modificat cu succes! Artistul vechi: '{artist_vechi}'. Artistul nou: '{self.artist_nou}'.")


# Creăm obiectul de tip comandă și îl executăm
titlu_nou = input("Introduceți noul titlu al cărții: ")
comanda_modifica_titlu_carte = ModificaTitluCarteCommand(carte_prototype, titlu_nou)
comanda_modifica_titlu_carte.execute()

# Afișăm cartea modificată
carte_prototype.afisare()

autor_nou = input("Introduceți noul autor al cărții: ")
comanda_modifica_autor_carte = ModificaAutorCarteCommand(carte_prototype, autor_nou)
comanda_modifica_autor_carte.execute()

carte_prototype.afisare()

titlu_nou = input("Introduceți noul titlu al filmului: ")
comanda_modifica_titlu_filmul = ModificaTitluFilmCommand(film_prototype, titlu_nou)
comanda_modifica_titlu_filmul.execute()

film_prototype.afisare()

regizor_nou = input("Introduceți noul regizor al filmului: ")
comanda_modifica_regizor_filmul = ModificaRegizorFilmCommand(film_prototype, regizor_nou)
comanda_modifica_regizor_filmul.execute()

film_prototype.afisare()

titlu_nou = input("Introduceți noul titlu al albumului muzical: ")
comanda_modifica_titlu_albumul = ModificaTitluMuzicaCommand(muzica_prototype, titlu_nou)
comanda_modifica_titlu_albumul.execute()

muzica_prototype.afisare()

artist_nou = input("Introduceți noul artist al albumului muzical: ")
comanda_modifica_artist_albumul = ModificaArtistMuzicaCommand(muzica_prototype, artist_nou)
comanda_modifica_artist_albumul.execute()

muzica_prototype.afisare()


#  putem crea o clasă separată pentru fiecare 
# comandă și să le asociem cu obiectele de tip CartePrototype, FilmPrototype și 
# MuzicaPrototype. Aceste clase ar trebui să implementeze o metodă de execuție a 
# comenzii, care să facă modificările corespunzătoare asupra obiectelor prototip 
# și să apeleze metoda de afișare pentru a afișa rezultatul modificărilor.
