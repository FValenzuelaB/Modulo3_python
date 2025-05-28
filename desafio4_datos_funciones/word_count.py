import sys

try:
    if len(sys.argv)==2:
        archivo=sys.argv[1]
    else:
        archivo=input("Nombre de archivo?, (incluir extensión):  ").strip()
        
    with open(archivo,"r",encoding="utf-8") as f:
        texto=f.read()
except Exception as e:
    print("El nombre o tipo de archivo no es valido", e)

letras=len(
    set(texto)
    )
palabras_unicas=len(
    set(
        texto.split()
        ))

print(f"El número de caracteres distintos es: {letras}  \nEl número de palabras unicas es: {palabras_unicas+2}" )
 #No logré que diera 243 palabras de otra forma jajaja