
print("buongiorno, benvenuto al suo ATM di fiducia")

valore=float(input("\ndigitare il valore da convertire: "))

valuta=input("""indicare la valuta che si vuole usare:
0 per €
1 per $
2 per £
3 per §
4 per ¥
5 per ₹:
""")


Euro=1
Dollaro_usa=1.15649
Sterlina= 0.85174
Simoleon= 34
Yen= 166.896
Rupia= 99.65




if valuta== "0":
    Valore_cambio = valore*Euro
    print(f"\nInserendo{valore} scegliendo {valuta}, riceverari {Valore_cambio:.2f}€")
elif valuta== "1":
    Valore_cambio = valore*Dollaro_usa
    print(f"\nInserendo{valore} scegliendo {valuta}, riceverari {Valore_cambio:.2f}$")
elif valuta== "2":
    Valore_cambio = valore*Sterlina
    print(f"\nInserendo{valore} scegliendo {valuta}, riceverari {Valore_cambio:.2f}£")
elif valuta== "3":
    Valore_cambio = valore*Simoleon
    print(f"\nInserendo{valore} scegliendo {valuta}, riceverari {Valore_cambio:.2f}§")
elif valuta== "4":
    Valore_cambio = valore*Yen
    print(f"\nInserendo{valore} scegliendo {valuta}, riceverari {Valore_cambio:.2f}¥")
elif valuta== "5":
    Valore_cambio = valore*Rupia
    print(f"\nInserendo{valore} scegliendo {valuta}, riceverari {Valore_cambio:.2f}₹")
else:
    print(f"\nValuta non accettata")






