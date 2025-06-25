"""richiesta all'utente l'iniziale del nome, il giorno e mese e genero un nome  """
#inserisco iniziale
#inserisco giorno
#inserisco mese
#tre liste
#dizionario per convertire lettere e numeri
#scorro nelle liste
#voillà il nome


nome=input("Inserisci il tuo nome: ").lower().strip()
iniziale=nome[0]
print(iniziale)

giorno=int(input("inserisci il tuo giorno di nascita: "))

mese=int(input("Inserisci il tuo mese di nascita: "))
#ora è una tupla
Lista_nomi=("Aerion","Baelgor","Cyneron","Dravok","Elandor","Faelir","Goramir","Helvorn","Itharos","Jandrel","Kaelric","Loramir","Myrrin","Nerion","Orvak","Pyrren","Quelvar","Rivenor","Sylthar","Thalior","Umbrek","Vaelor" ,"Wynskar","Xarion" ,"Ysilven" ,"Zarvek")
#ora è una tupla
lista_aggettivo=("Antico", "Oscuro", "Sacro", "Selvaggio", "Etereo", "Mistico", "Celestiale", "Tenebroso", "Fiammeggiante", "Glaciale", "Incantato", "Perduto", "Maledetto", "Benedetto", "Primordiale", "Dorato", "Sanguinoso", "Divino", "Lunare", "Solare", "Abissale", "Silenzioso", "Vorticoso", "Spettrale", "Maestoso", "Arcano", "Venerato", "Sussurrante", "Dimenticato", "Bruciante", "Implacabile")
#ora è una tupla
lista_titolo=("Custode", "Evocatore", "Stregone", "Profeta", "Veggente", "Signore", "Guardiano", "Errante", "Araldo", "Druido", "Campione", "Ombra")

lettere_numeri = {
    "a": 1,  "b": 2,  "c": 3,  "d": 4,  "e": 5,
    "f": 6,  "g": 7,  "h": 8,  "i": 9,  "j": 10,
    "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
    "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
    "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
    "z": 26
}

indice_nome = lettere_numeri[iniziale] - 1
nome = Lista_nomi[indice_nome]

aggettivo=lista_aggettivo[giorno-1]
titolo=lista_titolo[mese-1]







if indice_nome== 0 and giorno==3 and mese==7:

    print(f"ANNA SECONDO ME DORME!\nScherzo il tuo nome è: {nome} {titolo} {aggettivo}, giuro, pensavo peggio!")
elif indice_nome== 18 and giorno==26 and mese==5:
    print("Sabrina Sei Mitica!")
else:
    print(f"il tuo nome è :{nome} {titolo} {aggettivo}, ammazza che figo!")



#VERSIONE CON MATTEO e SABRINA
"""
titoli_mensili = {
    "Gennaio": "Decollo Invernale",
    "Febbraio": "Rotta Verso l’Orizzonte",
    "Marzo": "Turbulenze di Primavera",
    "Aprile": "Manovre di Rinnovamento",
    "Maggio": "Quota Maggiore",
    "Giugno": "Virata Estiva",
    "Luglio": "Cieli Sereni",
    "Agosto": "Volo d’Altura",
    "Settembre": "Atterraggio Morbido",
    "Ottobre": "Controllo Rotta",
    "Novembre": "Avviso di Turbolenza",
    "Dicembre": "Check List"
}
aggettivi_giornalieri = {
    1: "aerodinamico",  2: "slanciato",     3: "scattante",    4: "vigile",
    5: "pronto",        6: "preciso",       7: "elevato",      8: "lucido",
    9: "reattivo",     10: "radarizzato",  11: "coordinato", 12: "sollevato",
   13: "lineare",      14: "strategico",   15: "navigato",   16: "rapido",
   17: "sicuro",       18: "flessibile",   19: "orientato",  20: "controllato",
   21: "calibrato",    22: "agile",        23: "impeccabile",24: "preparato",
   25: "reattivo",     26: "dominante",    27: "persistente",28: "equilibrato",
   29: "veloce",       30: "disciplinato", 31: "concentrato"}
mese_nascita= input("in quale mese sei nato?").capitalize().strip()
giorno_nascita= int(input("in quale giorno sei nato: ").strip())

print(f"il tuo nuovo nome è: {titoli_mensili[mese_nascita]} {aggettivi_giornalieri[giorno_nascita]}")
"""