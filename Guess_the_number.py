import random


numero_segreto=random.randint(1,1000)
numero_giocato=""
tentativi=0

while numero_segreto != numero_giocato and tentativi<10:
    numero_giocato=int(input("inserisci il numero intero, ricorda hai 10 tentativi: "))
    if numero_giocato < numero_segreto :
        print("numero troppo basso, ritenta")
        #numero_giocato=int(input("numero troppo basso, ritenta"))
    elif numero_giocato>numero_segreto:
        print("numero troppo alto, ritenta")
       # numero_giocato=int(input("numero troppo alto, ritenta"))
    else:
        print(f"\nBravissimo hai indovinato il numero_segreto, il numero:{numero_segreto}")
    tentativi+=1

if numero_giocato!=numero_segreto:
    print(f"\nMi dispiace hai finito i tentativi!\nIl numero segreto era: {numero_segreto}")

print("\nPremi sul punsante PLAY per giocare di nuovo ")
#print(f"\nBravissimo hai indovinato il numero_segreto, il numero:{numero_segreto}")
