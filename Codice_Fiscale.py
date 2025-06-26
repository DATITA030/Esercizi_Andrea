# https://it.wikipedia.org/wiki/Codice_fiscale per capire cosa va messo
#prende cognome e prime 3 consonanti  [3]  3
# TODO formattare la stringa per togliere le lettere accentate
#nome prime 3 consonanti   [3]   6
#anno ultime 2 cifre [2]   8
#mese con il dizionario per il CF [1] 9
#giorno di nascita 2 cifre [2] aggiungi uno 0 davanti .add  se <10 per le donne +40  (capiscono se sei omo o donna)
#comune o stato di nascita 1 lettera e 3 numeri [4]  stato estero Z+ codice (dizionario)
#Carattere di controllo..... e qua la paura imperversa
#TODO controllare date possibili e accettabili es.31 febbraio, numeri negativi o numeri troppo lunghi



def separa_vocali_consonanti(parola):
    consonanti=[]
    vocali=[]
    tupl_vocali = ("A", "E", "I", "O", "U")

    for lettera in parola:
        if lettera in tupl_vocali:
            vocali.append(lettera)

        else:
            consonanti.append(lettera)

    return consonanti, vocali

def separa_caratteri_dispari_e_pari(parola):
    caratteri_dispari=[]
    caratteri_pari=[]
    #in realtà non serve avere 2 variabili separate, ne basta una.
    somma_pari=0
    somma_dispari=0

    for i, lettera in enumerate(parola):
        if i %2 ==0:
            #caratteri_dispari+=caratteri_dispari.append(parola)
            somma_dispari += valori_dispari.get(lettera)

        else:
            #caratteri_pari+= caratteri_pari.append(lettera)
            if 65 <= ord(lettera) <= 90:
                somma_pari +=ord(lettera) - 65
            else:
                somma_pari+= int(lettera)

    temp_somma=somma_pari+somma_dispari
    terminator= temp_somma %26
    return terminator




"""
def check_dizionario(dict, key):
    #trasformo tutte le chiavi in una lista
    dict_key_list=list(dict.key())
    if key in dict_key_list:
    return dict.get(key)
    else:
        return False
    """





vocali = ("A", "E", "I", "O", "U")
"""consonanti = ('B', 'C', 'D', 'F', 'G', 'H', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'Z')

alf_inglese=("J","K","W","X","Y") #mi servono per carattere terminatore e per aggiunta se nome cognome solo 2 chr."""
mese_dizionario = {
    "1": "A", "01": "A", "gennaio": "A",
    "2": "B", "02": "B", "febbraio": "B",
    "3": "C", "03": "C", "marzo": "C",
    "4": "D", "04": "D", "aprile": "D",
    "5": "E", "05": "E", "maggio": "E",
    "6": "H", "06": "H", "giugno": "H",
    "7": "L", "07": "L", "luglio": "L",
    "8": "M", "08": "M", "agosto": "M",
    "9": "P", "09": "P", "settembre": "P",
     "10": "R", "ottobre": "R",
     "11": "S", "novembre": "S",
     "12": "T", "dicembre": "T"}

