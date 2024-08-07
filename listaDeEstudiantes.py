#Vas a crear un programa en Python que gestione una lista de estudiantes. Cada estudiante tiene
#un nombre, una edad y una calificación. El programa debe permitir agregar nuevos estudiantes,
#actualizar la calificación de un estudiante, listar todos los estudiantes y guardar/cargar la lista de
#estudiantes desde un archivo en formato JSON
import time 
lista_curso = [
    {
        "nombre": "carlitos",
        "edad": 14,
        "calificacion": 5.3
    }
]

def barra_de_carga(): #Este bloque de codigo es una barra de carga
    print("\nCargando...")
    tiempo_inicio = time.time()
    tiempo_actual = time.time()
    while tiempo_actual - tiempo_inicio < 2:
        tiempo_transcurrido = tiempo_actual - tiempo_inicio
        porcentaje = int((tiempo_transcurrido / 2) * 100)
        barra = '[' + '=' * porcentaje + ' ' * (100 - porcentaje) + ']'
        print(f'\r{barra} {porcentaje}%', end='', flush=True)
        tiempo_actual = time.time()
        time.sleep(0.1)  # ajusta la velocidad de actualización de la barra de carga

    # Imprimir la barra de carga completa al 100%
    print('\r[' + '=' * 100 + '] 100%')

#OPCION 1
def agregar_estudiante(lista_curso, nombre, edad, calificacion): #se crea un diccionaro que representa a un estudiante y se guarda en la lsita de estudiantes
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion 
    }
    lista_curso.append(estudiante)
    barra_de_carga()
    print("\n Alumno agregado correctamente :) \n") #mensaje de confirmacion 
    time.sleep(1)
    
#OPCION 2
def actualizar_calificacion(lista_curso, nombre, nota):
    for alumno in lista_curso: #compara el nombre del alumno y al encontrarlo le modifica la nota
            if alumno["nombre"] == nombre:
                barra_de_carga()
                alumno["calificacion"] = nota
                print("***Editado Correctamente*** \n")
                time.sleep(1)
                
#OPCION 3
def listar_estudiantes(lista_curso):
    barra_de_carga()
    if len(lista_curso) == 0: # verifica que si no hay tareas creadas
        print("\nAun no hay tareas creadas\n")
    else:
        print(f"\nEn total tienes {len(lista_curso)} alumnos:\n") #por medio del FOR imprime en plantalla cada uno de los estudiantes 
        for alumno in lista_curso:
            print(f"Nombre del alumno: {alumno['nombre']}\n Edad: {alumno['edad']}\n calificacion: {alumno['calificacion']} \n")
            time.sleep(1)
            
#OPCION 4
def guardar_estudiantes(lista_curso):
    barra_de_carga()
    with open ("DB_Lista_curso.txt",'w') as database: #crea un archivo TXT y escribe sobre el los datos de los estudiantes
        lista = str(lista_curso)
        database.write(lista)
        print("\n***Guardado correctamente***\n")
        
#OPCION 5
def cargar_estudiantes():
    try:
        barra_de_carga()
        print("\n")
        with open('DB_Lista_curso.txt', 'r') as database: #Toma el archivo anteriormente creado y lo imprime en pantalla
            database = database.read()
            print(database)    
        print("\n")
    except FileNotFoundError: #si no encuentra el archivo saldra error
        print("\nArchivo no encontrado... primero debe crear el archivo (opcion 4)\n")
        time.sleep(1)

def menu ():
        print("1.Agregar nuevo estudiante\n2.Actualizar_calificacion\n3.ver estudiantes\n4.guardar estudiantes\n5.cargar estudiantes\n6.salir")

while True:
    menu()
    opcion = int(input("Ingresa la opcion que desees: "))
    if opcion == 1:
        try:
            nombre = str(input("ingresa el nombre del alumno: ")).strip()
            edad = int(input("ingresa la edad del alumno: "))
            calificacion = float(input("ingresa la calificacion del alumno: "))
            agregar_estudiante(lista_curso, nombre, edad, calificacion)
        except ValueError:
            print("ingrese el tipo de dato adecuado")
    elif opcion == 2:
        nombre = str(input("ingrea el nombre del alumno que quieres editar: ")).strip()
        nota = float(input("ingresa la nueva nota del alumno: "))
        actualizar_calificacion(lista_curso, nombre, nota)
    elif opcion == 3:
        listar_estudiantes(lista_curso)
    elif opcion == 4:
        guardar_estudiantes(lista_curso)
    elif opcion == 5:
        cargar_estudiantes() 
    elif opcion == 6:
        print("saliendo del programa...")
        time.sleep(1)
        print("fin del programa")
        break
