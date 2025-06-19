#dato un numero in input,scorriamo da 1 a 9, se sono divisori del numero stampiamo il divisore
import math

numero_ins=int(input("inserire un numero intero maggiore di 0:\n"))
if numero_ins==0:
    print("balordo non vale lo 0")
else:
    for numero in range(2, 10):
        resto = numero_ins % numero
        if resto == 0:
            print(f"{numero} E' un divisore di {numero_ins}")
        else:
            print(f"{numero} NON E' un divisore di {numero_ins}")

print("\n=========\n")


num_pr=int(input("inserire un numero intero:\n"))
if num_pr==1: #se uguale a 1 no buono
    print("1 è divisibile solo per se stesso, ma non è primo")
elif num_pr==0: #se uguale a 0 no buono
    print("ora mi hai stufato con sti giochini, lo 0 non vale")
else:  #se il numero inserito è diverso da 0 o 1 inizia il ciclo for
    for num in range(2, int(math.sqrt(num_pr)) + 1): #  ( consiglio raffaele)    num_pr **1/2
        rest = num_pr % num
        if rest == 0:
            print(f"{num_pr} E' divisibile per {num}, quindi non è primo")
            break
    else:
        print(f"{num_pr} NON E' divisibile per {num}, quindi è primo")



        """numero = ""
while not numero.isdigit():
    numero=input("Che numero checkiamo capo? ")

numero = int(numero)"""