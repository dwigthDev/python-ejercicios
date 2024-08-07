#Vamos a crear un programa en Python que gestione una lista de tareas. Cada tarea tiene un título,
#una descripción y un estado (pendiente o completada). El programa debe permitir agregar nuevas
#tareas, marcar tareas como completadas, listar todas las tareas y guardar/cargar las tareas desde
#un archivo en formato JSON
import time
import json
lista_de_tareas = [

]
#esto solo sirve para una animacion bonita (si, se la pedi chatgpt) 
def barra_de_carga():
    print("\nCargando... ")
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
        print("1.agregar nueva tarea\n2.marcar tarea completada\n3.ver tareas\n4.guardar tareas\n5.cargar tareas\n6.salir")



def agregar_tarea(lista_de_tareas, nombre, desc):
    tarea = {
        "titulo": nombre,
        "descripcion": desc,
        "estado": 'pendiente' #por defecto viene en pendiente
    }
    lista_de_tareas.append(tarea)
    barra_de_carga()
    print("\n Tarea agregada correctamente :) \n")
    time.sleep(1)

def marcar_completada(lista_de_tareas, nombre):
    barra_de_carga()
    for tarea in lista_de_tareas:
        if tarea["titulo"] == nombre: #compara el nombre para ver si es la correcta
            tarea["estado"] = "Realizada"
            print("***Editada Correctamente*** \n")
            time.sleep(1)
            return
    print("\nTarea no encontrada\n")
    time.sleep(1)

def listar_tareas(lista_de_tareas):
    barra_de_carga()
    if len(lista_de_tareas) == 0: #verifica si hay al menos una tarea
        print("\nAun no hay tareas creadas\n")
    else:
        print(f"\nEn total tienes {len(lista_de_tareas)} tareas:\n")
        for tarea in lista_de_tareas:    #imprime en pantalla las tareas
            print(f"Nombre de la tarea: {tarea['titulo']}\n Descripcion: {tarea['descripcion']}\n Estado: {tarea['estado']} \n")
            time.sleep(1)
        print("***Fin del listado*** \n")

def guardar_tareas(lista_de_tareas): #con esta funcion se genera un archivo JSON que guarda los datos
    barra_de_carga()
    with open ("DB_Listas.json",'w') as database:
        json.dump(lista_de_tareas, database, indent=4)
        print("\n***Guardado correctamente***\n")


def cargar_tareas():#esta funcion se encarga de leer el archivo generado 
    try:
        barra_de_carga()
        print("\n")
        with open ("DB_Listas.json",'r') as database:
            print(json.load(database))
        print("\n")
    except FileNotFoundError:
        print("\narchivo no encontrado... primero debe crear el archivo (opcion 4)\n")
        time.sleep(1)
        

while True:
    menu()
    opcion = int(input("Ingresa la opcion que desees: "))
    if opcion == 1:
        nombre = str(input("ingresa el nombre de la tarea: ")).strip()
        desc = str(input("ingresa la descripcion de la tarea: ")).strip()
        agregar_tarea(lista_de_tareas, nombre, desc)
    elif opcion == 2:
        nombre = str(input("ingrea el nombre de la tarea que deseas marcar como completa: ")).strip()
        marcar_completada(lista_de_tareas, nombre)
    elif opcion == 3:
        listar_tareas(lista_de_tareas)
    elif opcion == 4:
        guardar_tareas(lista_de_tareas)
    elif opcion == 5:
        cargar_tareas()         
    elif opcion == 6:
        print("saliendo del programa...")
        time.sleep(1)
        print("fin del programa")
        break
