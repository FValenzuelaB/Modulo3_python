

def factorial(numero:int):
    facto=1
    for i in range(1,numero+1):
        facto*=i
    return f"el factorial de {numero} es {facto}"
 

def productoria(numeros:list):
    prod=1
    for i in numeros:
        prod*=i
    return f"La productoria de {numeros} es {prod}"


