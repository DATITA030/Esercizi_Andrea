nome= input("scrivi il tuo nome: ")
print(f"Ciao {nome}, come stai?")

print(len(nome)) # lunghezza della stringa - numero di caratteri

print(nome.find("a")) #prima occorrenza della lettera cercata (partendo da 0)

print(nome.rfind("a")) #ultima occorrenza della lettera cercata (partendo da 0)


print(nome.upper())#trasformo TUTTA la stringa in MAIUSCOLO

print(nome.lower())#trasformo TUTTA la stringa in maiuscolo

print(nome.capitalize()) #convertire l'iniziale in maiuscolo

print(nome.isalpha()) # verifica se tutti i caratteri digitati siano lettere

print(nome.isdigit()) # verifica se tutti i caratteri digitati siano numeri

print("\n")

print(nome.startswith("and")) # iniziaCon controlla se la stringa inizia con carattere o serie di caratteri

print(nome.endswith("ra"))  #finisceCon controlla se la stringa termina con carattere o serie di caratteri

print(nome.count("a")) #controlla le occorrenze di un carattere

print(nome.replace("a", "q")) # sostituisce tutte le occorrenze con un nuovo carattere (sostituzione)

""" no.strip rimuove tutti gli spazi INIZIALI e FINALI di una stringa (noSpazi)"""

nome_senza_spazi = nome.strip()
print(len(nome_senza_spazi))

#print(nome.strip())

print(nome.strip("a")) #RIMUOVE UN CERTO CARATTERE ALL'INIZIO O ALLA FINE DELLA STRINGA (noA)

print(help(str)) #visualizza tutte le informazioni su i metodi delle stringhe. HELP FUNZIONA SU OGNI "metodo"