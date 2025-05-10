## utilidades= P*U-PG donde P es precio suscripcion, U es numero de usuarios y PG es gastos totales

pn=int(input("ingrese precio de suscrpición normal: $"))
un=int(input("ingrese numero de usuarios normales:"))

pp=pn*1.5
up=int(input("ingrese numero de usuarios premium:"))

gt=int(input("ingrese gastos totales : $"))

uti=pn*un+pp*up-gt

print(f"las utilidades son: ${uti:.0f}")