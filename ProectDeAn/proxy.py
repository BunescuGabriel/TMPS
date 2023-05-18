from command import ModificaTitluCarteCommand, ModificaAutorCarteCommand, ModificaTitluFilmCommand, \
    ModificaRegizorFilmCommand, ModificaTitluMuzicaCommand, ModificaArtistMuzicaCommand
from factory import Resursa, ResursaDecorator, ResursaFactory, Observer, CodUnicDecorator, ReducereDecorator
from main import creeaza_carte


class ProxyResursa(Resursa):
    def __init__(self, resursa,resursa_cu_reducere,  utilizatori_autorizati):
        self._resursa = resursa
        self._resursa_cu_reducere = resursa_cu_reducere
        self._utilizatori_autorizati = utilizatori_autorizati

    def afisare(self):
        utilizator_curent = input("Introduceti numele dvs.: ")
        if utilizator_curent in self._utilizatori_autorizati:
            while True:
                print("Alegeți o resursă:")
                print("1. Creaza Produselor")
                print("2. Afisare Produselor")
                print("3. Modificare resursă")
                print("4. Exit")
                optiune = int(input("Introduceți opțiunea dorită: "))
                if optiune == 1:
                    while True:
                        print("Alegeți o resursă pentru a o crea:")
                        print("1. Carte")
                        print("2. Film")
                        print("3. Album")
                        print("4. Înapoi")
                        optiune_creare = int(input("Introduceți opțiunea dorită: "))
                        if optiune_creare == 1:
                            creeaza_carte()
                        elif optiune_afisare == 4:
                            break
                        else:
                            print("Opțiune invalidă!")


                elif optiune == 2:
                    while True:
                        print("Alegeți o resursă pentru a o vizualiza:")
                        print("1. Carte")
                        print("2. Film")
                        print("3. Album")
                        print("4. Înapoi")
                        optiune_afisare = int(input("Introduceți opțiunea dorită: "))
                        if optiune_afisare == 1:
                            self._resursa_cu_reducere.afisare()
                        elif optiune_afisare == 2:
                            self._resursa_cu_reducere.afisare()
                        elif optiune_afisare == 3:
                            self._resursa_cu_reducere.afisare()
                        elif optiune_afisare == 4:
                            break
                        else:
                            print("Opțiune invalidă!")
                elif optiune == 3:
                    while True:
                        print("Alegeți o resursă pentru a o modifica:")
                        print("1. Carte")
                        print("2. Film")
                        print("3. Album")
                        print("4. Înapoi")
                        optiune_resursa = int(input("Introduceți opțiunea dorită: "))
                        if optiune_resursa == 1:
                            while True:
                                print("Alegeți ce doriți să modificați:")
                                print("1. Titlu")
                                print("2. Autor")
                                print("3. Înapoi")
                                optiune_modificare = int(input("Introduceți opțiunea dorită: "))
                                if optiune_modificare == 1:
                                    titlu_nou = input("Introduceți noul titlu al cărții: ")
                                    comanda_modifica_titlu_carte = ModificaTitluCarteCommand(self._resursa, titlu_nou)
                                    comanda_modifica_titlu_carte.execute()
                                    print("Titlul cărții a fost modificat cu succes!")
                                    # Afisarea doar a titlului modificat
                                    print("Noul titlu al cărții este:", titlu_nou)

                                elif optiune_modificare == 2:
                                    nou_autor = input("Introduceți noul autor: ")
                                    comanda_modifica_autor_carte = ModificaAutorCarteCommand(self._resursa, nou_autor)
                                    comanda_modifica_autor_carte.execute()
                                    print("Autorul cărții a fost modificat cu succes!")
                                    # Afisarea doar a titlului modificat
                                    print("Noul titlu al cărții este:", nou_autor)
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
                                    titlu_nou = input("Introduceți noul titlu al filmului: ")
                                    comanda_modifica_titlu_filme = ModificaTitluFilmCommand(self._resursa, titlu_nou)
                                    comanda_modifica_titlu_filme.execute()
                                    print("Titlul filmului a fost modificat cu succes!")
                                    # Afisarea doar a titlului modificat
                                    print("Noul titlu al filmului este:", titlu_nou)

                                elif optiune_modificare == 2:
                                    regizor_nou = input("Introduceți noul regizor: ")
                                    comanda_modifica_regizor_film = ModificaRegizorFilmCommand(self._resursa, regizor_nou)
                                    comanda_modifica_regizor_film.execute()
                                    print("Autorul cărții a fost modificat cu succes!")
                                    # Afisarea doar a titlului modificat
                                    print("Noul titlu al cărții este:", regizor_nou)
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
                                    titlu_nou = input("Introduceți noul titlu al Albomului: ")
                                    comanda_modifica_titlu_albumului = ModificaTitluMuzicaCommand(self._resursa, titlu_nou)
                                    comanda_modifica_titlu_albumului.execute()
                                    print("Titlul Albomului a fost modificat cu succes!")
                                    # Afisarea doar a titlului modificat
                                    print("Noul titlu al Albomului este:", titlu_nou)

                                elif optiune_modificare == 2:
                                    artist_nou = input("Introduceți noul artist: ")
                                    comanda_modifica_artistul_albom = ModificaArtistMuzicaCommand(self._resursa, artist_nou)
                                    comanda_modifica_artistul_albom.execute()
                                    print("Artistul albumului a fost modificat cu succes!")
                                    # Afisarea doar a titlului modificat
                                    print("Noul Artist al albumului este:", artist_nou)
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




