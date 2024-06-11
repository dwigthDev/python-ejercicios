1) Ejercicio: Gestor de Tareas
Descripción
Vamos a crear un programa en Python que gestione una lista de tareas. Cada tarea tiene un título,
una descripción y un estado (pendiente o completada). El programa debe permitir agregar nuevas
tareas, marcar tareas como completadas, listar todas las tareas y guardar/cargar las tareas desde
un archivo en formato JSON.
Requisitos
Lista de Tareas: Usa una lista para almacenar las tareas. Cada tarea debe ser un diccionario con las
siguientes claves:
 "titulo": El título de la tarea.
 "descripcion": Una breve descripción de la tarea.
 "estado": El estado de la tarea, que puede ser "pendiente" o "completada".
Funciones:
 agregar_tarea(tareas, titulo, descripcion): Agrega una nueva tarea a la lista de tareas.
 marcar_completada(tareas, titulo): Marca una tarea como completada por su título.
 listar_tareas(tareas): Imprime todas las tareas con su estado.
 guardar_tareas(tareas, nombre_archivo): Guarda la lista de tareas en un archivo JSON.
 cargar_tareas(nombre_archivo): Carga las tareas desde un archivo JSON y devuelve la lista
de tareas.
Archivo JSON: Usa la biblioteca json para guardar y cargar las tareas en un archivo JSON
