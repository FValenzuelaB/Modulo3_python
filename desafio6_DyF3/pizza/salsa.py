


def salsa(pizza:dict)->dict:
    salsas=["Salsa de Tomate","Salsa Alfredo","Salsa Barbeque","Salsa Pesto"]

    i=int(input("""
        Seleccionar tipo de salsa
        1. Salsa de Tomate.
        2. Salsa Alfredo.
        3. Salsa Barbeque.
        4. Salsa Pesto.
        \n"""))
    if i in range(1,5):
        pizza["salsa"]=salsas[i-1]
        return pizza
    else:
        return("Ingrese una opcíon valida")

if __name__=="__main__":
    salsa()