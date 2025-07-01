#questa è una classe DERIVATA
from esercizio_classi.employee import Employee


class Manager(Employee):
    #attributo di classe
    yearly_bonus=20
    def __init__(self,name,h_pay):
        #invoco il metodo init della super class (Employee)
        super().__init__(name,h_pay)