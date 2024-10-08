import tkinter as tk
from tkinter import messagebox
import csv

#Inicialización de variables globales
keys = 'id_producto', 'nombre', 'precio', 'presentacion', 'cantidad'
id_siguiente = 0
ventas = 0
inventario = []

#Importa el archivo persistente csv
def importar_archivo_persistente():
    global keys
    global inventario
    global id_siguiente
    with open('inventario.csv', 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, keys)
        for row in lector_csv:
           inventario.append(row)
           print(row)
           id_siguiente += 1
    return inventario

#Crea un archivo persistente CSV
def crear_archivo_persistente():
    with open("inventario.csv", 'w', newline='') as archivo_csv:
        global keys
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames = keys)
        #escritor_csv.writeheader()

#Actualiza el archivo persistente CSV        
def actualizar_archivo_persistente(nuevo_producto):
    with open ("inventario.csv", 'a', newline = '' ) as archivo_csv:
        global keys
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames = keys)
        escritor_csv.writerow(nuevo_producto)

# Agrega un nuevo producto al Inventario
def agregar_producto(id_producto: int, nombre: str, precio: float, presentacion: str, cantidad: int, archivo_csv):
    global id_siguiente
    global keys
    global escritor_csv
    id_siguiente = int(id_siguiente)
    nuevo_producto = {
        'id_producto': id_producto.get(),
        'nombre': nombre.get(),
        'precio': float(precio.get()),
        'presentacion': presentacion.get(),
        'cantidad': int(cantidad.get())
    }
    for producto in inventario:
        if id_producto.get() == producto['id_producto']:
            id_siguiente+=1
            id_producto.insert(0, id_siguiente)
            messagebox.showwarning("Advertencia", "El ID del producto ya existe")
            return
    inventario.append(nuevo_producto)
    print(f'Producto {nuevo_producto['nombre']} agregado')
    for producto in inventario:
        print(producto['nombre'])
    listbox_inventario.insert(tk.END, f"{producto["nombre"]}: ${producto['precio']} (Cantidad: {producto['cantidad']})")
    id_siguiente += 1
    actualizar_archivo_persistente(nuevo_producto)
    limpiar_entradas()

#Limpia las entradas de texto del menú 
def limpiar_entradas():
    id_producto.delete(0, tk.END)
    nombre.delete(0, tk.END)
    precio.delete(0, tk.END)
    presentacion.delete(0, tk.END)
    cantidad.delete(0, tk.END)
    id_producto.insert(0, id_siguiente)
    
def vender_producto(id_producto, cantidad_vendida, inventario, ventas):
    for producto in inventario:
        if id_producto == producto['id_producto']:
            producto['cantidad'] -= cantidad_vendida
            ventas += producto['precio']*cantidad_vendida


def mostrar_inventario(inventario):
    for producto in inventario:
        print (f'{producto["nombre"]}, {producto["presentacion"]} unidades: {producto["cantidad"]}')

#Actualiza el inventario del listbox
def actualizar_inventario(inventario):
    listbox_inventario.delete(0, tk.END)
    for producto, detalles in productos.items():
        listbox_inventario.insert(tk.END, f"{producto}: ${detalles['precio']} (Cantidad: {detalles['cantidad']})")

try:
    inventario = importar_archivo_persistente()
except:
    crear_archivo_persistente()
#    inventario = crear_archivo_persistente()

#with open("inventario.csv", 'r+', newline='') as archivo_csv:

        
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Kiosco APP")
ventana.geometry('600x400')
#escritor_csv = csv.DictWriter(archivo_csv, fieldnames= keys)



# Crea entradas de texto
label_id_producto = tk.Label(ventana, text="ID Producto:")
label_id_producto.grid(row=0, column=0, padx=10, pady=10)
id_producto = tk.Entry(ventana)
id_producto.grid(row=0, column=1, padx=10, pady=10)
id_producto.insert(0, id_siguiente)

label_nombre = tk.Label(ventana, text="Nombre Producto:")
label_nombre.grid(row=2, column=0, padx=10, pady=10)
nombre = tk.Entry(ventana)
nombre.grid(row=2, column=1, padx=10, pady=10)

label_precio = tk.Label(ventana, text="Precio:")
label_precio.grid(row=3, column=0, padx=10, pady=10)
precio = tk.Entry(ventana)
precio.grid(row=3, column=1, padx=10, pady=10)


label_presentacion = tk.Label(ventana, text="Presentacion:")
label_presentacion.grid(row=4, column=0, padx=10, pady=10)
presentacion = tk.Entry(ventana)
presentacion.grid(row=4, column=1, padx=10, pady=10)


label_cantidad = tk.Label(ventana, text="Cantidad: ")
label_cantidad.grid(row=5, column=0, padx=10, pady=10)
cantidad = tk.Entry(ventana)
cantidad.grid(row=5, column=1, padx=10, pady=10)

# Crear Botonones
boton_agregar_producto = tk.Button(ventana, text="Agrega Producto", command = lambda: agregar_producto(id_producto, nombre, precio, presentacion, cantidad, inventario))
boton_agregar_producto.grid(row=6, column=1, padx=10, pady=10)

boton_mostrar_inventario = tk.Button(ventana, text="Mostrar Inventario", command = lambda: mostrar_inventario(inventario))
boton_mostrar_inventario.grid(row=8, column=1, padx=10, pady=10)

# Crear List Box
label_inventario = tk.Label(ventana, text="Inventario:")
label_inventario.grid(row=0, column=2)
listbox_inventario = tk.Listbox(ventana, width=40)
listbox_inventario.grid(row=1, column=2, rowspan=10, padx=10, pady=10, sticky='ns')

# Cargar Listbox precargada
for producto in inventario:
    print(producto['nombre'])
    listbox_inventario.insert(tk.END, f"{producto["nombre"]}: ${producto['precio']} (Cantidad: {producto['cantidad']})")

#Iniciar el bucle principal
ventana.mainloop()