"""Esercizio su scontrino per input e F-string"""

numero_articoli= int(input("Quanti articoli hai acquistato?"))
costo_singolo =float(input("Quanto costa il singolo articolo?"))
totale= numero_articoli * costo_singolo

print(f"Acquistando {numero_articoli} articoli al costo singolo di {costo_singolo}€, spenderai {totale}")

sconto=int(input("se hai uno sconto dimmi quanto vale in %: "))

sconto_effettivo = totale * sconto/100

totale_scontato= totale - sconto_effettivo

print(f"Acquistando {numero_articoli} articoli al costo singolo di {costo_singolo}€, spenderai {totale} con il {sconto}% di sconto avrai un costo finale di {totale_scontato:.2f}€") # :.2f mi indica i decimali del float
print(f"lo sconto ricevuto è di {sconto_effettivo:.2f}")
