from command import ModificaTitluCarteCommand, \
    ModificaRegizorFilmCommand, ModificaTitluMuzicaCommand, ModificaArtistMuzicaCommand, \
    ModificaTitluFilmCommand, ModificaAutorCarteCommand, ValidareChain

from factory import Resursa, ResursaFactory, ResursaDecorator, CodUnicDecorator, ReducereDecorator, Observer, Carte, Film, Muzica


def creeaza_carte():
    factory = ResursaFactory()
    carte = factory.creare_resursa("carte")

    pret = float(input("Introduceti pretul: "))
    carte_pret = ResursaDecorator(carte, pret)
    carte.set_pret(pret)

    procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
    carte_cu_reducere = CodUnicDecorator(ReducereDecorator(carte_pret, procentaj_reducere))
    carte.set_procentaj_reducere(procentaj_reducere)
    carte.set_cod_unic(carte_cu_reducere.cod_unic)

    # Afisarea se face acum o singură dată în interiorul constructorilor decoratorilor
    carte_cu_reducere.afisare()

    validare_chain_carte = ValidareChain()
    validare_chain_carte.valideaza_carte(carte)

    observer = Observer()
    carte.register_observer(observer)

    return carte


def creeaza_film():
    factory = ResursaFactory()
    film = factory.creare_resursa("film")
    pret = float(input("Introduceti pretul: "))
    film_pret = ResursaDecorator(film, pret)
    film.set_pret(pret)

    procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
    film_cu_reducere = CodUnicDecorator(ReducereDecorator(film_pret, procentaj_reducere))
    film.set_procentaj_reducere(procentaj_reducere)  # Salvăm procentajul de reducere în obiectul carte
    film.set_cod_unic(film_cu_reducere.cod_unic)  # Transmit codul unic în metoda set_cod_unic()

    film_cu_reducere.afisare()
    # Creăm lanțul de responsabilitate pentru film
    validare_chain_film = ValidareChain()
    # Validează filmul folosind lanțul de responsabilitate pentru film
    validare_chain_film.valideaza_film(film)
    # Crearea obiectului de tip Observer
    observer = Observer()
    film.register_observer(observer)
    return film


def creeaza_album():
    factory = ResursaFactory()
    album = factory.creare_resursa("muzica")
    pret = float(input("Introduceti pretul: "))
    album_pret = ResursaDecorator(album, pret)
    album.set_pret(pret)

    procentaj_reducere = float(input("Introduceti procentajul de reducere: "))
    album_cu_reducere = CodUnicDecorator(ReducereDecorator(album_pret, procentaj_reducere))

    album.set_procentaj_reducere(procentaj_reducere)  # Salvăm procentajul de reducere în obiectul carte
    album.set_cod_unic(album_cu_reducere.cod_unic)  # Transmit codul unic în metoda set_cod_unic()

    album_cu_reducere.afisare()
    # Creăm lanțul de responsabilitate pentru film
    validare_chain_film = ValidareChain()
    # Validează filmul folosind lanțul de responsabilitate pentru film
    validare_chain_film.valideaza_album(album)
    # Crearea obiectului de tip Observer
    observer = Observer()
    album.register_observer(observer)
    return album



utilizatori_autorizati = ["user1", "user2", "user3"]


