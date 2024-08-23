import tkinter as tk
contador_id=0
lista_tareas = []


def agregar_tarea(lista_tareas, nombre, contador_id):
    completada = False
    lista_tareas.append({"id": contador_id, "nombre": nombre.get(), "completada": False})
    print(lista_tareas[contador_id])
    mostrar_texto('Tarea Agregada')
    contador_id += 1
    print(contador_id)
    #ventana_agregar_tarea.destroy()

    return

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





ventana = tk.Tk()
ventana.geometry('600x600')
ventana.title('Gestor de Tareas')

def mostrar_texto(entrada):
    etiqueta = tk.Label(ventana_agregar_tarea, text="Ingrese el Nombre de la Nueva Tarea")
    etiqueta.pack(pady=10)
    texto = 'Tarea agregada'
    etiqueta.config(text=f"Texto ingresado: {texto}")


def abrir_ventana_agregar_tarea():
    # Crear una ventana Agregar Tarea
    global ventana_agregar_tarea
    ventana_agregar_tarea = tk.Toplevel()
    ventana_agregar_tarea.title("Agregar Tarea")
    ventana_agregar_tarea.geometry("300x200")

    # Crear un botón dentro de la ventana agregar_tarea para cerrarla
    boton_cerrar = tk.Button(ventana_agregar_tarea, text="Cerrar ventana", command=ventana_agregar_tarea.destroy)
    boton_cerrar.pack(pady=20)
    
    
    # Crear una etiqueta para mostrar el texto ingresado
    etiqueta = tk.Label(ventana_agregar_tarea, text="Ingrese el Nombre de la Nueva Tarea")
    etiqueta.pack(pady=10)
 
    # Crear un cuadro de entrada
    entrada = tk.Entry(ventana_agregar_tarea, width=40)
    entrada.pack(pady=10)
    boton = tk.Button(ventana_agregar_tarea, text="Agregar", command=lambda: agregar_tarea(lista_tareas, entrada, contador_id))
    boton.pack(pady=10)




# Crear un botón dentro de la ventana principal para abrir la ventana agregar_tareaabrir_ventana_agregar_tarea
boton_abrir = tk.Button(ventana, text="Agregar Tarea", command=abrir_ventana_agregar_tarea)
boton_abrir.pack(pady=20)





botonAgregarTarea = tk.Button(ventana, text='Agregar Tarea', font=('Arial', 20), command= lambda: agregar_tarea(lista_tareas, 'Ejemplo'))
botonAgregarTarea.pack()

ventana.mainloop()