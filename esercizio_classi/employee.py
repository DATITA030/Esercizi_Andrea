#è la classe base



class Employee:
    def __init__(self,name,h_pay):
        self.name = name
        self.h_pay = h_pay

    def calc_wage(self):
        print(f"metodo per calcolare la RAL di {self.name}, che guadagna {self.h_pay}$/h")