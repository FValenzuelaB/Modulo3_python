## utilidades= P*U-PG donde P es precio suscripcion, U es numero de usuarios y PG es gastos totales

p=int(input("ingrese precio de suscrpición : $"))
u=int(input("ingrese numero de usuarios:"))
gt=int(input("ingrese gastos totales : $"))
uant=int(input("ingrese utilidades año anterior : $"))

uti=p*u-gt
razon=uti/uant

print(f"las utilidades son: ${uti}")
print(f"y la razón con las del año pasado es: {razon:.2f}")
print(f"o lo que es lo mismo un {(razon*100):.1f}%")