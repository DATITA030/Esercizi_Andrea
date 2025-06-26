"""PROGRAMMAZIONE ORIENTATA A OGGETTI
La programmazione a oggetti è un PARADIGMA di PROGETTAZIONE
organizza il codice in OGGETTI e CLASSI
Le CLASSI sono insiemi di PROPRIETA' e METODI che gli oggetti hanno in comune
PROPRIETA' descrivono le caratteristiche (Esempio: gli aggettivi)
METODI descrivono le azioni (Esempio: i verbi)
la OOP: permette di creare codice, MODULARE, FACILE DA MODIFICARE e ORGANIZZARE
LA CLASSE è un TEMPLATE sulla quale si creano gli oggetti e si DEFINISCONO le PROPRIETA'(attributi e comportamenti) METODI (comuni agli oggetti che ne fanno parte)

per le Classi sarebbe meglio usare il CamelCase e lo snake_case per variabili...
"""



class NomeClasse:
    def __init__(self):
        print("istruzione dentro il metodo __init__")   #scrivo PASS (pass) per cancellare l'errore, che mi esce fuori perche è vuoto.

obj= NomeClasse() #Ricordarsi le parentesi, se non funziona senza dare errore è per quello

class User:
    def __init__(self,name,age):    #definisco gli attributi
        self.name=name
        self.age= age


    def say_hello(self):
         print(f"Ciao Anna! mi chiamo {self.name} e ho {self.age} anni")

user1=User("Andrea", 26)
user2=User("Agenzia delle Entrate",100)
user1.say_hello()
user2.say_hello()
#risposta= input("ti faccio unadomanda").strip()
#stringa= "nel mezzo del cammin di nostra vita".strip()
print()
print(user1.name)
user1.name="Mario"
print(user1.name)
print()


class Dog:
    species = "Canis Lupus Familiaris"  #attributo di classe, non attributo di istanza
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):         #non costretti a farlo, ma è un metodo che esiste
        return f"name-->{self.name}"    #serve a visualizzare velocemente i metodi degli attributi di istanza

    def make_sound(self):    #metodo di istanza
        return f"{self.name} bark!"

dog1=Dog("Chapo",10)
print(dog1.species)    #attributo di classe, quindi tutti i cani rientrano li
print(dog1.make_sound())

print()
class Cat:
    class_attribute= "Felix felinis"
    class_number =10

    @classmethod  #DECORATORI non sono commenti, ne Keywords, ne codice
    def metodo_di_classe(cls,parametro): #metodo di classe
        cls.class_number += parametro
        return cls.class_number


#metodo statico
    @staticmethod
    def metodo_statico(parametro1, parametro2):
        return parametro1+parametro2

     #metodo di istanza
    def make_sound(self):    #metodo di istanza
        return f"Miao!"

print(Cat.metodo_di_classe(5)) #gli do il parametro che si incrementa al class_number
print(Cat.metodo_statico(2,6))
cat1=Cat()

print(cat1.metodo_di_classe(40))
print(cat1.metodo_statico(10,20))

#METODI STATICI
