""" esercizio per il costrutto IF"""

from operator import ifloordiv

print("hello bella gggente!")

valore=int(input("\ninserisci un valore intero uguale a 10: "))

#mutualmente esclusivi
if valore == 10 :
    print("\nDaje bbbravooo, 10 è uguale a 10")
elif 9<= valore <=11 and valore!= 10 :
    print("\nDaje bro ce stai quasi... n'altro pochetto... restarta che ci sei!")
else:
    print("\nMortacci de pippo... t'ho detto 10 sveglia n'po', manco vicino ci sei andato!!! Restarta!")


"""operazione ternario, si usa per assegnare un valore ad una variabile in base ad una condizione"""

valore=94
messaggio= "\nvalore è pari" if valore % 2  ==0 else "\nvalore è dispari"
print(messaggio)
