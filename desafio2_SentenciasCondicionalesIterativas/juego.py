#Importar lo necesario
import random
import sys


#Definir opciones
opciones=["piedra","papel","tijeras","salir"]


while True:
    try:
        #Definir opcion de jugador y del compu para esta vuelta
        j=input('Elige piedra, papel o tijeras, si quieres detener el juego escribe "salir": ').lower()
        compu=random.choices(opciones)
        compu=compu[0]

        #Establecer resultado para cada caso
        if j not in opciones:
            print('Invalido, debe ser "piedra", "papel" o "tijeras"')
            continue
        elif j =="salir":
            print('Hasta la proxima')
            break
        elif j==compu:
            print('Empate!')
        elif (j=="piedra" and compu=="tijeras") or (j=="papel" and compu=="piedra") or (j=="tijeras" and compu=="papel"):
            print(f'Tu eligiste {j}, el computadór eligió {compu}:')
            print('Ganaste!!')
        else:
            print(f'Tu eligiste {j}, el computadór eligió {compu}:')
            print('Perdiste!')

    #En caso de romperse el programa
    except:
        print("No can do")
        break
