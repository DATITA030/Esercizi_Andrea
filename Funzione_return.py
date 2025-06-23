"""RESTITUIRE UN VALORE
Le funzioni possono restituire valori"""



def somma(a,b):
    res =a+b  #variabile privata (interna)
    print(f"Il valore di sum ALL'interno della funzione somma() è {res}")
    return res

def calcola_somma_e_differenza (a,b):
    sum=a + b
    dif=a - b
    return sum, dif

pippo= somma(23,78)
#print(res) non può funzionare perchè res è una variabile interna alla funzione... è accessibile solo nella funzione, a meno di usare Return
print(pippo) #non posso fare il print di res, ma posso fare il print di pippo, variabile a cui ho assegnato il valore.
#OPPURE res=somma(....) usato Pippo per non confondere. è un res diverso dalla variabile privata
#res in una funzione e res esterna non sono la stessa cosa.

print("\n==\n")
"""RESTITUIRE VALORI MULTIPLI restituire più valori sottoforma di tupla"""
res1,res2 = calcola_somma_e_differenza(78,23)
print(f"la somma vale {res1}")
print(f"la differenza vale {res2}")