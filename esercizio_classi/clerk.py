# questa è una classe DERIVATA
from esercizio_classi.employee import Employee


class Clerk(Employee):
    def __init__(self,name,h_pay,boss):

        super().__init__(name,h_pay)

        #attributo di istanza specifico per i clerk
        self.boss = boss