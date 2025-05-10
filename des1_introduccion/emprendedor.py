## utilidades= P*U-PG donde P es precio suscripcion, U es numero de usuarios y PG es gastos totales

p=int(input("ingrese precio de suscrpición : $"))
u=int(input("ingrese numero de usuarios:"))
gt=int(input("ingrese gastos totales : $"))

uti=p*u-gt

print(f"las utilidades son: ${uti}")