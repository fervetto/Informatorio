lista_tareas = [{'id_tarea' : '0', 'nombre': 'estudiar', 'completada': False},
                {'id_tarea' : '1', 'nombre': 'cocinar', 'completada': False},
                {'id_tarea' : '2', 'nombre': 'trabajar', 'completada': False}]



# Funcion que muestra las opciones disponibles para el usuario.
def mostrar_menu():
    while True:
        print('\nOpciones:')
        print('1. Agregar tarea')
        print('2. Marcar tarea completada')
        print('3. Eliminar Tarea')
        print('4. Mostrar lista de tareas')
        print('5. Salir')
        opcion = input('Seleccione una opcion: ')
        return opcion

#Funcion que añade una nueva tarea a la lista
def agregar_tarea(lista_tareas):
    nueva_tarea = {'id_tarea' : '001', 'nombre': 'estudiar', 'completada': False}
    nueva_tarea['id_tarea'] = str(len(lista_tareas))
    nueva_tarea['nombre'] = input("ingrese el nombre de la nueva tarea: ")
    lista_tareas.append(nueva_tarea)
    return lista_tareas

#Funcion que marca una tarea como completada utilizando su ID
def marcar_completada(lista_tareas, id_tarea):
    for tarea in lista_tareas:
        if tarea['id_tarea'] == id_tarea:
            tarea['completada'] = True
    return lista_tareas

#Función que muestra todas las tareas con su estado (completada o pendiente)
def eliminar_tarea(lista_tareas, id_tarea):
    for tarea in lista_tareas:
        if tarea['id_tarea'] == id_tarea:
            lista_tareas.remove(tarea)
    return lista_tareas

def mostrar_tareas(lista_tareas):
    print('\nLista de tareas: ')
    for tarea in lista_tareas:
        print('\n', tarea['nombre'], ': ')
        if tarea['completada']:
            print ('Completada')
        else:
            print ('Pendiente')
        

opcion = mostrar_menu()
while True:
    if opcion == '1':
        agregar_tarea(lista_tareas)
    elif opcion == '2':
        id_tarea = input('ingrese la id de la tarea: ')
        marcar_completada(lista_tareas, id_tarea)
    elif opcion == '3':
        id_tarea = input('ingrese la id de la tarea: ')
        eliminar_tarea(lista_tareas, id_tarea)
    elif opcion == '4':
        mostrar_tareas(lista_tareas)
    elif opcion == '5':
        break        
    opcion = mostrar_menu()
for tarea in lista_tareas:
    print(tarea)
