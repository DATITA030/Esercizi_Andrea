"""struttura iterativa di controllo utilizzata per eseguire ripeuttamente un blocco di codice finche una condizione è vera.
La condizione viene valutata prima di ogni iterazione e se il risultato è:
True il blocco di codice viene eseguito una volta.
Se è False il ciclo si interrompe."""

contatore=1
while contatore<=5:
    print("contatore:", contatore)
    contatore +=1 #sintassi alternativa a:    contatore = contatore +1

""" l'istruzione break si usa per interrompere il ciclo while anche se la condizione non è ancora diventata falsa"""
print("\n=========================\n")

print("ISTR BREAK")
count=0
while count <=10:
    print("count:",count)
    count+=1
    if count == 4:     #sto cercando questo numero
       print("\nTrovato!",4)
       break            #ora che lo ho trovato termino il while

print("\n===========\n")

"""l'istruzione CONTINUE si usa per saltare l'iterazione corrente e passare alla successiva"""
print("ISTR CONTINUE")
CT=0
while CT<=9:
    CT+=1 #visto che il print è dopo il CT+=1 mi stamperà anche il 10
    if CT ==6:
        print("a questo giro passo oltre")
        continue
    print("CT:", CT) #print è sotto while e fuori dall'IF, quindi scrivo tutti i numeri


print("\n============\n")

""" CICLO WHILE ELSE
si può aggiungere un else anche al ciclo while
questo blocco else si esegue solo se non viene interrotto da un'a istruzione BREAK"""
print("CICLO WHILE ELSE")

contat=1
x=42
while contat<=10:
    if contat==x :
        print("ho trovato x!:",x)
        break
    contat+=1
else:
    print("non ho trovato il numero che volevo")
print("al termine del ciclo while il cod riprende da qui")

print("\n============\n")

"""Validazione input: chiedere tutte le volte che serve un input finche serve e non mi fornisce ci0 che richiedo. """
print("VALIDAZIONE INPUT")


password= ""  #attivo una stringa vuota, mi serve per il ciclo while
contatoree=0

while password != "python123" and contatoree < 3:
    password = input("\nInserisci la password: ")

    if password != "python123":
        contatoree += 1
        print("\nMannaggia, ti sei sbagliato ignorantee!!")
        print(f"Tentativi effettuati: {contatoree}")
    else:
        print("\nAccesso consentito! Bravo Hacker!")
        break

if password != "python123":
    print("Noob, hai raggiunto il massimo numero di tentativi. Accesso negato Looserrr.")





"""while contatoree<3 :
    password =input("\ninserisci la password: ")

    if password == "python123" :
        print("Acesso consentito,Bravo Hacker")
        break
    else:
        contatoree+=1
        print("\nMannaggia, ti sei sbagliato!")
        print(f"Tentativi effettuati: {contatoree}")
else:
    print("Hai raggiunto il massimo numero di tentativi. Accesso negato.")"""
