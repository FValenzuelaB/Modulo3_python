import sys

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

try:
    if len(sys.argv)>1:
        monto=int(sys.argv[1])
    else:
        monto=int(input("Ingrese monto minimo: ")) 

    new_dict={
        key: value for (key, value) in ventas.items() if ventas[key]>monto 
    }

    print(new_dict)

except ValueError:
    print("Ingrese un valor valido en formato de numero entero")
