import os
usuarios = [{'nombre' : 'Juan', 'pin':'1234', 'saldo':1000, 'intentos_login':0, 'bloqueado': False},
            {'nombre' : 'Luca', 'pin':'5678', 'saldo':1500, 'intentos_login':0, 'bloqueado' : False}]


#Funcion para verificar pin
def verificar_pin(usuario, pin):
    while pin != usuario['pin'] and not usuario['bloqueado']:
        usuario['intentos_login'] += 1
        print('Pin incorrecto, Intente nuevamente')
        pin = input('Ingrese su pin: ')
        os.system('cls')
        if usuario['intentos_login'] >= 4:
            usuario['bloqueado'] = True
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
    verificar_pin(usuario, pin)
    while not usuario['bloqueado']:
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