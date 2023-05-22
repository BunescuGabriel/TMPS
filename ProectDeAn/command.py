
# aici sunt reprezentate patternurile command si chain of responsability
# pentru obiectele carte, film si muzica


class ModificaTitluCarteCommand:
    def __init__(self, carte, titlu_nou):
        self.carte = carte
        self.titlu_nou = titlu_nou

    def execute(self):
        self.carte.modifica_titlu(self.titlu_nou)


class ModificaAutorCarteCommand:
    def __init__(self, carte, autor_nou):
        self.carte = carte
        self.autor_nou = autor_nou

    def execute(self):
        self.carte.modifica_autor(self.autor_nou)


class ModificaTitluFilmCommand:
    def __init__(self, film, titlu_nou):
        self.film = film
        self.titlu_nou = titlu_nou

    def execute(self):
        self.film.modifica_titlu(self.titlu_nou)


class ModificaRegizorFilmCommand:
    def __init__(self, film, regizor_nou):
        self.film = film
        self.regizor_nou = regizor_nou

    def execute(self):
        self.film.modifica_regizor(self.regizor_nou)


class ModificaTitluMuzicaCommand:
    def __init__(self, album, titlu_nou):
        self.album = album
        self.titlu_nou = titlu_nou

    def execute(self):
        self.album.modifica_titlu(self.titlu_nou)


class ModificaArtistMuzicaCommand:
    def __init__(self, album, artist_nou):
        self.album = album
        self.artist_nou = artist_nou

    def execute(self):
        self.album.modifica_artist(self.artist_nou)



class ValidareTitlu:
    def __init__(self, succesor=None):
        self.succesor = succesor

    def valideaza(self, titlu):
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
        if len(editura) >= 5:
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
        if an_aparitie >= 1455 and an_aparitie <= 2023:  # Modificați condițiile la valorile dorite
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
        if self.validare_titlu.valideaza(carte.titlu) and \
                self.validare_autor.valideaza(carte.autor) and \
                self.validare_editura.valideaza(carte.editura):
            print("Cartea este validă.")
        else:
            print("Cartea nu este validă.")

    def valideaza_film(self, film):
        # Începeți validarea în lanț pentru carte
        if self.validare_titlu.valideaza(film.titlu) and \
                self.validare_regizor.valideaza(film.autor) and \
                self.validare_an.valideaza(film.an_aparitie):
            print("filmul este validă.")
        else:
            print("filmul nu este valid.")

    def valideaza_album(self, album):
        # Începeți validarea în lanț pentru carte
        if self.validare_titlu.valideaza(album.titlu) and \
                self.validare_regizor.valideaza(album.autor) and \
                self.validare_an.valideaza(album.an_aparitie):
            print("albumul muzical este validă.")
        else:
            print("albumul muzical nu este valid.")
