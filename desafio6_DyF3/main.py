from pizza.menu import menu
from pizza.masa import masa
from pizza.salsa import salsa
from pizza.ingredientes import fun_ingredientes


def main():
    ingredientes=[]
    pizza={
        "masa":"",
        "salsa":"",
        "ingredientes":ingredientes
        }
   
    while True:
        
        menu()
        opcion=input("Seleccione una opción: ")
        if opcion in ["1","2","3","4","5"]:
            True
        else:
            raise ValueError("Ingrese una opción valida (1,2,3,4 o 5), vuelva a empezar su pedido")

        if opcion=="1":
            masa(pizza)
            print(f"El tipo de masa elegida es: {pizza["masa"]}")
        
        elif opcion=="2":
            salsa(pizza)
            print(f"El tipo de salsa elegida es: {pizza["salsa"]}")

        elif opcion=="3":
            ingredientes=fun_ingredientes(ingredientes)
            print(f"Los ingredientes elegidos son: {ingredientes}")

        elif opcion=="4":
            print(f"\nLa pizza actual está compuesta de la siguiente manera: ")
            for k,v in pizza.items():
                print(f"{k}:{v}")

        elif opcion=="5":
            confirmacion=input(f"""
                  El pedido actuál tomará {20+len(ingredientes)*2} minutos, desea confirmar el pedido?
                  1. Si
                  2. NO
                  """).lower().strip()
            if confirmacion=="1" or confirmacion=="si":
                print("Gracias por su pedido! que lo disfrute")
                break
            else:
                continue
                
            
main()
        