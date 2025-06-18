#  si possono usare per le stringhe.. sia i " che i '... meglio " perchè non si usano nella lingua italiana
from operator import truediv

print("Hello World")
print('Hello World')
pippo = 5
pippo=42
pluto=42.5 #decimale si usa il punto 42.5
minni= "42.5"
# tippizzazione dinamica, python riconosce da solo il tipo di dato inserito: int, float, char, str
#si può cambiare il tipo assegnando valore diverso
#pippo ≠ Pippo Case sensitive
a,b,c = 3,4,5  #assegnazione multipla , ma meglio evitare di usarla
print(a,b,c)
print(pippo)
#esperimenti tipi
print(type(pippo)) # mi stampa il tipo di variabile usata
print(type(minni))

messaggio = 'Alessandro Manzoni ha scritto "I Promessi Sposi "' #Si può usare anche \" \" indica un carattere che va stampato CARATTERE DI ESCAPE
# messaggio = "Alessandro Manzoni ha scritto \"I Promessi Sposi \""
print(messaggio)
messaggio = """Nel mezzo 
del cammin 
di nostra vita""" #stirnghe multilinea
print(messaggio)

#CONCATENAZIONE DI STRINGHE:
nome = "Andrea" #string 1
saluto = "Ciao" #string 2
print(saluto + " " + nome) # ho concatenato fra le " lo spazio per separare Ciao Andrea

#ripetizione stringhe
print ("Ciao a tutti! " *3)

#ESPERIMENTI OPERATORI
somma =5 + 6   #+
print(somma)
sottrazione= 6-5   #-
print(sottrazione)
moltiplicazione = 6*5  #*
print(moltiplicazione)
divisione = 43/7  #/
print(divisione)
divisione_senza_resto = 43//7  # // divisione senza resto oppure divisione intera
print(divisione_senza_resto)
esponente = 5**3   #**
print(esponente)

MODULO =5 % 2 # % MODULO oppure RESTO DIVISIONE
print(MODULO)
print(13 % 3)
print(12 % 3)  #il modulo ha un numero di risultati pari al "divisore"  %3 ha 3 risultati 0,1,2  modulo %5 5 risultati 0,1,2,3,4  -

#numeri float
x= 0.1 +0.2
print(x) # a causa della trasformazione in binario dei numeri pycharm e python non potendo andare all'infinito daranno 0.30000000000004 o altro come fine

#OPERATORI DI CONFRONTO (>)  (<)  (>=)   (<=)  (==) (!=)
# == ad esempio in un IF costo_margherita == costo_diavola print("costano uguale")
# !=  DIVERSO  stesso esempio


#BOOLEANI solo True e False e sono con la T e la F maiuscola
valore_booleano_vero = True
valore_booleano_falso = False

print (5>3) #mi ristituira' il valore True
print(5<3)   #mi ristituira' il valore False
print(10==10)   #mi ristituira' il valore True

print(True+True) #1+1
print(True+False)  #1+0

#OPERATORI LOGICI:   AND     OR     NOT
#(5>3) and (10>5)  True entrambe le condizioni vere
#(5>10) or (10>5)  True se almeno 1 è True
# not (5>3)  inverte il valore logico
print("Lucciola")
print (5>3)
print(5<3)
print("\n""inizio")
print((5 > 3) and (5 < 3))
print((5 > 3) or (5 < 3))
print(not(5<3)) # mi restituisce l'opposto quindi mi da True al posto di False (5<3)
print("test errore\n")
print((5 > 3) and print(5 < 3))

#Typecasting
pi_greco = 3.14
# print("il valore di pi greco è" + pi_greco) # non funziona perchè non si possono concatenare str e float, ma solo tra str e str o simili.
print("il valore di pi greco è " + str(pi_greco)) #trasformo il valore float in una stringa di testo

#Typecastin implicito
somma= 5+ 3.14 #mi cambia il tipo in maniera dinamica e implicita
print(type(somma))
name = "Marta"
age = 27
print("\nMi chiamo " + name + " e ho " + str(age) + " anni." )

#F-STRINGS (format string [stringe formattate]
#Per essere riconosciuta deve iniziare con la lettera f o F
name = "Alice"
age = 25
print(f"Mi chiamo {name} e ho {age} anni")

a=15
b=43
print (f"la somma di {a} e {b} è {a+b}")

ora= 17
pro =23
nobis = ora + pro
print(super)
print(f"La somma di {ora}+{pro} è {ora +pro}")
scoobydoo= True
shaggy=False


#INPUT istruzione che chiede all'utente di inserire qualcosa a tastiera. indipendentemente dal tipo lo considera una stringa di testo
