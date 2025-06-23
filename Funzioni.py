"""Le FUNZIONI, chiamate anche METODI (in alcuni contesti programm ad oggetti), sono blocchi di CODICI RIUTILIZZABILI
progettati per eseguire un'OPERAZIONE SPECIFICA (SRP).
Le funzioni consentono di ORGANIZZARE, RIUTILIZZARE (DRY) e MANTENERE il codice in modo più semplice ed efficente.

DRY: Don't Repeat Yourself  :se ci sono più azioni ripetute è vanno messe in funzioni a parte (ogni funzionalità deve apparire una sola volta).
SRP: Single responsibility Principle: ogni funzione fa 1 e 1 sola istruzione  (1 responsabilità, 1 solo compito)"""

def nome_funzione(parametro1,parametro2):
    print(parametro1)
    print(parametro2)

def saluta(nome):
    print(f"Ciao!{nome}!")

def somma(a,b):
    sum=a+b
    print(f"il valore della somma di a+b è {sum}")

def somma_default(a=5,b=3):          #parametri di default
    sum=a+b
    print(f"la somma di a+b è {sum} (default)")

def differenza(a,b):      #KEYWORDS argument
    diff=a-b
    print(f"la differenza di {a} - {b} è {diff}")

def stampa_elenco(*elenco):        #parametri arbitrari
    for item in elenco:
        print(item)

def stampa_dizionario(**dizionario):
    for chiave, valore in dizionario.items():
        print(f"{chiave}->{valore}")

#invocare la funzione basta scrivere il nome della funzione
nome_funzione("nome","Andrea")
nome_funzione("cognome","Marzorati")
nome_funzione("età",26)

"""Se una funzione viene definita, ma non invocata, non viene eseguita!!"""

print() #per fare uno spazio

saluta("Antonio")

somma(12,38)
somma(2099,534)
somma(12.2,42)
somma("alice","pizza")

#parametri di default
somma_default() #se non scrivo valori mi rimangono quelli di default
somma_default(27,15) #se scrivo dei valori li sovrascrivo
somma_default(26,) #sovrascrivo solo il primo
somma_default(b=30) #sovrascrivo il secondo però è un Keyword argument, non con i parametri di default

"""Keyword arguments """
print("\n\n")

differenza(3,9)
differenza(5,3)
differenza(b=3,a=5) #posso scriverli come voglio, a sarà sempre il 1° e b il 2°

"""Parametri Arbitrari  in grado di ricevere un numero arbitrario di parametri
in formato tupla utilizzando il simbolo asterisco *"""

print("\n\n")

stampa_elenco(1,2,3,4,5)# sono tuple perchè hanno parentesi tonde, non modificabili e ordinate
stampa_elenco("rosso","blu","giallo")

print("\n\n")

stampa_dizionario(nome="Anna",age=72,city="corsicosCity")

stampa_dizionario(a="Rosso",b="Verde",c="Blu")