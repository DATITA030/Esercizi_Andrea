class Automobile:
    n_ruote= 4 #attributo di classe tutte le auto hanno 4 ruote

    #metodo statico
    @staticmethod
    def info():
        print("Una automobile è un mezzo di trasporto su ruote")

    #metodo di classe
    @classmethod
    def start(cls):
        print("Avvio la leggenda")

    @classmethod
    def stop(cls):
        print("Meglio se la spengo, 40 milioni è un attimo perderli")

    #metodo init (anche lui è un metodo dunder [doppio underscore]
    def __init__(self,marca,modello,telaio):
        self.marca=marca
        self.modello=modello
        self.telaio=telaio

    #metodo dunder
    def __str__(self):
        return f"Questa auto è una {self.marca}, modello {self.modello}, telaio n° {self.telaio}"

    def accendi_navigatore(self,navigatore):
        if navigatore== True:
            print("Con questo navigatore posso viaggiare senza cartina")
        else:
            print("Nel '62 i navigatori erano i passeggeri, mi perderò di sicuro!!!")

    def modalità_volo(self,volo):
        if volo==True:
            print("Strade? Dove andiamo noi, non servono... strade.")
        else:
            print("Mi dispiace, ma non è una DeLorean")


#invoco il metodo statico a partire dalla classe
Automobile.info()

#visualizzo il valore di attributo di classe a partire dalla Classe
print(f"ogni automobile ha: {Automobile.n_ruote} ruote")

#invoco i due metodi di classe a partire dalla CLASSE
Automobile.start()
Automobile.stop()

car_obj=Automobile("Ferrari","250 GTO","3705GT")
car_obj2=Automobile("DeLorean Motor Company","DMC-12","Back To the Future")
print(car_obj.__str__())
print(car_obj2.__str__())

#posso invocare il metodo dunder str anche così
print(car_obj)

#invoco il metodo di istanza a partire dall'ISTANZA della classe
car_obj.accendi_navigatore(False)
car_obj.modalità_volo(False)
car_obj2.modalità_volo(True)
#invoco il metodo statico a partire dall'istanza



