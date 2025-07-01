

class User:
    def __init__(self,name,age,surname,address,fiscal_code):

        #attr pubblici
        self.name=name
        self.age=age

        #attributo protetto
        self._surname= surname

        #attributo privato
        self.__address =address
        self.__fiscal_code= fiscal_code

    #metodo pubblico
    def say_hello(self):
        return f"Ciao, sono {self.name} {self._surname}, vivo a {self.__address} e ho {self.age} anni {self._drive()} e quando la uso {self.__music()}"

    #metodo protetto
    def _drive(self):
        return "la mia macchina è una Subaru baracca "

    #metodo privato
    def __music(self):
        return f"La mia banda suona il rock ed è un'eterna partenza, funziona a onde medie e modulazione di frequenza"

    #metodo getter per __address (uso lo snake case e rimuovo i due underscore)
    def get_address(self):
        return self.__address

    #metodo setter per __address
    def set_addres(self,address):
        self.__address =address

    @property
    def fiscal_code(self):
        return self.__fiscal_code

    #metodo setter con il decoratore
    @fiscal_code.setter
    def fiscal_code(self, fiscal_code):
        self.__fiscal_code=fiscal_code


if __name__== "__main__":
    # test e debug
    user_obj =User("Marco",30,"Aurelio","Polibio")
    print(user_obj.say_hello())
    print(user_obj._drive())

    #richiamo un metodo get con il decoratore property Viene richiamato non come se fosse un METODO, ma come un ATTRIBUTO Pubblico
    print(user_obj.fiscal_code)

    #imposto il valore di fiscal_code usando il metodo setter
    #con il decoratore
    user_obj.fiscal_code="nuovo codice fiscale"
    print(f"Il nuovo codice fiscale di {user_obj.name} è {user_obj.fiscal_code}")