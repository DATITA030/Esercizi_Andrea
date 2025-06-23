"""richiesta all'utente l'iniziale del nome, il giorno e mese e genero un nome  """
#inserisco iniziale
#inserisco giorno
#inserisco mese
#tre liste
#dizionario per convertire lettere e numeri
#scorro nelle liste
#voillà il nome


iniziale=input("Inserisci la tua iniziale: ").lower()

giorno=int(input("inserisci il tuo giorno di nascita: "))

mese=int(input("Inserisci il tuo mese di nascita: "))

Lista_nomi=["Aerion","Baelgor","Cyneron","Dravok","Elandor","Faelir","Goramir","Helvorn","Itharos","Jandrel","Kaelric","Loramir","Myrrin","Nerion","Orvak","Pyrren","Quelvar","Rivenor","Sylthar","Thalior","Umbrek","Vaelor" ,"Wynskar","Xarion" ,"Ysilven" ,"Zarvek"]

lista_aggettivo=["Antico", "Oscuro", "Sacro", "Selvaggio", "Etereo", "Mistico", "Celestiale", "Tenebroso", "Fiammeggiante", "Glaciale", "Incantato", "Perduto", "Maledetto", "Benedetto", "Primordiale", "Dorato", "Sanguinoso", "Divino", "Lunare", "Solare", "Abissale", "Silenzioso", "Vorticoso", "Spettrale", "Maestoso", "Arcano", "Venerato", "Sussurrante", "Dimenticato", "Bruciante", "Implacabile"]

lista_titolo=["Custode", "Evocatore", "Stregone", "Profeta", "Veggente", "Signore", "Guardiano", "Errante", "Araldo", "Druido", "Campione", "Ombra"]

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





#indice_nome=0
#print(indice_nome)

if indice_nome== 0 and giorno==3 and mese==7:

    print("ANNA SECONDO ME DORME!")
elif indice_nome== 18 and giorno==26 and mese==5:
    print("Sabrina Sei Mitica!")
else:
    print(f"il tuo nome è :{nome} {titolo} {aggettivo}, ammazza che figo!")



#print(help(str))
#Guardiano
"""numero=0
lettere=["a","b","c"]
for lettera in lettere:
    lettere.replace("lettera","numero"+1)
"""