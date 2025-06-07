
def validate(opciones:list, eleccion:str)->str:
    #Se crea un ciclo while, el cual verifica si la opción ingresada está en la lista de opciones,
    #de no ser así da msg de error y solicita ingresar una nueva opción, luego retorna la opcion validada.
    while eleccion not in opciones:
            print ("Opción no válida, ingrese una de las opciones válidas:")
            eleccion = input('Ingresa una Opción: ').lower()
    return eleccion
            


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
