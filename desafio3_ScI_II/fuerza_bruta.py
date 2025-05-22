from string import ascii_lowercase
import getpass


try:
    intentos=0
    password=getpass.getpass("Ingrese su clave:   ")
    adivinadas=""

    for i in range(len(password)):
        for j in ascii_lowercase:
            intentos+=1
            if j==password[i]:
                adivinadas+=j
                break
    print(f"Se adivinó la pass: {password} en {intentos} intentos.")

except Exception as e:
    print("no se pudo procesar su clave", e)