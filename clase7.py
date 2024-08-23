# def saludar():
#     return 'Hola mundo!'

# print(saludar())

# def sumar(num_1 , num_2 = 10):
#     return num_1 + num_2

# numero_1 = 3
# numero_2 = 8 

# resultado = sumar(num_1=numero_2)

# print(f'resultado de la suma: {resultado}')

# def saludar(nombre, mensaje = 'Hola'):
#     return f'{mensaje}, {nombre}'

# print(saludar('Ceci', 'Chau'))

# def impresion_con_args(a,b,*args):
#     print(f'a = {a}')
#     print(f'b = {b}')
#     print(f'args = {args}')


# impresion_con_args(1,2,3,4)
    
# def sumar(**kwargs):
#     resultado=0

#     for clave, valor in kwargs.items():
#         print(clave, '=', valor)
#         resultado += valor
    
#     return resultado

# print(sumar(a=3,b=10,c=5))

# def impresion_con_args_kwargs(a,b,*args,c,d,**kwargs):
#     print(f'a = {a}')
#     print(f'b = {b}')
#     print(f'args = {args}')
#     print(f'c = {c}')
#     print(f'd = {d}')
#     print(f'kwargs = {kwargs}')
    
# impresion_con_args_kwargs(1,2,3,4,c=5,d=6,e=7,f=8)

# def operacion(a,b):
#     suma = a+b
#     resta = a-b

#     return suma,resta

# resultado_de_suma,resultado_de_resta  = operacion(5,3)

# print(resultado_de_resta,resultado_de_suma)

# def multiplicar(a,b):
#     return a * b
#     print('fin de la funcion')

# assert multiplicar(3,2) > 6, 'no es mayor a 6'
import os
usuarios = [{'nombre' : 'Juan', 'pin':'1234', 'saldo':1000, 'intentos_login':0, 'bloqueado': False},
            {'nombre' : 'Luca', 'pin':'5678', 'saldo':1500, 'intentos_login':0, 'bloqueado' : False}]


#Funcion para verificar pin
def verificar_pin(usuario, pin):
    while pin != usuario['pin'] and not usuario['bloqueado']:
        print('Pin incorrecto, Intente nuevamente')
        pin = input('Ingrese su pin: ')
        os.system('cls')
    if usuario['intentos_login'] >= 4:
        usuario['bloqueado']= True
    usuario['intentos_login'] += 1
    if usuario['bloqueado']:
        print('Usuario bloqueado, comuniquese con su entidad bancaria')

    if pin == usuario['pin'] and not usuario['bloqueado']:
        usuario['intentos_login']=0
    return usuario

#Función para encontrar un usuario mediante su nombre
def encontrar_usuario(nombre):
    for usuario in usuarios:
        if usuario['nombre'] == nombre:
            return usuario
    return None

#Función para consultar el saldo
def consultar_saldo(usuario):
    return usuario['saldo']

#Función para depositar
def depositar(usuario,monto):
    usuario['saldo'] += monto
    return usuario['saldo']

def cajero():
    nombre =input('Ingrese su nombre: ')
    usuario = encontrar_usuario(nombre)

    if usuario is None:
        print('usuario no encontrado')
        return
    
    pin = input('Ingrese su pin: ')
    os.system('cls')

    # while pin != usuario['pin'] and not usuario['bloqueado']:
    #     print('Pin incorrecto, Intente nuevamente')
    #     pin = input('Ingrese su pin: ')
    #     os.system('cls')
    #     if usuario['intentos_login'] >= 4:
    #         usuario['bloqueado']= True
    #     usuario['intentos_login'] += 1
    # if usuario['bloqueado']:
    #     print('Usuario bloqueado, comuniquese con su entidad bancaria')

    # if pin == usuario['pin'] and not usuario['bloqueado']:
    #     usuario['intentos_login']=0
    verificar_pin(usuario, pin)
    while True:
        print('\nOpciones:')
        print('1. Consultar saldo')
        print('2. Depositar dinero')
        print('3. Salir')
        opcion = input('Seleccione una opcion: ')
        os.system('cls')

        if opcion == '1':
            print(f'Saldo actual: {consultar_saldo(usuario)}')
        elif opcion == '2':
            monto = int(input('Ingrese la cantidad que deseaa depositar: '))
            nuevo_saldo = depositar(usuario, monto)
            print('Su nuevo saldo es', nuevo_saldo)
        elif opcion == '3':
            print('Gracias por utilizar el cajero!')
            break
        else:
            print('Opcion invalida')

cajero()