class ProxyResursa(Resursa):
    def __init__(self, resursa, resursa_cu_reducere, utilizatori_autorizati):
        super().__init__()
        self.resursa = resursa
        self._resursa_cu_reducere = resursa_cu_reducere
        self._utilizatori_autorizati = utilizatori_autorizati
        self._obiecte_create = []  # Inițializați lista pentru a stoca obiectele create

    def afisare(self):
        utilizator_curent = input("Introduceți numele dvs.: ")
        if utilizator_curent in self._utilizatori_autorizati:
            while True:
                print("Alegeți o resursă:")
                print("1. Crează Produsele")
                print("2. Afișare Produse")
                print("3. Modificare resursă")
                print("4. Exit")
                optiune = int(input("Introduceți opțiunea dorită: "))
                if optiune == 1:
                    while True:
                        print()
                        print("Alegeți o resursă pentru a o crea:")
                        print("1. Carte")
                        print("2. Film")
                        print("3. Album")
                        print("4. Înapoi")
                        optiune_creare = int(input("Introduceți opțiunea dorită: "))
                        if optiune_creare == 1:
                            self._obiect_creat = creeaza_carte()
                            self._obiecte_create.append(self._obiect_creat)  # Salvăm obiectul creat
                        if optiune_creare == 2:
                            self._obiect_creat = creeaza_film()
                            self._obiecte_create.append(self._obiect_creat)
                        if optiune_creare == 3:
                            self._obiect_creat = creeaza_album()
                            self._obiecte_create.append(self._obiect_creat)
                        elif optiune_creare == 4:
                            break
                elif optiune == 2:
                    while True:
                        print()
                        print("Alegeți o resursă pentru a o vizualiza:")
                        print("1. Carte")
                        print("2. Film")
                        print("3. Album")
                        print("4. Înapoi")
                        optiune_afisare = int(input("Introduceți opțiunea dorită: "))
                        print()
                        if optiune_afisare == 1:
                            if self._obiecte_create:
                                carte_creat = False
                                for obiect in self._obiecte_create:
                                    if isinstance(obiect, Carte):
                                        obiect.afisare()
                                        carte_creat = True
                                        if isinstance(obiect, CodUnicDecorator):
                                            obiect.afisare()
                                if not carte_creat:
                                    print('Nu a fost creat niciun obiect de tip "Carte" încă.')
                            else:
                                print("Nu a fost creat niciun obiect încă.")
                        elif optiune_afisare == 2:
                            if self._obiecte_create:
                                film_creat = False
                                for obiect in self._obiecte_create:
                                    if isinstance(obiect, Film):
                                        obiect.afisare()
                                        film_creat = True
                                        if isinstance(obiect, CodUnicDecorator):
                                            obiect.afisare()
                                if not film_creat:
                                    print("Nu a fost creat niciun obiect de tip film încă")
                            else:
                                print("Nu a fost creat niciun obiect încă.")
                        elif optiune_afisare == 3:
                            if self._obiecte_create:
                                album_creat = False
                                for obiect in self._obiecte_create:
                                    if isinstance(obiect, Muzica):
                                        obiect.afisare()
                                        album_creat = True
                                        if isinstance(obiect, CodUnicDecorator):
                                            obiect.afisare()
                                if not album_creat:
                                    print('Nu a fost creat niciun obiect de tip album încă')
                            else:
                                print("Nu a fost creat niciun obiect încă.")
                        elif optiune_afisare == 4:
                            break
                        else:
                            print("Opțiune invalidă!")
                elif optiune == 3:
                    while True:
                        print()
                        print("Alegeți o resursă pentru a o modifica:")
                        print("1. Carte")
                        print("2. Film")
                        print("3. Album")
                        print("4. Înapoi")
                        optiune_resursa = int(input("Introduceți opțiunea dorită: "))
                        print()
                        if optiune_resursa == 1:
                            while True:
                                print()
                                print("Alegeți ce doriți să modificați:")
                                print("1. Titlu")
                                print("2. Autor")
                                print("3. Înapoi")
                                optiune_modificare = int(input("Introduceți opțiunea dorită: "))
                                if optiune_modificare == 1:
                                    # Modificare titlu carte
                                    if self._obiecte_create:
                                        carte_creat = False
                                        for obiect in self._obiecte_create:
                                            if isinstance(obiect, Carte):
                                                obiect.afisare()
                                                carte_creat = True
                                        if carte_creat:
                                            titlu_obiect = input(
                                                "Introduceți titlul cărții pe care doriți să o modificați: ")
                                            for obiect in self._obiecte_create:
                                                if isinstance(obiect, Carte) and obiect.titlu == titlu_obiect:
                                                    titlu_nou = input("Introduceți noul titlu al cărții: ")
                                                    print()
                                                    if titlu_nou.strip() != "":
                                                        command = ModificaTitluCarteCommand(obiect, titlu_nou)
                                                        command.execute()
                                                    break
                                            else:
                                                print("Nu există o carte cu titlul specificat.")
                                        else:
                                            print("Nu a fost creat niciun obiect de tip 'Carte' încă.")
                                    else:
                                        print("Nu a fost creat niciun obiect încă.")
                                elif optiune_modificare == 2:
                                    if self._obiecte_create:
                                        carte_creat = False
                                        for obiect in self._obiecte_create:
                                            if isinstance(obiect, Carte):
                                                obiect.afisare()
                                                carte_creat = True
                                        if carte_creat:
                                            titlu_obiect = input(
                                                "Introduceți titlul cărții pe care doriți să îi modificați autorul: ")
                                            for obiect in self._obiecte_create:
                                                if isinstance(obiect, Carte) and obiect.titlu == titlu_obiect:
                                                    nume_nou = input("Introduceți noul nume al autorului cărții: ")
                                                    prenume_nou = input(
                                                        "Introduceți noul prenume al autorului cărții: ")
                                                    nationalitate_nou = input(
                                                        "Introduceți noua naționalitate a autorului cărții: ")
                                                    an_nastere_nou = input(
                                                        "Introduceți noul an de naștere al autorului cărții: ")

                                                    nume_vechi = obiect.autor.nume if nume_nou.strip() == "" else nume_nou
                                                    prenume_vechi = obiect.autor.prenume if prenume_nou.strip() == "" else prenume_nou
                                                    nationalitate_veche = obiect.autor.nationalitate if nationalitate_nou.strip() == "" else nationalitate_nou
                                                    an_nastere_vechi = obiect.autor.an_nastere if an_nastere_nou.strip() == "" else an_nastere_nou

                                                    autor_nou = f"{nume_vechi} {prenume_vechi} ({nationalitate_veche}, {an_nastere_vechi})"
                                                    print()
                                                    if any(val.strip() != "" for val in
                                                           [nume_nou, prenume_nou, nationalitate_nou, an_nastere_nou]):
                                                        command = ModificaAutorCarteCommand(obiect, autor_nou)
                                                        command.execute()
                                                    break
                                            else:
                                                print("Nu există o carte cu autorul specificat.")
                                        else:
                                            print("Nu a fost creat niciun obiect de tip 'Carte' încă.")
                                    else:
                                        print("Nu a fost creat niciun obiect încă.")
                                elif optiune_modificare == 3:
                                    break
                                else:
                                    print("Opțiune invalidă!")
                        elif optiune_resursa == 2:
                            while True:
                                print("Alegeți ce doriți să modificați:")
                                print("1. Titlu")
                                print("2. Regizor")
                                print("3. Înapoi")
                                optiune_modificare = int(input("Introduceți opțiunea dorită: "))
                                if optiune_modificare == 1:
                                    if self._obiecte_create:
                                        film_creat = False
                                        for obiect in self._obiecte_create:
                                            if isinstance(obiect, Film):
                                                obiect.afisare()
                                                film_creat = True
                                        if film_creat:
                                            titlu_obiect = input(
                                                "Introduceți titlul filmului pe care doriți să îl modificați: ")
                                            for obiect in self._obiecte_create:
                                                if isinstance(obiect, Film) and obiect.titlu == titlu_obiect:
                                                    titlu_nou = input("Introduceți noul titlu al filmului: ")
                                                    print()
                                                    if titlu_nou.strip() != "":
                                                        command = ModificaTitluFilmCommand(obiect, titlu_nou)
                                                        command.execute()
                                                    break
                                            else:
                                                print("Nu există niciun film cu titlul specificat.")
                                        else:
                                            print("Nu a fost creat niciun obiect de tip 'Film' încă.")
                                    else:
                                        print("Nu a fost creat niciun obiect încă.")
                                elif optiune_modificare == 2:
                                    if self._obiecte_create:
                                        film_creat = False
                                        for obiect in self._obiecte_create:
                                            if isinstance(obiect, Film):
                                                obiect.afisare()
                                                film_creat = True
                                        if film_creat:
                                            titlu_obiect = input(
                                                "Introduceți titlul filmului pe care doriți să îi modificați autorul: ")
                                            for obiect in self._obiecte_create:
                                                if isinstance(obiect, Film) and obiect.titlu == titlu_obiect:
                                                    nume_nou = input("Introduceți noul nume al regizorului filmului: ")
                                                    prenume_nou = input(
                                                        "Introduceți noul prenume al regizorului filmului: ")
                                                    nationalitate_nou = input(
                                                        "Introduceți noua naționalitate a regizorului filmului: ")
                                                    an_nastere_nou = input(
                                                        "Introduceți noul an de naștere al regizorului filmului: ")

                                                    nume_vechi = obiect.autor.nume if nume_nou.strip() == "" else nume_nou
                                                    prenume_vechi = obiect.autor.prenume if prenume_nou.strip() == "" else prenume_nou
                                                    nationalitate_veche = obiect.autor.nationalitate if nationalitate_nou.strip() == "" else nationalitate_nou
                                                    an_nastere_vechi = obiect.autor.an_nastere if an_nastere_nou.strip() == "" else an_nastere_nou

                                                    regizor_nou = f"{nume_vechi} {prenume_vechi} ({nationalitate_veche}, {an_nastere_vechi})"
                                                    print()
                                                    if any(val.strip() != "" for val in
                                                           [nume_nou, prenume_nou, nationalitate_nou, an_nastere_nou]):
                                                        command = ModificaRegizorFilmCommand(obiect, regizor_nou)
                                                        command.execute()
                                                    break
                                            else:
                                                print("Nu există o carte cu autorul specificat.")
                                        else:
                                            print("Nu a fost creat niciun obiect de tip 'Carte' încă.")
                                    else:
                                        print("Nu a fost creat niciun obiect încă.")

                                elif optiune_modificare == 3:
                                    break
                                else:
                                    print("Opțiune invalidă!")
                        elif optiune_resursa == 3:
                            while True:
                                print("Alegeți ce doriți să modificați:")
                                print("1. Titlu")
                                print("2. Artistul")
                                print("3. Înapoi")
                                optiune_modificare = int(input("Introduceți opțiunea dorită: "))
                                if optiune_modificare == 1:
                                    if self._obiecte_create:
                                        album_creat = False
                                        for obiect in self._obiecte_create:
                                            if isinstance(obiect, Muzica):
                                                obiect.afisare()
                                                album_creat = True
                                        if album_creat:
                                            titlu_obiect = input(
                                                "Introduceți titlul Albumului muzical pe care doriți să îl modificați: ")
                                            for obiect in self._obiecte_create:
                                                if isinstance(obiect, Muzica) and obiect.titlu == titlu_obiect:
                                                    titlu_nou = input("Introduceți noul titlu al albumului: ")
                                                    print()
                                                    if titlu_nou.strip() != "":
                                                        command = ModificaTitluMuzicaCommand(obiect, titlu_nou)
                                                        command.execute()
                                                    break
                                            else:
                                                print("Nu există niciun album cu titlul specificat.")
                                        else:
                                            print("Nu a fost creat niciun obiect de tip 'Album' încă.")
                                    else:
                                        print("Nu a fost creat niciun obiect încă.")
                                elif optiune_modificare == 2:
                                    if self._obiecte_create:
                                        album_creat = False
                                        for obiect in self._obiecte_create:
                                            if isinstance(obiect, Muzica):
                                                obiect.afisare()
                                                album_creat = True
                                        if album_creat:
                                            titlu_obiect = input(
                                                "Introduceți titlul albumului pe care doriți să îi modificați artistul: ")
                                            for obiect in self._obiecte_create:
                                                if isinstance(obiect, Muzica) and obiect.titlu == titlu_obiect:
                                                    nume_nou = input("Introduceți noul nume al artistului al albumului: ")
                                                    prenume_nou = input(
                                                        "Introduceți noul prenume al artistului al albumului: ")
                                                    nationalitate_nou = input(
                                                        "Introduceți noua naționalitate a artistului al albumului: ")
                                                    an_nastere_nou = input(
                                                        "Introduceți noul an de naștere al artistului al albumului: ")

                                                    nume_vechi = obiect.autor.nume if nume_nou.strip() == "" else nume_nou
                                                    prenume_vechi = obiect.autor.prenume if prenume_nou.strip() == "" else prenume_nou
                                                    nationalitate_veche = obiect.autor.nationalitate if nationalitate_nou.strip() == "" else nationalitate_nou
                                                    an_nastere_vechi = obiect.autor.an_nastere if an_nastere_nou.strip() == "" else an_nastere_nou

                                                    artist_nou = f"{nume_vechi} {prenume_vechi} ({nationalitate_veche}, {an_nastere_vechi})"
                                                    print()
                                                    if any(val.strip() != "" for val in
                                                           [nume_nou, prenume_nou, nationalitate_nou, an_nastere_nou]):
                                                        command = ModificaArtistMuzicaCommand(obiect, artist_nou)
                                                        command.execute()
                                                    break
                                            else:
                                                print("Nu există o carte cu autorul specificat.")
                                        else:
                                            print("Nu a fost creat niciun obiect de tip 'Carte' încă.")
                                    else:
                                        print("Nu a fost creat niciun obiect încă.")
                                elif optiune_modificare == 3:
                                    break
                                else:
                                    print("Opțiune invalidă!")
                        elif optiune_resursa == 4:
                            break
                        else:
                            print("Opțiune invalidă!")
                elif optiune == 4:
                    print("Programul se încheie. La revedere!")
                    return  # Ieșim din metoda afisare() pentru a încheia programul
                else:
                    print("Opțiune invalidă!")

            print("Aplicația s-a încheiat.")


resursa = ResursaFactory()  # înlocuiți cu instanța reală a clasei Resursa

resursa_cu_reducere = CodUnicDecorator  # înlocuiți cu instanța reală a clasei ResursaDecorator

utilizatori_autorizati = ["user1", "user2", "user3"]
proxy_resursa = ProxyResursa(resursa, resursa_cu_reducere, utilizatori_autorizati)
proxy_resursa.afisare()




