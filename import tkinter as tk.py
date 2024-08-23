import tkinter as tk

def boton_presionado(valor):
    operando = ''
    if valor.isdigit():
        operando = operando + valor
    if valor == '+':
        operador= '+'
            

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear botones con valores predeterminados
valores = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0']
botones = []

for valor in valores:
    boton = tk.Button(ventana, text=str(valor), command=lambda v=valor: boton_presionado(v))
    boton.pack(side=tk.LEFT, padx=5, pady=5)
    botones.append(boton)

# Iniciar el bucle principal de la ventana
ventana.mainloop()

print(boton_presionado())