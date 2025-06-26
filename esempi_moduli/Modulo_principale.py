import Modulo_secondario
if __name__ == "__main__":
    print("ciao sono il modulo principale")
    print("La variabile del modulo principale ha valore", __name__)
    Modulo_secondario.funzione_modulo_secondario()
    print(Modulo_secondario.variabile_del_modulo_secondario)

