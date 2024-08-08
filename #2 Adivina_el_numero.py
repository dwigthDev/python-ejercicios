#importacion de la libreria "ramdom"
import random
import time
repeticion = 1
contador = 0
numero = 0
#esta funcion es la que logra generar un numero aleatorio y a la vez verificar si es par par 
def generador():
    global repeticion #declara la variable 'repeticion' como global y que se pueda cambiar el valor mas adelante
    global numero
    while repeticion == 1:
        numero = random.randint(1, 100)
        if numero % 2 == 0:
            repeticion = 2 #si el numero es par rompe el bucle
        else:
            numero = random.randint(1, 100) #si el numero no es par genera otro numero
            
#esta funcion configura el tipo de dificultadad
def lectorDificultad(dificultad):
    global vidas
    if dificultad == 1:
        vidas = 10
    elif dificultad == 2:
        vidas = 8
    elif dificultad == 3:
        vidas = 5
        
#esta funcion valida y muestra el mensaje en pantalla, segun la eleccion del usuario
def validacion(eleccion):
    global contador
    global vidas
    if eleccion > numero:
        vidas = vidas - 1
        contador =+ 1
        print(f'Tu número es mayor al buscado, te quedan {vidas}')
    elif eleccion < numero :
        vidas = vidas - 1
        contador =+ 1
        print(f'Tu número es menor al buscado, te quedan {vidas}')
    elif eleccion == numero:
        print(f'Felicidades {nombre_usuario} {apellido_usuario} has acertado con {contador}')
        
    if vidas == 0:
        print(f'Lo siento {nombre_usuario} {apellido_usuario} No lograste adivinar el número en nivel {dificultad} \n el numero buscado era {numero}')
        

#Aqui comienza el juego
print("bienvenido, el juego consiste en adivinar un numero aleatorio el cual sera generado por la computadora") 
time.sleep(1)
nombre_usuario = input("para empezar ingresa tu nombre: ")
apellido_usuario = input("Ahora ingresa tu apellido: ")
while repeticion == 1:
    try:
        dificultad = int(input("""elije la dificultad:
                                ingresa "1" para facil   (10 intentos)
                                ingresa "2" para medio   (8 intentos)
                                ingresa "3" para dificil (5 intentos)
                                Ingresa un Valor: """))
        if dificultad >= 1 and dificultad <=3:
            lectorDificultad(dificultad)
            while vidas != 0:
                eleccion = int(input(f'elejiste la dificultad {dificultad} y tienes {vidas} vidas, ingresa un numero par: '))
                if eleccion % 2 == 0:
                    validacion(eleccion)
                else:
                    print("Tu número no es par,ingresa nuevamente ")
        else:
            print('invalido, el numero debe ser 1, 2 o 3')
            
    except ValueError:
            print("valor no valido, debe ser un numero entero")
            
            
            #pendiente: validar si eljugador quiere seguir tras perder 
        
