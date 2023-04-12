


from Structural.factory import CodUnicDecorator, ReducereDecorator, Resursa, ResursaDecorator, ResursaFactory


class ProxyResursa(Resursa):
    def __init__(self, resursa, utilizatori_autorizati):
        self._resursa = resursa
        self._utilizatori_autorizati = utilizatori_autorizati

    def afisare(self):
        utilizator_curent = input("Introduceti numele dvs.: ")
        if utilizator_curent in self._utilizatori_autorizati:
            print("Alegeți o resursă:")
            print("1. Carte")
            print("2. Film")
            print("3. Album")
            optiune = int(input("Introduceți opțiunea dorită: "))
            if optiune == 1:
                print(self._resursa.afisare())
            elif optiune == 2:
                print(self._resursa.afisare())
            elif optiune == 3:
                print(self._resursa.afisare())
            else:
                print("Opțiune invalidă!")
        else:
            print(f"Accesul pentru {utilizator_curent} este restricționat!")

           
factory = ResursaFactory()


pret = float(input("Introduceti pretul: "))
carte = ResursaDecorator(factory.creare_resursa("carte"), pret)
procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
carte_cu_reducere = CodUnicDecorator(ReducereDecorator(carte, procentaj_reducere))
carte_cu_reducere.afisare()

pret = float(input("Introduceti pretul: "))
film = ResursaDecorator(factory.creare_resursa("film"), pret)
procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
film_cu_reducere = CodUnicDecorator(ReducereDecorator(film, procentaj_reducere))
film_cu_reducere.afisare()

pret = float(input("Introduceti pretul: "))
album = ResursaDecorator(factory.creare_resursa("muzica"), pret)
procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
album_cu_reducere = CodUnicDecorator(ReducereDecorator(album, procentaj_reducere))
album_cu_reducere.afisare()

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





# Pentru a proteja resursele si pentru a impiedica persoanele neautorizate sa 
# acceseze anumite produse, putem crea un proxy
# care sa verifice autorizarea inainte de a permite accesul la resurse.

# In continuare, voi crea un proxy pentru resursele "Carte", "Film" si
# "Muzica" care vor verifica daca utilizatorul care doreste sa cumpere un produs 
# este autorizat sau nu. In cazul in care utilizatorul este autorizat, acesta poate cumpara produsul.
# In caz contrar, utilizatorul va primi un mesaj de eroare.

# In exemplul de mai sus, clasa ProxyResursa va primi o instanță a clasei Resursa și o listă de utilizatori 
# autorizați. Apoi, metoda afisare a proxy-ului va verifica dacă utilizatorul curent se află în lista utilizatorilor 
# autorizați și, în funcție de aceasta, va permite sau va restricționa accesul la resursa.

# Pentru a utiliza acest proxy pentru resursele "Carte", "Film" și "Muzica", vom crea instanțe ale claselor,
# iar apoi vom aplica decoratorii și proxy-ul, în ordinea următoare: