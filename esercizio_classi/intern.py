#questa è una classe DERIVATA
from esercizio_classi.clerk import Clerk


class Intern(Clerk):
    forfait=280

    def __init__(self,name,h_pay,boss):
        super().__init__(name,0,boss)

    def calc_wage(self):
        print(f"{self.name}, guadagna {self.forfait}$ al mese ")
