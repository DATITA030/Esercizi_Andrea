"""Collezioni dati = array
list   -  collezione ordinata e modificabile
tuble  -  collezione ordinata, ma non modificabile
set    -  collezione non ordinata e non indicizzata con elementi unici
dict   -  collezione di coppie chiave-valore modificabile e ordinata"""



#LISTA, list []
"""utilizzate per memorizzare più valori in un'unica variabile. 
Ordinate - gli elementi hanno un indice che parte da 0
Modificabili - gli elementi possono essere aggiunti, rimossi o duplicati
Dublicabili - consentono valori duplicati"""

frutti=["mela", "banana", "ciliegia","mela"]
print(frutti)
print("\n=========\n")
#metodi delle liste
#AGGIUNGERE UN ELEMENTO
frutti.append("arancia",)
print(frutti)
print("\n============\n")
#MODIFICARE UN ELEMENTO
frutti[1]="kiwi"
print(frutti)
frutti[0]="kiwo"
print(frutti)
print("\n============\n")
#RIMUOVERE UN ELEMENTO
frutti.remove("kiwi")
print(frutti)
print("\n=======\n")

fruits=["mela", "banana", "ciliegia","mela","mela","ananas","passion","albicocca","mela","mela"]
#fruits.append("mela")
#print(fruits)     #Esercizio trabocchetto di Sabrina
for fruit in fruits:
    print(fruits)
    print("sto visitando l'elemento", fruit)
    if fruit == "mela":
        print("questa mela è una ",fruit)
        fruits.remove(fruit) #il comando rimuove la prima mela che trova nella lista
print(fruits)

#fruits.sort() #li mette in ordine alfabetico
#print(fruits)


print("\n======\n")


frut= ("mela","banana","ciliegia","mela")
print(frut)
print(frut[1])
"""print(help(list))"""

print("\n======\n")

#TUPLE tuple()
"""le tuple simili alle liste, ma sono IMMUTABILI : una volta create, il loro contenuto non può essere modificato.
si riconoscono perchè usano le () e non le []
ORDINATE - elementi hanno un indice zero
CONSENTONO DUPLICATI - lo stesso valore può ripetersi più volte"""

fruits =("mela", "pera","banana")
print(fruits)
print(fruits[2])

print("\n======\n")

"""INSIEMI - SET
colezioni non ordinate e non indicizzate

NON INDICIZZATI
MODIFICABILI
NON ORDINATI"""

fruits={"mela", "fragola", "pompelmo", "mela","banana", "fragola"} #vengono ridotti ad una sola occorrenza
print(fruits)
print("\n======\n")

#METODI DEI SET
#rimuove i duplicati e mantiene sempre l'ordine

numeris={1,2,3,4,5,4}
print(numeris)
numeris.add(7)
print(numeris)
numeris.remove(3)
print(numeris)
print("\n======\n")

"""i set sono molto utili per operazioni matematici come UNIONE, INTERSEZIONE e DIFFERENZA"""

A={1,3,4}
B={2,4,5}
#unione di due insiemi
print(f"insieme A",A)
print(f"insieme B",B)
print(f"print di A.union (B)",A.union(B))
print(f"intersezione di A e B", A.intersection(B)) #il risultato è sempre un SET
print(f"differenza di A MENO B",A.difference(B))
print(f"differenza di B MENO A", B.difference(A))

print("\n======\n")

"""DIZIONARI - DICT{}
I dizionari memorizzano dati sotto forma di coppie key-value (chiave-valore)
ORDINATI - a partire da Python 3.7 (prima non erano ordinati)
INDICIZZATI PER CHIAVE - gli elementi sono accessibili tramite KEY
MODIFICABILI - le coppie possono essere aggiunte o rimosse
CHIAVI UNICHE - le chiavi di un DICT non possono essere duplicate"""

persona={"nome":"Andrea",
         "età":26,
         "città":"Milano"}

#METODI DEI DIZIONARI
print(persona)
print(persona["nome"])
persona["professione"]= "Data Engineer" #questa chiave non esiste e quindi si aggiunge
print(persona)

persona["età"]=27
print(persona)
print("\n======\n")

persona.pop("città")
print(persona)

print("\n CICLI FOR E DIZIONARI\n")

"""CICLI FOR E DIZIONARI"""

for chiave, valore in persona.items():
    print(f"{chiave}-> {valore}")

print("\n1======\n")

for chiave in persona.keys():
    print(chiave)

print("\n2======\n")

for valore in persona.values():
    print(valore)