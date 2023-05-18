
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




