import tkinter as tk

ventana =tk.Tk()

ventana.title('Mi primer ventana con tkinter')
ventana.geometry('500x500')

etiqueta1 = tk.Label(ventana, text='Hola mundo desde la GUI', font=('Arial', 20))
etiqueta1.pack()

def saludar():
    print('hola mundo desde la consola')

boton = tk.Button(ventana, text='Saludar', command=saludar, font=('Arial', 20))
boton.pack()

ventana.mainloop()