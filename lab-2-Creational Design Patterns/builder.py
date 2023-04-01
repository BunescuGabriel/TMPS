
#  pattern-ului Builder pentru clasa Autor în Python

class AutorBuilder:
    def __init__(self):
        self.nume = ""
        self.prenume = ""
        self.nationalitate = None
        self.an_nastere = None

    def set_nume(self, nume):
        self.nume = nume
        return self

    def set_prenume(self, prenume):
        self.prenume = prenume
        return self

    def set_nationalitate(self, nationalitate):
        self.nationalitate = nationalitate
        return self

    def set_an_nastere(self, an_nastere):
        self.an_nastere = an_nastere
        return self

    def build(self):
        return Autor(self.nume, self.prenume, self.nationalitate, self.an_nastere)


class Autor:
    def __init__(self, nume, prenume, nationalitate=None, an_nastere=None):
        self.nume = nume
        self.prenume = prenume
        self.nationalitate = nationalitate
        self.an_nastere = an_nastere

    def __str__(self):
        return f"{self.nume} {self.prenume} ({self.nationalitate}, {self.an_nastere})"

# autor_builder = AutorBuilder()

# autor_builder.set_nume(input("Introduceți numele autorului: "))
# autor_builder.set_prenume(input("Introduceți prenumele autorului: "))
# autor_builder.set_nationalitate(input("Introduceți naționalitatea autorului: "))
# autor_builder.set_an_nastere(input("Introduceți anul nașterii autorului: "))

# autor = autor_builder.build()
# print(autor)




# Clasa AutorBuilder este clasa Builder care conține metodele set_XXX() pentru a 
# seta valorile atributelor obiectului Autor. În constructorul clasei AutorBuilder, 
# toate atributele sunt inițializate cu valori implicite (de exemplu, string-ul gol pentru nume 
# și prenume și None pentru naționalitate și anul nașterii).

# Metodele set_XXX() primesc valorile pentru fiecare atribut și le setează în 
# obiectul AutorBuilder. Aceste metode returnează întotdeauna instanța obiectului 
# AutorBuilder astfel încât să putem utiliza mai multe metode înlănțuite.

# Metoda build() este metoda care construiește obiectul Autor folosind valorile setate
# în obiectul AutorBuilder. Această metodă returnează obiectul Autor construit.

# În exemplul de utilizare, am creat un obiect AutorBuilder și am 
# utilizat metodele set_XXX() pentru a seta valorile pentru fiecare atribut. 
# După aceea, am apelat metoda build() pentru a construi obiectul Autor și l-am 
# afișat folosind metoda __str__() a clasei Autor.