import random
import time

# Lista de usuarios
usuarios = [
    {
        "nombre": "santi",
        "id": 1,
        "contrasena": "ll",
        "peso": 60.0,
        "altura": 180,
        "rutinas": [  # es una lista ya que pueden ser varias las rutinas de cada usuario
            {
                "titulo": "día de pecho",  # cada rutina se conforma por su título(str) y los ejercicios (list)
                "ejercicios": [
                    {"nombre": "curl de bíceps", "peso": 22, "repeticiones": 12, "series": 4},
                    {"nombre": "press banca", "peso": 150, "repeticiones": 10, "series": 4},
                    {"nombre": "press militar", "peso": 37, "repeticiones": 8, "series": 4}
                ],
                "cantidad": 3
            }
        ]
    }
]

# Función para crear ejercicios
def crearEjercicios(cantidad_ejercicios):
    lista_de_ejercicios = []
    for i in range(cantidad_ejercicios):
        nombre = str(input(f"Ingresa el nombre del ejercicio {i+1}\n---> "))
        peso = int(input(f"Ingresa la cantidad de peso en kg para {nombre} (únicamente debes agregar el número entero)\n---> "))
        repeticiones = int(input(f"Ingresa la cantidad de repeticiones para {nombre}\n---> "))
        series = int(input(f"Ingresa la cantidad de series para {nombre}\n---> "))  # Convertimos series a int
        constructor = {
            "nombre": nombre,
            "peso": peso,
            "repeticiones": repeticiones,
            "series": series
        }
        lista_de_ejercicios.append(constructor)
    return lista_de_ejercicios

# Función para crear una rutina
def crearRutina(usuario):
    titulo_rutina = str(input("Ingresa el nombre de tu rutina.\n---> "))
    cantidad_ejercicios = int(input("Ingresa la cantidad de ejercicios para tu rutina.\n---> "))
    ejercicios = crearEjercicios(cantidad_ejercicios)
    rutina = {
        "titulo": titulo_rutina,
        "ejercicios": ejercicios,
        "cantidad": cantidad_ejercicios
    }
    usuario["rutinas"].append(rutina)
    print(f"\nRutina agregada exitosamente: {usuario['rutinas']}\n")

# Función para imprimir las rutinas
def imprimirRutina(usuario):
    if not usuario["rutinas"]:
        print("No tienes rutinas guardadas.")
    else:
        for idx, rutina in enumerate(usuario["rutinas"], start=1):
            print(f"Rutina {idx}: {rutina['titulo']}")
            for ejercicio in rutina["ejercicios"]:
                print(f"  - {ejercicio['nombre']}: {ejercicio['peso']}kg, {ejercicio['repeticiones']} reps, {ejercicio['series']} series")

# Función para usar una rutina
def usarRutina(usuario):
    cant_rutinas = len(usuario["rutinas"])
    if cant_rutinas == 0:
        op = int(input("Aún no tienes ninguna rutina creada hasta el momento\nSi desea crear una rutina ingrese 1, si desea volver ingrese cualquier otro número\n---> "))
        if op == 1:
            crearRutina(usuario)
        else:
            print("Regresando al menú...")
    else:
        op = int(input("Si desea ver todas las rutinas creadas hasta el momento ingrese 1, si desea buscar una rutina por su nombre ingrese 2\n---> "))
        if op == 1:
            print("Tus rutinas son:\n")
            imprimirRutina(usuario)
        elif op == 2:
            nombre_rutina = str(input("Ingrese el nombre de la rutina que busca:\n---> "))
            for rutina in usuario["rutinas"]:
                if rutina["titulo"].lower() == nombre_rutina.lower():
                    print(f"Rutina encontrada: {rutina['titulo']}")
                    for ejercicio in rutina["ejercicios"]:
                        print(f"  - {ejercicio['nombre']}: {ejercicio['peso']}kg, {ejercicio['repeticiones']} reps, {ejercicio['series']} series")
                    break
            else:
                print("Rutina no encontrada.")

# Segunda parte del código (una vez registrado el usuario podrá usar todas las funciones)
def opciones_de_usuario(usuario):
    while True:
        try:
            print(f"\nBienvenido, {usuario['nombre']}!")
            op = int(input(f"Ingrese la opción que desea ejecutar\n1. Crear una rutina\n2. Usar una rutina\n3. Salir\n---> "))
            if op == 1:
                crearRutina(usuario)
            elif op == 2:
                usarRutina(usuario)
            elif op == 3:
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        except ValueError:
            print("Ha ocurrido un error... asegúrese de ingresar solo números '1', '2' o '3'.")

# Primera parte del código (registrar usuarios y login de usuarios)
def crearUsuario():
    id_usuario = random.randint(1, 1000)
    nombre_usuario = str(input("Ingresa tu nombre de usuario.\n---> "))
    contrasena_usuario = str(input("Ingresa tu contraseña.\n---> "))
    peso_usuario = float(input("Para poder hacer un seguimiento adecuado de tu progreso necesitamos tu peso en kilogramos, ingresa solo el número (ejemplo: 70 o 70.5).\n---> "))
    altura_usuario = int(input("También necesitaremos tu altura en cm (ejemplo 170).\n---> "))
    constructor = {
        "nombre": nombre_usuario,
        "id": id_usuario,
        "contrasena": contrasena_usuario,
        "peso": peso_usuario,
        "altura": altura_usuario,
        "rutinas": []  # Cambié "rutina" a "rutinas"
    }
    usuarios.append(constructor)
    print("\nUsuario creado correctamente, ahora podrás iniciar sesión.\n")
    time.sleep(1)

# Función para ingresar (login de usuarios)
def ingresar():
    usuario = str(input("Ingresa el nombre de usuario.\n---> "))
    contrasena = str(input("Ingresa la contraseña.\n---> "))
    for elemento in usuarios:
        if elemento["nombre"] == usuario and elemento["contrasena"] == contrasena:
            print("\nHas ingresado correctamente.\n")
            time.sleep(1)
            opciones_de_usuario(elemento)
            break
    else:
        print("Usuario no encontrado, verifique los datos e intente nuevamente.")

# Menú principal
def menu():
    while True:
        try:
            op = int(input("Bienvenido a Gym Tracker!!!\nIngrese la opción que desea ejecutar:\n1. Ingresar\n2. Registrarse\n3. Salir\n---> "))
            if op == 1:
                ingresar()
            elif op == 2:
                crearUsuario()
            elif op == 3:
                print("Saliendo de Gym Tracker. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        except ValueError:
            print("Ha ocurrido un error")
menu()
