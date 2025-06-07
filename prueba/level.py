def choose_level(n_pregunta:int, p_level:int):
    if p_level not in [1,2,3]:
        raise ValueError ("La cantidad de preguntas por nivel debe ser 1, 2 o 3")
    
    elif p_level ==1:
        if n_pregunta ==1:
            return 'basicas'
        elif n_pregunta==2:
            return 'intermedias'
        elif n_pregunta ==3:
            return 'avanzadas'
        else:
            return ("Ingrese un numero valido de preguntas por nivel")
    
    elif p_level==2:
        if n_pregunta in [1,2]:
            return 'basicas'
        elif n_pregunta in [3,4]:
            return 'intermedias'
        elif n_pregunta in [5,6]:
            return 'advanzadas'
        else:
            return ("Ingrese un numero valido de preguntas por nivel")
        
    elif p_level==3:
        if n_pregunta in [1,2,3]:
            return 'basicas'
        elif n_pregunta in [4,5,6]:
            return 'intermedias'
        elif n_pregunta in [7,8,9]:
            return 'advanzadas'
        else:
            return ("Ingrese un numero valido de preguntas por nivel")
    
    

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias