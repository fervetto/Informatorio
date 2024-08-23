import tkinter as tk
operadores=['+', '-', '*', '/']
resultado = 0
operando = '0'

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("El segundo número debe ser distinto de 0")


def calculadora(operando1, operando2, operador):
    while True:
        num1 = int(operando1)
        num2 = int(operando2)
 
        if operador == '+':
            return sumar(num1, num2)
        elif opcion == '-':
            restar(num1, num2)
        elif opcion == '*':
            multiplicar(num1, num2)
        elif opcion == '/':
            dividir(num1, num2)
        elif opcion ==5:
            break
        else:
            print("Opcion no válida, intente nuevamente: ")

def boton_presionado(valor):
    global operando
    if valor.isdigit():
        operando = operando+valor
    elif valor in operadores:
        resultado = int(operando)
        operando=''
        operador=valor
        resultado=calculadora(resultado, operador, operando)
        print(resultado)
    elif valor == '=':
        print(resultado)
        

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear botones con valores predeterminados
valores = ['1','2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '=']
botones = []

for valor in valores:
    boton = tk.Button(ventana, text=str(valor), command=lambda v=valor: boton_presionado(v))
    boton.pack(side=tk.LEFT, padx=5, pady=5)
    botones.append(boton)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
