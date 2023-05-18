# Lista utilizatorilor autorizați
from factory import ResursaFactory, ResursaDecorator, CodUnicDecorator, ReducereDecorator, Observer
from proxy import ProxyResursa


class creeaza_carte():
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
    # Crearea obiectului de tip Observer
    observer = Observer()
    # Înregistrarea observatorului la obiectul de tip CartePrototype
    carte.register_observer(observer)

utilizatori_autorizati = ["user1", "user2", "user3"]

# Crearea instanțelor de proxy pentru fiecare dintre cele trei resurse
carte_proxy = ProxyResursa(creeaza_carte().carte,creeaza_carte().carte_cu_reducere, utilizatori_autorizati)
# film_proxy = ProxyResursa(film,film_cu_reducere, utilizatori_autorizati)
# album_proxy = ProxyResursa(album,album_cu_reducere, utilizatori_autorizati)

# Utilizarea resurselor prin intermediul proxy-ului
carte_proxy.afisare()
# film_proxy.afisare()
# album_proxy.afisare()
