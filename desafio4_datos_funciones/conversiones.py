import sys

try:
    if len(sys.argv)==5:
        conv_soles=float(sys.argv[1])
        conv_arg=float(sys.argv[2])
        conv_dollar=float(sys.argv[3])
        cash=float(sys.argv[4])
    else:
        conv_soles=float(input("Tasa de conversión a soles: "))
        conv_arg=float(input("Tasa de conversión a pesos argentinos: "))
        conv_dollar=float(input("Tasa de conversión a dolares: "))
        cash=float(input("Monto de dinero a convertir: "))


    convertidor={
        "soles":cash*conv_soles,
        "Pesos Argentinos":cash*conv_arg,
        "Dólares":cash*conv_dollar
    }

    print(f"\nLos {cash:.0f} pesos equivalen a:")
    for k,v in convertidor.items():
        print(f"{v:.2f},{k}")
    print()

except Exception as e:
    print("Los datos ingresados no son validos dado: ",e)


