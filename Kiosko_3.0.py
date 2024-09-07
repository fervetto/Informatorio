import tkinter as tk
from tkinter import messagebox
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
    global escritor_csv
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

#Actualiza el inventario del listbox
def actualizar_inventario(inventario):
    listbox_inventario.delete(0, tk.END)
    for producto, detalles in productos.items():
        listbox_inventario.insert(tk.END, f"{producto}: ${detalles['precio']} (Cantidad: {detalles['cantidad']})")

#Limpia las entradas de texto del menú 
def limpiar_entradas():
    id_producto.delete(0, tk.END)
    nombre.delete(0, tk.END)
    precio.delete(0, tk.END)
    presentacion.delete(0, tk.END)
    cantidad.delete(0, tk.END)
    id_producto.insert(0, id_siguiente)

def eliminar_producto():
    seleccionado = listbox_inventario.curselection()
    if seleccionado:
        indice = seleccionado[0]
        listbox_inventario.delete(indice)
        del inventario[indice]
        limpiar_entradas()
        messagebox.showinfo("Información", "Producto eliminado exitosamente")
    else:
        messagebox.showerror("Error", "Selecciona un producto para eliminar")

def cargar_producto_para_editar(event):
    seleccionado = listbox_inventario.curselection()
    if seleccionado:
        indice = seleccionado[0]
        producto = inventario[indice]
        
        id_producto.delete(0, tk.END)
        id_producto.insert(0, producto['id_producto'])
        
        nombre.delete(0, tk.END)
        nombre.insert(0, producto['nombre'])
        
        precio.delete(0, tk.END)
        precio.insert(0, producto['precio'])
        
        presentacion.delete(0, tk.END)
        presentacion.insert(0, producto['presentacion'])
        
        cantidad.delete(0, tk.END)
        cantidad.insert(0, producto['cantidad'])

def editar_producto():
    seleccionado = listbox_inventario.curselection()
    if seleccionado:
        indice = seleccionado[0]
        inventario[indice] = {
            'id_producto': id_producto.get(),
            'nombre': nombre.get(),
            'precio': float(precio.get()),
            'presentacion': presentacion.get(),
            'cantidad': int(cantidad.get())
        }
        
        listbox_inventario.delete(indice)
        listbox_inventario.insert(indice, f"{inventario[indice]['id_producto']}: {inventario[indice]['nombre']} - ${inventario[indice]['precio']} (Cantidad: {inventario[indice]['cantidad']})")
        limpiar_entradas()
        messagebox.showinfo("Información", "Producto editado exitosamente")
    else:
        messagebox.showerror("Error", "Selecciona un producto para editar")

def vender_producto():
    seleccionado = listbox_inventario.curselection()
    if seleccionado:
        indice = seleccionado[0]
        producto = inventario[indice]
        
        if producto['cantidad'] > 0:
            producto['cantidad'] -= 1
            listbox_inventario.delete(indice)
            listbox_inventario.insert(indice, f"{producto['id_producto']}: {producto['nombre']} - ${producto['precio']} (Cantidad: {producto['cantidad']})")
            messagebox.showinfo("Información", f"Se vendió 1 unidad de {producto['nombre']}")
        else:
            messagebox.showwarning("Advertencia", "No hay suficiente stock para vender")
    else:
        messagebox.showerror("Error", "Selecciona un producto para vender")

def buscar_producto():
    query = nombre.get().lower()
    resultados = [p for p in inventario if query in p['nombre'].lower() or query == p['id_producto']]
    listbox_inventario.delete(0, tk.END)
    if resultados:
        for producto in resultados:
            listbox_inventario.insert(tk.END, f"{producto['id_producto']}: {producto['nombre']} - ${producto['precio']} (Cantidad: {producto['cantidad']})")
    else:
        messagebox.showinfo("Sin resultados", "No se encontró ningún producto con ese nombre o ID.")

def mostrar_inventario():
    for producto in inventario:
        print(f"{producto['nombre']}, {producto['presentacion']} unidades: {producto['cantidad']}")


# Programa Principal

try:
    inventario = importar_archivo_persistente()
except:
    crear_archivo_persistente()
    
    #Crear la ventana principal
ventana = tk.Tk()
ventana.title("Kiosco APP")
ventana.geometry('600x400')

# Crear entradas de texto
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

label_presentacion = tk.Label(ventana, text="Presentación:")
label_presentacion.grid(row=4, column=0, padx=10, pady=10)
presentacion = tk.Entry(ventana)
presentacion.grid(row=4, column=1, padx=10, pady=10)

label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.grid(row=5, column=0, padx=10, pady=10)
cantidad = tk.Entry(ventana)
cantidad.grid(row=5, column=1, padx=10, pady=10)

# Crear Botones
boton_agregar_producto = tk.Button(ventana, text="Agregar Producto", command=lambda: agregar_producto(id_producto, nombre, precio, presentacion, cantidad, inventario))
boton_agregar_producto.grid(row=6, column=0, padx=10, pady=10)

boton_editar_producto = tk.Button(ventana, text="Editar Producto", command=editar_producto)
boton_editar_producto.grid(row=6, column=1, padx=10, pady=10)

boton_eliminar_producto = tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto)
boton_eliminar_producto.grid(row=7, column=0, padx=10, pady=10)

boton_vender_producto = tk.Button(ventana, text="Vender Producto", command=vender_producto)
boton_vender_producto.grid(row=7, column=1, padx=10, pady=10)

boton_mostrar_inventario = tk.Button(ventana, text="Mostrar Inventario", command=mostrar_inventario)
boton_mostrar_inventario.grid(row=8, column=0, padx=10, pady=10)

boton_buscar_producto = tk.Button(ventana, text="Buscar Producto", command=buscar_producto)
boton_buscar_producto.grid(row=8, column=1, padx=10, pady=10)


# Crear ListBox
label_inventario = tk.Label(ventana, text="Inventario:")
label_inventario.grid(row=0, column=2)
listbox_inventario = tk.Listbox(ventana, width=40)
listbox_inventario.grid(row=1, column=2, rowspan=12, padx=10, pady=10, sticky='ns')

# Cargar Listbox precargada
for producto in inventario:
    print(producto['nombre'])
    listbox_inventario.insert(tk.END, f"{producto["nombre"]}: ${producto['precio']} (Cantidad: {producto['cantidad']})")

# Asociar evento de clic en el Listbox
listbox_inventario.bind("<<ListboxSelect>>", cargar_producto_para_editar)

# Iniciar el bucle principal
ventana.mainloop()
