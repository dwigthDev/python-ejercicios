#Vas a crear un programa en Python que gestione una lista de estudiantes. Cada estudiante tiene
#un nombre, una edad y una calificación. El programa debe permitir agregar nuevos estudiantes,
#actualizar la calificación de un estudiante, listar todos los estudiantes y guardar/cargar la lista de
#estudiantes desde un archivo en formato JSON

import json
import time 
lista_curso = [
    {
        "nombre": "carlitos",
        "edad": 14,
        "calificacion": 5.3
    }
]

def barra_de_carga(): #YO RECICLO CODIGO COMO SI FUERA PLASTICO XD
    print("\nCargando... pi pu pi pu")
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



def menu ():
        print("1.Agregar nuevo estudiante\n2.Actualizar_calificacion\n3.ver estudiantes\n4.guardar estudiantes\n5.cargar estudiantes\n6.salir")
        
#OPCION 1
def agregar_estudiante(lista_curso, nombre, edad, calificacion):
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "calificacion": calificacion 
    }
    lista_curso.append(estudiante)
    barra_de_carga()
    print("\n Alumno agregado correctamente :) \n")
    time.sleep(1)
    
#OPCION 2
def actualizar_calificacion(lista_curso, nombre, nota):
    for alumno in lista_curso:
            if alumno["nombre"] == nombre: #compara el nombre para ver si es la correcta
                barra_de_carga()
                alumno["calificacion"] = nota
                print("***Editado Correctamente*** \n")
                time.sleep(1)
                
#OPCION 3
def listar_estudiantes(lista_curso):
    barra_de_carga()
    if len(lista_curso) == 0:
        print("\nAun no hay tareas creadas\n")
    else:
        print(f"\nEn total tienes {len(lista_curso)} alumnos:\n")
        for alumno in lista_curso:
            print(f"Nombre del alumno: {alumno['nombre']}\n Edad: {alumno['edad']}\n calificacion: {alumno['calificacion']} \n")
            time.sleep(1)
            
#OPCION 4
def guardar_estudiantes(lista_curso):
    barra_de_carga()
    with open ("DB_Lista_curso.txt",'w') as database:
        lista = str(lista_curso)
        database.write(lista)
        print("\n***Guardado correctamente***\n")
        
#OPCION 5
def cargar_estudiantes():
    try:
        barra_de_carga()
        print("\n")
        with open('DB_Lista_curso.txt', 'r') as database:
            database = database.read()
            print(database)    
        print("\n")
    except FileNotFoundError:
        print("\nArchivo no encontrado... primero debe crear el archivo (opcion 4)\n")
        time.sleep(1)

def validarOpcion(opcion):
    if opcion == 1:
        try:
            nombre = str(input("ingresa el nombre del alumno: "))
            edad = int(input("ingresa la edad del alumno: "))
            calificacion = float(input("ingresa la calificacion del alumno: "))
            agregar_estudiante(lista_curso, nombre, edad, calificacion)
        except ValueError:
            print("ingrese el tipo de dato adecuado")
    elif opcion == 2:
        nombre = str(input("ingrea el nombre del alumno que quieres editar: "))
        nota = float(input("ingresa la nueva nota del alumno: "))
        actualizar_calificacion(lista_curso, nombre, nota)
    elif opcion == 3:
        listar_estudiantes(lista_curso)
    elif opcion == 4:
        guardar_estudiantes(lista_curso)
    elif opcion == 5:
        cargar_estudiantes()   
           
while True:
    menu()
    opcion = int(input("Ingresa la opcion que desees: "))
    validarOpcion(opcion)
