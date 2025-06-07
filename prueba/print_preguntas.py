import preguntas as p

# Imprimir enunciado y alternativas
def print_pregunta(enunciado:list, alternativas:list)->str:
    letras=['A','B','C','D']
    print(enunciado,"\n")

    for a in range(len(alternativas)):
        print(f"{letras[a]}. {alternativas[a][0]}")

    
   
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4