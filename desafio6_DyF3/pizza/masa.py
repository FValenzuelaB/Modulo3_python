

def masa():
    masas=["Masa Tradicional","Masa delgada","Masa con Bordes de Queso"]

    i=int(input("""
        Seleccionar tipo de masa
        1. Masa Tradicional.
        2. Masa Delgada.
        3. Masa con Bordes de queso.
        \n"""))
    if i in range(1,4):
        return masas[i-1]
    else:
        return("Ingrese una opcíon valida")

if __name__=="__main__":
    masa()
    
    
    