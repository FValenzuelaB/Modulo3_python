

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


def calcular(**kwargs):
    for k,v in kwargs.items():
        if "fact_" in k:
            print(factorial(v))
        elif "prod_" in k:
            print(productoria(v))
        else:
            raise SyntaxError("Debes ingresar el requerimiento con formato fact_1 = int, prod_1 = list[int o float], etc") 


calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
