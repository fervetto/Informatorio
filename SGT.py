""" Ejercicio: Sistema de Gestión de Tareas
Crea un programa simple que funcione como un sistema de gestión de tareas. 
El programa permitirá a los usuarios añadir tareas, marcar tareas como completadas, eliminar tareas y ver la lista de tareas. 
Usaremos funciones para organizar el código y facilitar la reutilización."""

"""Requisitos

• Utiliza una lista para almacenar las tareas. Cada tarea será representada con los siguientes campos:
• id: un número único que identifica la tarea.
• nombre: una cadena que describe la tarea.
• completada: un booleano que indica si la tarea está completada."""

# Funciones:
# mostrar_menu(): Muestra las opciones disponibles para el usuario.

def mostrar_menu():
    print("\nSistema de Gestión de tareas")
    print("Elige una opcion: ")
    print("1. Agregar tarea")
    print("2. Marcar tarea completada")
    print("3. Mostrar lista de tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

# agregar_tarea(lista_tareas): Añade una nueva tarea a la lista.

def agregar_tarea(lista_tareas, contador_id):
    nombre = input("Ingrese una tarea: ")
    completada = False
    lista_tareas.append({"id": contador_id, "nombre": nombre, "completada": completada})
    print("Tarea agregada")
    return contador_id + 1

# marcar_completada(lista_tareas, id_tarea): Marca una tarea como completada usando su ID.

def marcar_completada(lista_tareas, id_tarea):
    for tarea in lista_tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            print("Tarea completada")
            return
    print("Tarea no encontrada")

# eliminar_tarea(lista_tareas, id_tarea): Elimina una tarea de la lista usando su ID.

def eliminar_tarea(lista_tareas, id_tarea):
    for tarea in lista_tareas:
        if tarea["id"] == id_tarea:
            lista_tareas.remove(tarea)
            print("Tarea eliminada")
            return
    print("Tarea no encontrada")
# mostrar_tareas(lista_tareas): Muestra todas las tareas con su estado (completada o pendiente).

def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas en la lista")
        return
    print("lista de tareas: ")
    for tarea in lista_tareas:
            estado = "completada" if tarea["completada"] else "pendiente"
            print(f"Id:{tarea['id']}, Nombre:{tarea['nombre']}, Estado:{estado}")

def main():
              
    lista_tareas = []
    contador_id = 1
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
             contador_id = agregar_tarea(lista_tareas, contador_id)
        elif opcion == '2':
            id_tarea = int(input("Ingrese el id de la tarea completada: "))
            marcar_completada(lista_tareas, id_tarea)
        elif opcion == '3':
              mostrar_tareas(lista_tareas)
        elif opcion == '4':
          id_tarea = int(input("Ingrese el id de la tarea que desea eliminar: "))
          eliminar_tarea(lista_tareas, id_tarea)
        elif opcion == '5':
            print("Programa terminado")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
