from factory import ResursaFactory, ResursaDecorator, CodUnicDecorator, ReducereDecorator
from proxy import ProxyResursa


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
        if self.validare_titlu.valideaza(carte.titlu) and \
                self.validare_autor.valideaza(carte.autor) and \
                self.validare_editura.valideaza(carte.editara):
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

factory = ResursaFactory()

carte = factory.creare_resursa("carte")
pret = float(input("Introduceti pretul: "))
carte_pret = ResursaDecorator(carte, pret)
procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
carte_cu_reducere = CodUnicDecorator(ReducereDecorator(carte_pret, procentaj_reducere))
carte_cu_reducere.afisare()
# Creăm lanțul de responsabilitate pentru carte
validare_chain_carte = ValidareChain()
# Validează cartea folosind lanțul de responsabilitate pentru carte
validare_chain_carte.valideaza_carte(carte)


film = factory.creare_resursa("film")
pret = float(input("Introduceti pretul: "))
film_pret = ResursaDecorator(film, pret)
procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
film_cu_reducere = CodUnicDecorator(ReducereDecorator(film_pret, procentaj_reducere))
film_cu_reducere.afisare()
# Creăm lanțul de responsabilitate pentru film
validare_chain_film = ValidareChain()
# Validează filmul folosind lanțul de responsabilitate pentru film
validare_chain_film.valideaza_film(film)

album = factory.creare_resursa("muzica")
pret = float(input("Introduceti pretul: "))
album_pret = ResursaDecorator(album, pret)
procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
album_cu_reducere = CodUnicDecorator(ReducereDecorator(album_pret, procentaj_reducere))
album_cu_reducere.afisare()
# Creăm lanțul de responsabilitate pentru film
validare_chain_film = ValidareChain()
# Validează filmul folosind lanțul de responsabilitate pentru film
validare_chain_film.valideaza_album(album)



# Lista utilizatorilor autorizați
utilizatori_autorizati = ["user1", "user2", "user3"]

# Crearea instanțelor de proxy pentru fiecare dintre cele trei resurse
carte_proxy = ProxyResursa(carte_cu_reducere, utilizatori_autorizati)
film_proxy = ProxyResursa(film_cu_reducere, utilizatori_autorizati)
album_proxy = ProxyResursa(album_cu_reducere, utilizatori_autorizati)

# utilizarea resurselor prin intermediul proxy-ului
carte_proxy.afisare()
film_proxy.afisare()
album_proxy.afisare()




