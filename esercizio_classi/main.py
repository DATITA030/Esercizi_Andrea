#qui scrivo il codice vero del software
from esercizio_classi.animals import Anatra, Squalo
from esercizio_classi.clerk import Clerk
from esercizio_classi.intern import Intern
from esercizio_classi.manager import Manager

if __name__ == "__main__":

    #assumo un manager
    obj1= Manager("Donaldo Trumpo", 25)

    #invoco il metodo calc_wage() del manager
    obj1.calc_wage()

    #assumo un clerk
    obj2= Clerk("JD VanCess", 10,"Donaldo Trumpo")

    #invoco il calc_wage() del clerk
    obj2.calc_wage()

    #assumo un intern
    obj3 = Intern("Michelone Johnson",0,"Donaldone Trump")
    # invoco il calc_wage() del intern
    obj3.calc_wage()
    print()

    #voglio vedere gli stipendi di tutti i miei dipendenti
    dipendenti=[obj1,obj2,obj3]
    for dipendente in dipendenti:
        dipendente.calc_wage()

    print()

    animal_obj1=Anatra()
    animal_obj1.nuota()
    animal_obj1.vola()

    animal_obj2 = Squalo()
    animal_obj2.nuota()
