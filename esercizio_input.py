#INPUT istruzione che chiede all'utente di inserire qualcosa a tastiera. indipendentemente dal tipo lo considera una stringa di testo
print("Questo programma calcola l'area di un rettangolo: ")
altezza= int(input("inserire altezza del rettangolo: ")) #inserisco dentro la variabile il nome inserito nella tastiera
base= input("inserire base del rettangolo: ")
area=altezza* int(base)
print(f"L'area del rettangolo di altezza {altezza} e base {base} è {area}")
# stampa la stringa di testo + la variabile nome (str)

