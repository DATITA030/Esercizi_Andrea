"""stampo un elenco di numeri fino a che non me lo dice l'utente.
se il numero è multiplo di 3 stampo fizz, se è multiplo di 5 scrivo buzz
se è multiplo di 15 fizzbuzz"""


#1°metodo
"""
numeri=int(input("inserisci un numero: ").strip())
for n in range(1,numeri+1):
    if n %15 ==0:
        print("Fizz_Buzz")
    elif n%5 ==0:
        print("Buzz")
    elif n% 3==0:
        print("Fizz")
    else:
        print(n)
"""
#2°metodo
"""
def buzz():
    print("buzz")
def fizz():
    print("fizz")
def fizz_buzz():
    print("Fizz_Buzz")

numeri=int(input("inserisci un numero: ").strip())
for n in range(1,numeri+1):
    if n %15 ==0:
        fizz_buzz()
    elif n%5 ==0:
        buzz()
    elif n% 3==0:
        fizz()
    else:
        print(n)

buzz()
"""

#3°metodo
"""
numeri=[]
while True:
    numero= input("inserisci un numero o digita fine: ")
    if numero== "fine":
        break
    else:
        numeri.append(int(numero))

for n in numeri:
    if n %15 ==0:
        print("Fizz_Buzz")
    elif n%5 ==0:
        print("Buzz")
    elif n% 3==0:
        print("Fizz")
    else:
        print(n)
print(numeri)

"""

"""

def stampa_fi_bu(stringa):
    print(stringa)

numeri=int(input("inserisci un numero: ").strip())
for n in range(1,numeri+1):
    if n%5==0:
        stampa_fi_bu("Fizz_Buzz")
    elif n % 5 == 0:
        stampa_fi_bu("Buzz")
    elif n % 3 == 0:
        stampa_fi_bu("Fizz")
    else:
        print(n)
"""