comuni_dizionario={
    "biella": "A859",
    "milano": "F205",
    "magenta": "E801",
    "bustoarsizio": "B300",
    "ecuador": "Z605"
}
valori_dispari = {
    "0": 1,  "1": 0,  "2": 5,  "3": 7,  "4": 9,  "5": 13, "6": 15, "7": 17, "8": 19, "9": 21,
    "A": 1,  "B": 0,  "C": 5,  "D": 7,  "E": 9,  "F": 13, "G": 15, "H": 17, "I": 19, "J": 21,
    "K": 2,  "L": 4,  "M": 18, "N": 20, "O": 11, "P": 3,  "Q": 6,  "R": 8,  "S": 12, "T": 14,
    "U": 16, "V": 10, "W": 22, "X": 25, "Y": 24, "Z": 23
}
#ho fatto anche pari, ma non ci serve
valori_pari = {
    '0': 0,  '1': 1,  '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6,  '7': 7,  '8': 8,  '9': 9,
    'A': 0,  'B': 1,  'C': 2,  'D': 3,  'E': 4,  'F': 5,  'G': 6,  'H': 7,  'I': 8,  'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}
conversione_resto = {
    0: 'A',  1: 'B',  2: 'C',  3: 'D',  4: 'E',  5: 'F',
    6: 'G',  7: 'H',  8: 'I',  9: 'J', 10: 'K', 11: 'L',
   12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
   18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
   24: 'Y', 25: 'Z'
}

cognome=input("Inserisci il tuo Cognome: ").upper().strip().replace(" ","")
#print("DEBUG",cognome)

nome=input("Inserisci il tuo Nome: ").upper().strip().replace(" ","")
#invoco la funzione

lista_consonanti , lista_vocali =separa_vocali_consonanti(cognome)
#print("DEBUG",lista_consonanti,lista_vocali)
#print(lista_consonanti)

#creo una lista che contiene tutte le consonanti, tutte le vocali e 3X

temp_cf=lista_consonanti + lista_vocali +["X","X","X"]
cf=temp_cf[0]+temp_cf[1]+temp_cf[2]

#Nome
lista_consonanti, lista_vocali=separa_vocali_consonanti(nome)

#cf_nome=temp_cf[0]+temp_cf[1]+temp_cf[2]

if len(lista_consonanti)>=4:
    cf+=lista_consonanti[0]+lista_consonanti[1]+lista_consonanti[2]
else:
    temp_cf = lista_consonanti + lista_vocali + ["X", "X", "X"]
    cf+=temp_cf[0] + temp_cf[1] + temp_cf[2]



year=input("in che anno sei nato?: ").strip().replace(" ","")
#uso isdigit per vedere se è numero
#se l'anno inserito ha meno di 2 caratteri aggiungiamo 00
if year.isdigit() ==False or len(year)<2:
    cf+="00"
else:
    cf+= year[-2:]



mese=input("Inserisci il tuo mese di nascita: ").lower().strip().replace(" ","")
#controllo se il mese inserito corrisponde a una delle chiavi del dizionario
#trasformo tutte le chiavi in una lista
dizionario_chiave_lista=list(mese_dizionario.keys())
if mese in dizionario_chiave_lista:
    cf+= mese_dizionario.get(mese)
else:
    cf += "X"


nascita=input("In che giorno sei nato?:").strip().replace(" ","")
if nascita.isdigit():
    nascita=int(nascita)
    if nascita<1 or nascita>31:
        nascita=00
else:
    nascita=00

sesso=input("Quale è il tuo sesso(alla nascita eh, non stiamo a usare dovizia di particolari qui)?: M/F? ").capitalize().strip().replace(" ","")
#controllare il primo carattere stringa sex per verificare se M o F
if sesso[0]=="M":
    cf += f"{nascita:02d}"  #STRING FORMATTING, FORMATTAZIONE NUMERICA CON ZERI INIZIALI
elif sesso[0]=="F":
    cf += f"{nascita +40:02d}"
else:
    cf += "00"


comune= input("in quale comune o stato estero sei nato?:").lower().strip().replace(" ","")
dizionario_chiave_cap=list(comuni_dizionario.keys())
if comune in dizionario_chiave_cap:
    cf+=comuni_dizionario.get(comune)
else:
    cf+= "X000"


terminator=separa_caratteri_dispari_e_pari(cf)
print(terminator)

cf+= chr(terminator+65)

print(cf)

"""check_comune=check_dizionario(comuni_dizionario, comune)
if check_comune:
    cf+= check_city
else:
    cf+="X000" """
"""dizionario_chiave_dispari= list(valori_dispari.keys())
for cf in dizionario_chiave_dispari:
    if cf in dizionario_chiave_dispari:"""


