
print("Hola, esta es una guía basica para hacer primeros Auxilios")

while True:
    print("La persona responde a estimulos?")
    r1=input("Si/No: ").strip().lower()

    if r1=="si":
        print("Evaluar la necesidad de llevar a la persona al hospital mas cercano")
        break
    elif r1=="no":
        print("Abrir la via aerea de la persona")
        print("Respira?")
        r2=input("Si/No: ")

        if r2=="si":
            print("Permitir posición de suficiente ventilación")
            break

        elif r2=="no":
            print("Administrar 5 respiraciones boca a boca y llamar ambulancia")

            while True:
                print("Tiene signos vitales?")
                r3=input("Si/No: ")

                if r3=="si":
                    print("Reevaluar a la espera de ambulancia")
                    r4=input("Llegó la ambulancia?..... Si/No: ")
                elif r3=="no":
                    print ("Administrar compreciónes torácicas hasta que llegue la ambulancia")
                    r4=input("Llegó la ambulancia?..... Si/No: ")

                if r4=="no":
                    continue
                elif r4=="si":
                    break
            break
