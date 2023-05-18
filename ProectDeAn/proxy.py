from factory import Resursa

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
            print("4. Modificare resursă")
            print("5. Exit")
            optiune = int(input("Introduceți opțiunea dorită: "))
            if optiune == 1:
                print(self._resursa.afisare())
            elif optiune == 2:
                print(self._resursa.afisare())
            elif optiune == 3:
                print(self._resursa.afisare())
            elif optiune == 4:
                while True:
                    print("Alegeți ce doriți să modificați:")
                    print("1. Titlu")
                    print("2. Autor")
                    print("3. Înapoi")
                    optiune_modificare = int(input("Introduceți opțiunea dorită: "))
                    if optiune_modificare == 1:
                        nou_titlu = input("Introduceți noul titlu: ")
                        self._resursa.set_titlu(nou_titlu)
                        print("Titlul a fost modificat cu succes!")
                    elif optiune_modificare == 2:
                        nou_autor = input("Introduceți noul autor: ")
                        self._resursa.set_autor(nou_autor)
                        print("Autorul a fost modificat cu succes!")
                    elif optiune_modificare == 3:
                        break
                    else:
                        print("Opțiune invalidă!")
            elif optiune == 5:
                print("Programul se încheie. La revedere!")
                return  # Ieșim din metoda afisare() pentru a încheia programul
            else:
                print("Opțiune invalidă!")
        else:
            print(f"Accesul pentru {utilizator_curent} este restricționat!")
