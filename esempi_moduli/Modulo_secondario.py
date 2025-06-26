
def funzione_modulo_secondario():
    print("sono la funzione del modulo secondario")

variabile_del_modulo_secondario =5.78

#per evitare che questo pezzo venga preso quando non voglio devo fare un if così
if __name__=="__main__":
    print("Ciao sono il modulo secondario")
    print("La variabile __name__ del modulo secondario ha valore", __name__)