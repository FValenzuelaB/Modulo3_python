import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad:str):

    if not opciones[dificultad]:
        return None # No quedan preguntas disponibles en este nivel

    # Elegir una pregunta al azar
    numero = random.choice(opciones[dificultad])  #toma un numero de los que queden entre 1 y 3 para la dificultad elegida
    opciones[dificultad].remove(numero) #ahora que tenemos el numero guardado en parametro numero, eliminamos el numero de la lista

    key = f'pregunta_{numero}' #dado que en preguntas.py todas las preg son pregunta_i, podemos armar str usando "numero".
    pregunta = p.pool_preguntas[dificultad][key] #con el str pregunta_numero podemos invocar la pregunta en cuestión

    alternativas_mezcladas = shuffle_alt(pregunta)

    return pregunta['enunciado'][0], alternativas_mezcladas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')