import string
import random
def generar(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for i in range (longitud))
    print("Tu contraseña es:", contraseña)
print("Bienvenidos al generador de contraseñas... \npara continuar ingrese la longitud de tu contraseña")
while True:
    try:
        longitud = int(input("---> "))
        generar(longitud)
    except ValueError:
        print("Asegurese de ingresar un numero ")