from Structural.prototype import CartePrototype, FilmPrototype, MuzicaPrototype


class ValidareTitlu:
    def __init__(self, succesor=None):
        self.succesor = succesor

    def valideaza(self, titlu):
        # Implementați logica de validare pentru titlu
        # Returnați True dacă titlul este valid sau apelați succesorul pentru a continua validarea
        if len(titlu) >= 8:
            if self.succesor is not None:
                return self.succesor.valideaza(titlu)
            else:
                return True
        else:
            return False

class ValidareAutor:
    def __init__(self, succesor=None):
        self.succesor = succesor

    def valideaza(self, autor):
        # Implementați logica de validare pentru autor (nume și prenume)
        # Returnați True dacă autorul este valid sau apelați succesorul pentru a continua validarea
        if len(autor.nume) >= 5 and len(autor.prenume) >= 5:  
            if self.succesor is not None:
                return self.succesor.valideaza(autor)
            else:
                return True
        else:
            return False

class ValidareRegizor:
    def __init__(self, succesor=None):
        self.succesor = succesor
   
    def valideaza(self, regizor):
        # Returnați True dacă autorul este valid sau apelați succesorul pentru a continua validarea
        if len(regizor.nume) >= 5 and len(regizor.prenume) >= 5:  
            if self.succesor is not None:
                return self.succesor.valideaza(regizor)
            else:
                return True
        else:
            return False

class ValidareArtist:
    def __init__(self, succesor=None):
        self.succesor = succesor
   
    def valideaza(self, artist):
        # Returnați True dacă autorul este valid sau apelați succesorul pentru a continua validarea
        if len(artist.nume) >= 5 and len(artist.prenume) >= 5:  
            if self.succesor is not None:
                return self.succesor.valideaza(artist)
            else:
                return True
        else:
            return False

class ValidareEditura:
    def __init__(self, succesor=None):
        self.succesor = succesor

    def valideaza(self, editura):
        # Implementați logica de validare pentru editură
        # Returnați True dacă editura este validă sau apelați succesorul pentru a continua validarea
        if len(editura) >= 8:
            if self.succesor is not None:
                return self.succesor.valideaza(editura)
            else:
                return True
        else:
            return False

class ValidareAn:
    def __init__(self, succesor=None):
        self.succesor = succesor

    def valideaza(self, an_aparitie):
        # Implementați logica de validare pentru an
        # Returnați True dacă anul este valid sau apelați succesorul pentru a continua validarea
        if an_aparitie >= 1955 and an_aparitie <= 2023:  # Modificați condițiile la valorile dorite
            if self.succesor is not None:
                return self.succesor.valideaza(an_aparitie)
            else:
                return True
        else:
            return False

class ValidareChain:
    def __init__(self):
        self.validare_titlu = ValidareTitlu()
        self.validare_autor = ValidareAutor()
        self.validare_editura = ValidareEditura()
        self.validare_an = ValidareAn()
        self.validare_regizor = ValidareRegizor()
        

    def valideaza_carte(self, carte):
        # Începeți validarea în lanț pentru carte
        if self.validare_titlu.valideaza(carte.titlu):
            if self.validare_autor.valideaza(carte.autor):
                if self.validare_editura.valideaza(carte.editura):
                    print("Cartea este validă.")
                else:
                    print("Editura nu este validă.")
            else:
                print("Autorul nu este valid.")
        else:
            print("Titlul nu este valid.")
    
    def valideaza_film(self, film):
        # Începeți validarea în lanț pentru carte
        if self.validare_titlu.valideaza(film.titlu):
            if self.validare_regizor.valideaza(film.regizor):
                if self.validare_an.valideaza(film.an_aparitie):
                    print("filmul este validă.")
                else:
                    print("anul nu este validă.")
            else:
                print("regizor nu este valid.")
        else:
            print("filmul nu este valid.")
            
    def valideaza_album(self, album):
        # Începeți validarea în lanț pentru carte
        if self.validare_titlu.valideaza(album.titlu):
            if self.validare_regizor.valideaza(album.artist):
                if self.validare_an.valideaza(album.an_aparitie):
                    print("albumul muzical este validă.")
                else:
                    print("anul nu este validă.")
            else:
                print("artist nu este valid.")
        else:
            print("albumul muzical nu este valid.")

carte_prototype = CartePrototype()
# Creăm lanțul de responsabilitate pentru carte
validare_chain_carte = ValidareChain()
# Validează cartea folosind lanțul de responsabilitate pentru carte
validare_chain_carte.valideaza_carte(carte_prototype)

film_prototype = FilmPrototype()
# Creăm lanțul de responsabilitate pentru film
validare_chain_film = ValidareChain()
# Validează filmul folosind lanțul de responsabilitate pentru film
validare_chain_film.valideaza_film(film_prototype)

muzica_prototype = MuzicaPrototype()
# Creăm lanțul de responsabilitate pentru film
validare_chain_film = ValidareChain()
# Validează filmul folosind lanțul de responsabilitate pentru film
validare_chain_film.valideaza_album(muzica_prototype)



# am creat trei clase separate pentru validarea titlului,
# autorului și editurii, care pot fi personalizate în funcție de nevoile dvs. 
# de validare. Apoi, am creat clasa ValidareChain care utilizează aceste clase 
# pentru a crea un lanț de responsabilitate. Când apelăm metoda valideaza() pe obiectul 
# ValidareChain, acesta va începe validarea în lanț, trecând prin fiecare verificare 
# în ordine, până când o verificare eșuează sau până când toate verificările sunt trecute 
# cu succes. Aceasta oferă flexibilitate în adăugarea și modificarea funcționalității de 
# validare în lanțul de responsabilitate, fără a afecta codul clientului.