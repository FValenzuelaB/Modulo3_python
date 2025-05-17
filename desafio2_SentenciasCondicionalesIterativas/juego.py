#Importar lo necesario
import random
import sys


#Definir opciones y resultado computadora
opciones={"piedra","papel","tijeras"}
compu=random.choices(opciones)
compu=compu[0]

#Pedir a jugador su elección

while True:
    try:
        j=input('Elige piedra, papel o tijeras, si quieres detener el juego escribe "salir": ').lower()

        if j not in opciones:
            print('Invalido, debe ser "piedra", "papel" o "tijeras"')
            continue
        elif j =="salir":
            print('Hasta la proxima')
            break
        elif j==compu:
            print('Empate!')
        elif (j=="piedra" and compu=="tijeras") or (j==)
