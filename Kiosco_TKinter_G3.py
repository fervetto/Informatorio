import tkinter as tk

ventas = 0
inventario = []
productos = {
    'id_producto': '',
    'nombre' : '',
    'precio' : '',
    'presentación' : '',
}

def agregar_producto(id_producto: int, nombre: str, precio: float, presentación: str, cantidad: int):
    nuevo_producto = {'id_producto' : id_producto, 'nombre' : nombre.get(), 'precio' : precio.get(),
                      'presentacion': presentación.get(), 'cantidad' : cantidad.get()}
    inventario.append(nuevo_producto)
    print(f'Producto {nuevo_producto['nombre']} agregado')
    for producto in inventario:
        print(producto['nombre'])
    
def vender_producto(id_producto, cantidad_vendida, inventario, ventas):
    for producto in inventario:
        if id_producto == producto['id_producto']:
            producto['cantidad'] -= cantidad_vendida
            ventas += producto['precio']*cantidad_vendida
            
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Kiosco APP")
ventana.geometry('600x600')


# Crea entradas de texto
label_id_producto = tk.Label(ventana, text="ID Producto:")
label_id_producto.grid(row=0, column=0, padx=10, pady=10)
id_producto = tk.Entry(ventana)
id_producto.grid(row=0, column=1, padx=10, pady=10)

label_nombre = tk.Label(ventana, text="Nombre Producto:")
label_nombre.grid(row=2, column=0, padx=10, pady=10)
nombre = tk.Entry(ventana)
nombre.grid(row=2, column=1, padx=10, pady=10)

label_precio = tk.Label(ventana, text="Precio:")
label_precio.grid(row=3, column=0, padx=10, pady=10)
precio = tk.Entry(ventana)
precio.grid(row=3, column=1, padx=10, pady=10)


label_cantidad = tk.Label(ventana, text="Cantidad:")
label_cantidad.grid(row=4, column=0, padx=10, pady=10)
cantidad = tk.Entry(ventana)
cantidad.grid(row=4, column=1, padx=10, pady=10)


label_presentacion = tk.Label(ventana, text="Presentación: ")
label_presentacion.grid(row=5, column=0, padx=10, pady=10)
presentacion = tk.Entry(ventana)
presentacion.grid(row=5, column=1, padx=10, pady=10)

# Crear Botonones
boton_agregar_producto = tk.Button(ventana, text="Agrega Producto", command = lambda: agregar_producto(id_producto, nombre, precio, cantidad, presentacion))
boton_agregar_producto.grid(row=6, column=1, padx=10, pady=10)



#Iniciar el bucle principal
ventana.mainloop()