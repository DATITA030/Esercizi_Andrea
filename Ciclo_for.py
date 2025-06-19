"""CICLO FOR :struttura iterativa utilizzata per eseguire un blocco di codice per un determinato numero di volte
questo in base a un valore iterabile.
il ciclo for si basa su una variabile d'appoggio che ad ogni iterazione assume il valore sell'elemento successivo
"""
for i in range (10,20):


    ...   #mi tolgono l'errore, utile in futuro per saltare pezzi di codice già checkati e andare a vanti senza errore nel codice

for i in range(10, 20):


    pass       #mi tolgono l'errore, utile in futuro per saltare pezzi di codice già checkati e andare a vanti senza errore nel codice


parola="python"
for lettera in parola:
    print(lettera)


for n in range(1,11): #1 incluso 11 escluso
    print(n)

print("\n================\n")

"""metodo RANGE"""
#range(stop) genera un numero da 0 allo stop -1
range(5)

#range(start,stop) genera un numero dallo start a stop-1
range(1,11) #come visto nel secondo esempio

#range(start,stop,step) genera un numero dallo start(3), lo stop-1 (54) e il salto (2)
for n in range(3,54,2):
    print(n)
print("\n================\n")
"""anche il ciclo FOR può usare il BREAK e funziona come nel ciclo while"""

for numero in range(10):
    if numero==5:
        print("break", numero)
        break
    print(numero)



print("\n================\n")
"""anche il ciclo FOR può usare il CONTINUE e funziona come nel ciclo while"""
for number in range(10):
    if number==5:
        print("salto il",number)
        continue
    print(number)
else:
    print("il ciclo for con il continue è finito")

print("\n================\n")

#tabellina 8
for number in range(8,81,8):
    print(number)

#tabelline... di raffaele, 1 cicli for annidato
for i in range (1,10): #i =1 e j sale
    print(f"TABELLINA DEL {i}")
    for j in range(1,11): #finiti tutti i j, porta i su di uno.. quindi I=2 e lo moltiplica poi per tutti i j
        print(i*j, end=" ") #un \n nascosto che fa andare a capo se gli dici end=qualcosa
    print()