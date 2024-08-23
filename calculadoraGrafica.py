import tkinter as tk
def sumar(num1, num2):
    return num1 + num2

def IngresarValor(num):
    pass
    
def saludar():
    print('Hola')

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("El segundo número debe ser distinto de 0")
        
def calculadora():
    leyenda = "El resultado es: "
    while True:
        num1 = int(input('Ingrese el primer valor: '))
        num2 = int(input('Ingrese el segundo valor: '))
        
        opcion= int(input('''Ingrese la operación deseada:
            1.- sumar
            2.- Restar
            3.- multiplicar
            4.- Dividir
            5.- Salir\n'''))
        
        if opcion == 1:
            print(leyenda, sumar(num1, num2))
        elif opcion == 2:
            print(leyenda, restar(num1, num2))
        elif opcion ==3:
            print(leyenda, multiplicar(num1, num2))
        elif opcion == 4:
            print(leyenda, dividir(num1, num2))
        elif opcion ==5:
            break
        else:
            print("Opcion no válida, intente nuevamente: ")

ventana= tk.Tk()
ventana.title('Calculadora')
ventana.geometry('500x700')

boton1 = tk.Button(ventana, text='1', command=saludar, font=('Arial', 20)).grid(row=1, column=1)
boton2 = tk.Button(ventana, text='2', command=saludar, font=('Arial', 20))
boton2.grid(column=2, row=1)
boton3 = tk.Button(ventana, text='3', command=saludar, font=('Arial', 20))
boton3.grid(column=3, row=1)
boton4 = tk.Button(ventana, text='4', command=saludar, font=('Arial', 20)).grid(column=1, row=2)
boton5 = tk.Button(ventana, text='5', command=saludar, font=('Arial', 20)).grid(column=2, row=2)
boton6 = tk.Button(ventana, text='6', command=saludar, font=('Arial', 20)).grid(column=3, row=2)
boton7 = tk.Button(ventana, text='7', command=saludar, font=('Arial', 20)).grid(column=1, row=3)
boton8 = tk.Button(ventana, text='8', command=saludar, font=('Arial', 20)).grid(column=2, row=3)
boton9 = tk.Button(ventana, text='9', command=saludar, font=('Arial', 20)).grid(column=3, row=3)
boton0 = tk.Button(ventana, text='0', command=saludar, font=('Arial', 20)).grid(column=1, row=4)
botonSuma = tk.Button(ventana, text='+', command=sumar, font=('Arial', 20)).grid(column=2, row=4)
botonResta = tk.Button(ventana, text='0', command=restar, font=('Arial', 20)).grid(column=3, row=3)
botonMultiplicar = tk.Button(ventana, text='*', command=multiplicar, font=('Arial', 20))
botonDivision = tk.Button(ventana, text='/', command=dividir, font=('Arial', 20))




ventana.mainloop()


calculadora()
