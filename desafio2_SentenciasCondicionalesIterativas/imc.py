#Pedir datos necesarios para el calculo
m=int(input("Ingrese su peso en Kilogramos: "))
a=float(input("Ingrese su altura en centimetros: "))
a=a/100

#Calcular el IMC
imc=m/(a**2)

#Evaluar calificación de OMS
if imc<18.5:
    oms="Bajo Peso"
elif imc>=18.5 and imc<25:
    oms="Adecuado"
elif imc>=25 and imc<30:
    oms="Sobrepeso"
elif imc>=30 and imc<35:
    oms="Obesidad de Grado 1"
elif imc>=35 and imc<40:
    oms="Obesidad de Grado 2"
else:
    oms="Obesidad de Grado 3"

#Mostrar resultado y calificación OMS
print(f"Su IMC es de {imc:.2f}")
print(f"De acuerdo a la OMS esto califica como {oms}")


