""" esercizio calcolatrice in 2 Versioni, meno bella e più elegante """
"""
print("\nBenvenuto/a nella nuova calcolatrice Ramieri Edition!!")
valore_1=float(input("Insersci il 1° valore: "))
valore_2=float(input("Inserisci il 2° valore: "))
operazione=input("inserisci il tipo di operazione, solo il simbolo: ")

if operazione == "+":
    print(f"{valore_1 + valore_2}")
elif operazione =="-":
    print(f"{valore_1 - valore_2}")
elif operazione == "x" :
    print(f"{valore_1 * valore_2}")
elif operazione == "/" :
    print(f"{valore_1 / valore_2}")
elif operazione == "^" :
    print(f"l'^ è uguale a {valore_1 ** valore_2}")
elif operazione == "√" :
    print(f"la √ è uguale a {valore_1 ** (1/valore_2)}")
else :
    print("figa metti un simbolo per fare una operazione!")
"""


print("\nBenvenuto/a nella nuova calcolatrice Ramieri Edition!!")
valore_1=float(input("Insersci il 1° valore: "))
valore_2=float(input("Inserisci il 2° valore: "))
operazione=input("inserisci il tipo di operazione, solo il simbolo: ")

if operazione== "+":
    calcolo= valore_1+valore_2
    print(calcolo)

elif operazione== "-":
    calcolo= valore_1 - valore_2
    print(calcolo)

elif operazione== "*":
    calcolo= valore_1 * valore_2
    print(calcolo)

elif operazione== "/":
    if valore_2==0:
        print("errore")
    else:
        calcolo= valore_1 / valore_2
        print(calcolo)

elif operazione== "^":
    calcolo= valore_1 ** valore_2
    print(calcolo)

elif operazione== "√":
    calcolo= valore_1 *(1/valore_2)
    print(calcolo)

else:
    print("ERRORE")