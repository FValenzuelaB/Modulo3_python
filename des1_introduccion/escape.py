import math as m

#Velocidad de escape

r=int(input("Ingrese radio del planeta en metros: "))
g=float(input("Ingrese aceleración de gravedad como decimal: "))

v=m.sqrt(2*r*g)
vkm=v/1000
print (f"La velocidad de escape del planeta es de {v:.1f} m/s o {vkm:.2f} km/s")