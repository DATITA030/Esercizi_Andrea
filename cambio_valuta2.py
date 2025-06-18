"""Programma cambio valuta con 2 tassi per fare il cambio valuta anche dell'imput """


print("Buongiorno, benvenuto al suo ATM di fiducia")

valore = float(input("\nDigitare il valore da convertire: "))

valuta_1 = input("""\nIndicare in che valuta si versa:
0 per €
1 per $
2 per £
3 per §
4 per ¥
5 per ₹:
""")

valuta_2 = input("""\nIndicare la valuta che si vuole usare:
0 per €
1 per $
2 per £
3 per §
4 per ¥
5 per ₹:
""")

# se uso una valuta iniziale diversa dall'euro
if valuta_1 == "0":
    tasso_1 = 1
    simbolo_1 = "€"
elif valuta_1 == "1":
    tasso_1 = 1.15649
    simbolo_1 = "$"
elif valuta_1 == "2":
    tasso_1 = 0.85174
    simbolo_1 = "£"
elif valuta_1 == "3":
    tasso_1 = 34
    simbolo_1 = "§"
elif valuta_1 == "4":
    tasso_1 = 166.896
    simbolo_1 = "¥"
elif valuta_1 == "5":
    tasso_1 = 99.65
    simbolo_1 = "₹"
else:
    print("\nValuta di partenza non presente a sistema.")
    exit()

if valuta_2 == "0":
    tasso_2 = 1
    simbolo_2 = "€"
elif valuta_2 == "1":
    tasso_2 = 1.15649
    simbolo_2 = "$"
elif valuta_2 == "2":
    tasso_2 = 0.85174
    simbolo_2 = "£"
elif valuta_2 == "3":
    tasso_2 = 34
    simbolo_2 = "§"
elif valuta_2 == "4":
    tasso_2 = 166.896
    simbolo_2 = "¥"
elif valuta_2 == "5":
    tasso_2 = 99.65
    simbolo_2 = "₹"
else:
    print("\nERRORE, hai perso i soldi.")


if valuta_1 == valuta_2:
    print("\nStai usando lo stesso tasso di cambio.")
else:
    in_euro = valore / tasso_1
    risultato = in_euro * tasso_2
    print(f"\nInserendo {valore:.2f}{simbolo_1}, riceverai {risultato:.2f}{simbolo_2}")
