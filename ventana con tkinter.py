import tkinter as tk
import os
ventana = tk.Tk()
ventana.title("Mi primer ventana")
ventana.geometry("400x300")
etiqueta = tk.Label(ventana, text='hola mundo!', font=('Arial', 20))
etiqueta.pack()

def saludar():
    print('Hello!')
    
def limpiar():
    os.system('cls')
    
boton = tk.Button(ventana, text='saludar', font=('Arial', 20), command=saludar)
boton.pack()

limpiar = tk.Button(ventana, text='limpiar', font=('Arial', 20), command=limpiar)
limpiar.pack()

ventana.mainloop()