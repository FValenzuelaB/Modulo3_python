

def fun_ingredientes(ingredientes:list)->list:
    #este se usa para el caso de ejecutar esta función sola, no desde main, además se usa para guardar ingredientes localmente
    ingredientez=[]
    #Menu para agregar o quitar ingredientes
    n=input("""
            Indique que desea hacer
            1. Agregar Ingredientes.
            2. Eliminar ingredientes.
            """)
    #Para agregar ingredientes opcion1, se muestran los disponibles y se crea lista de nuevos ingredientes,
    #los cuales luego se agregan a la ya existente proveniente desde main, para finalmente devolver la lista modificada.
    if n=="1":
        print(f"""
        La lista actual de ingredientes es {ingredientes}
        Los Ingredientes disponibles son:
        Tomate, Champiñones, Aceituna, Cebolla, Pollo, Jamón, Carne, Tocino, Queso
        """)
        ing=input("Ingrese los ingredientes deseados en formato 'Carne tocino queso' sin comas, solo espacios: \n")
        ingred=ing.split(" ")
        ingredientez=[str(i).lower().strip() for i in ingred]
        for i in ingredientez:
            ingredientes.append(i)
        return ingredientes
    
    #Se toma la lista existente de ingredientes, se crea lista de ingredientes a eliminar 
    #y luego con el 'for' se eliminan uno a uno los ingredientes de la listta proveniente de main
    elif n=="2":
        print(f"\n La lista actual de ingredientes es:{ingredientes}")
        e=input("Ingrese elementos a eliminar: ")
        el=e.split (" ")
        elminados=[str(k).lower().strip() for k in el]
        for a in elminados:
            ingredientes.remove(a)
        return ingredientes
    
    #El programa tiene poca resilencia a que el usuario ingrese mal los nombres, como por ejemplo podría agregar 5 veces aceitunas
    #O agregar aceitunas y luego AXEITUNAAZ, y tratar de eliminar AXEITUNAAZ y escribir AXEITUNAZ, con lo que no se eliminaria nada
    #Pero, de momento el test no pide abarcar estas problematicas y sería algo engorroso ahora mismo.

if __name__=="__main__":
    fun_ingredientes()