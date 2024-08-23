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


ventana= ventana.title('Calculadora')
ventana.geometry('500x700')
calculadora()
