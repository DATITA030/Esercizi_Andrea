#creare una simulazione di login
#creare una "struttura" (collezione) che simula un database in cui registrare 3 username e la password corrispondente
#chiedere all'utente di inserire lo username
#chiedere all'utente di inserire la password
#verificare che password e username siano corretti
#gestire errori con custom exception
#permettere all'utente di fare il login SOLO SE LE CREDENZIALI SIANO CORRETTE
class Errore_accesso(Exception):
    pass

def verifica(username, password):
    if username in user_list:  #for chiave in user_list......
        if user_list[username]==password:
            print("Accesso Consentito")
            print("Grazie Carlo per l'aiuto nel if della funzione")
            return True
    raise Errore_accesso




#Creo struttura... Dizionario 3 chiavi e 3 valori
user_list={"Mari_o":"1234",
           "Michela23":"forza",
           "Raffaele":"Avvolt010",
           "Paolo":"password"}

try:
    username = input("inserisci lo username") #chiedo all'utente uno username
    password=input("inserisci la password") #chiedo all'utente la password
    verifica(username, password)



except Errore_accesso as ex:
    print(f"Errore di accesso, non so che dirti{ex}")






