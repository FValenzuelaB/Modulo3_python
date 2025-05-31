import sys

# Diccionario de artículos y precios en dólares
precios = {
    'Notebook': 700,
    'Teclado': 30,
    'Mouse': 12,
    'Monitor': 250,
    'Escritorio': 135,
    'Tarjeta de Video': 1500
}

def filtro(precios: dict[str, int], umbral: int):
    if len(sys.argv) >= 3:
        criterio = str(sys.argv[2]).lower().strip()
    else:
        criterio = "mayor"

    if criterio == "mayor":
        return f"Los productos con precios mayores al umbral son: {[k for k, v in precios.items() if v > umbral]}"
    elif criterio == "menor":
        return f"Los productos con precios menores al umbral son: {[k for k, v in precios.items() if v < umbral]}"
    else:
        raise ValueError(f"\nEl criterio ingresado es incorrecto: '{sys.argv[2]}'. Usa 'mayor' o 'menor'")

try:
    if len(sys.argv) < 2:
        raise ValueError("Debes ingresar al menos un umbral de precio como argumento.")
    
    umbral = int(sys.argv[1])
    resultado = filtro(precios, umbral)
    print("Artículos filtrados:", resultado)

except Exception as e:
    print("Error:", e)
