from prototype import CartePrototype, FilmPrototype, MuzicaPrototype


class ResourceAdapter:
    def __init__(self, resource):
        self.resource = resource

    def get_title(self):
        return self.resource.titlu
    
    def get_author(self):
        if isinstance(self.resource, CartePrototype):
            return self.resource.autor.get_full_name()
        elif isinstance(self.resource, FilmPrototype):
            return self.resource.regizor.get_full_name()
        elif isinstance(self.resource, MuzicaPrototype):
            return self.resource.artist.get_full_name()

    def get_year(self):
        return self.resource.an_aparitie

    def display(self):
        self.resource.afisare()

carte_prototype = CartePrototype()
film_prototype = FilmPrototype()
muzica_prototype = MuzicaPrototype()

adapter1 = ResourceAdapter(carte_prototype)
adapter2 = ResourceAdapter(film_prototype)
adapter3 = ResourceAdapter(muzica_prototype)

print(adapter1.get_title())  # prints the title of the book
print(adapter1.get_author())  # prints the name of the author of the book
print(adapter1.get_year())  # prints the year of publication of the book

print(adapter2.get_title())  # prints the title of the book
print(adapter2.get_author())  # prints the name of the author of the book
print(adapter2.get_year())  # prints the year of publication of the book

print(adapter3.get_title())  # prints the title of the book
print(adapter3.get_author())  # prints the name of the author of the book
print(adapter3.get_year())  # prints the year of publication of the book

# Clasa ResourceAdapter preia o instanță a oricăruia dintre CartePrototype,
# Clasele FilmPrototype sau MuzicaPrototype în constructorul său. Oferă trei
# metode get_title(), get_author() și get_year(), care returnează titlul, autorul,
# și, respectiv, anul resursei. Metoda get_author() folosește isinstance()
# pentru a determina tipul de resursă și returnează numele complet al autorului sau regizorului,
# în funcție de tip. În cele din urmă, metoda display() apelează metoda afisare() a resursei
# pentru a-i afișa detaliile.

# Puteți utiliza acest adaptor pentru a lucra cu oricare dintre CartePrototype, FilmPrototype sau MuzicaPrototype
# obiecte, ca acesta: