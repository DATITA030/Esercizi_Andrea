from user import User

if __name__=="__main__":
    user1 = User("Marco",30,"Aurelio","Polibio")
    print(user1.say_hello())
    #libero accesso agli attributi pubblici
    print(f"gli attributi pubblici dell'oggetto user1 sono {user1.name} e {user1.age} ")
    #ho accesso all'attributo protetto(che non appare subito in lista) ma ho un warning
    print(f"l'attributo protetto dell'oggetto user1 è {user1._surname}")
    #non ho accesso all'attributo privato(nascosto)... quindi il codice genera un errore
    #print(f"l'attributo privato dell'oggetto user1 è {user1.__address}")

    #aggirando il NAME MANGLING è possibile accedere agli attributi privati
    print(f"Provo a visualizzare il valore di un attributo privato: {user1._User__address}")

    user1._User__address ="Milano"
    print(f"modificata {user1._User__address}")

    print(user1._drive())
    #verifico accesso metodo privato
    print(f"{user1._drive()}  va scritto tra parentesi graffa --> }}")

    #accedo al valore dell'attributo privato __address tramite metodo get (GETTER)
    print(f"Il valore di __address è {user1.get_address()}")
    # modifico il valore dell'attributo privato __address tramite metodo set (SETTER)
    user1.set_addres("Firenze")
    print(f"Il nuovo valore di __address è {user1.get_address()}")

    #accesso all'attributo PRIVATO fiscal code con il getter @property
    print(f"Il codice fiscale di {user1.name} è {user1.fiscal_code}")  #l'auto completamento me lo segna con una p viola perchè pycharm riconosce il property
