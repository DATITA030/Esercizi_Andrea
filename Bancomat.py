"""deposito, prelievo, saldo, uscita)
gestione PIN o sicurezza base
limiti di saldo o blocco conti  il saldo verrà generato randomicamente per provare più casistiche
in realtà dovrebbe avere accesso ad un file dove leggere i nomi e i saldi."""

#LAVORI IN CORSO.. MEN (man visto che sono solo) AT WORK (?!?)

# 2prelievo rapido; 1inserire carta; 3 Pin; 4 scontrino

import random
print("Benvenuto presso il nostro Bancomat, prego inserire la carta ")
#deposito=float(input("inserisci la cifra che vuoi depositare"))
saldo=random.uniform(-5555.99,5000.99)

selezione=int(input("""selezionare l'opzione desiderata:"
0 visione saldo
1 deposito
2 Rapido_50
3 Rapido_100
4 Rapido_200
5 Prelievo
6 Exit
:... """))
Rapido_50 = 50
Rapido_100 = 100
Rapido_200 = 200

PIN=34782 # creo/inizializzo la variabile PIN da verificare

blocco_conto=""
limite_prelievo=3000
if selezione <=5:
    PIN_ins = int(input("inserire il PIN della carta"))
    while PIN != PIN_ins:  # verifica pin fino a codice giusto
        PIN_ins = int(input("pin errato riprovare:"))
    if selezione == 0: #prelievo <= limite_prelievo:
        print(f"il tuo saldo è di :{saldo:.2f}€")
    elif selezione == 1:
        deposito=int(input("inserire quanto si vuole depositare\n:"))
        nuovo_saldo= saldo + deposito
        print(f" ha scelto di depositare {deposito}€ il nuovo saldo è di {nuovo_saldo:.2f}€")
    elif selezione == 2:
        print(f"il saldo attuale è di: {saldo:.2f}")
        nuovo_saldo = saldo - Rapido_50
        print(f"Perfetto, hai prelevato {Rapido_50}€\nIl tuo nuovo Saldo è di :{nuovo_saldo:.2f}€")
    elif selezione ==3:
        print(f"il saldo attuale è di: {saldo}")
        nuovo_saldo = saldo - Rapido_100
        print(f"Perfetto, hai prelevato {Rapido_100}€\nIl tuo nuovo Saldo è di :{nuovo_saldo:.2f}€")
    elif selezione ==4:
        print(f"il saldo attuale è di: {saldo:.2f}")
        nuovo_saldo = saldo - Rapido_200
        print(f"Perfetto, hai prelevato {Rapido_200}€\nIl tuo nuovo Saldo è di :{nuovo_saldo:.2f}€")
    else:
        prelievo = int(input("inserire quanto si vuole prelevare\n:"))
        if prelievo <= limite_prelievo : #vorrei aggiungere anche un limite saldo... per tutti i prelievi....
            nuovo_saldo=saldo- prelievo
            print(f"Perfetto, hai prelevato {prelievo}€\nIl tuo nuovo Saldo è di :{nuovo_saldo:.2f}€")
        else:
            print("\nLimite prelievo superato, provare più tardi")

else:
    print("opzione al momento non presente attendere aggiornamenti") #così però non mi piace, devo ragionare sul da farsi
nuovo_saldo=saldo            #verificare attentamente linea 64 e 65... se con il prelievo (pulsante 5) vado in negativo non appare il messaggio
if nuovo_saldo<0 or saldo<0 :
    print(f"Saldo negativo attenzione{saldo:.2f}")
print("Ritirare la carta, arrivederci")

#accesso=int(input("""selezionare l'operazione desiderata:
#0 visione saldo
#1 deposito
#2 prelievo
#"""))




