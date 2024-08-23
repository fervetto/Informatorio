# class Coche:
#     cantidad_ruedas = 4
#     # metodo constructor
#     def __init__(self, marca, modelo, color,):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
        
#     def acelerar(self):
#         print(f'El auto {self.marca} {self.modelo} {self.color} esta acelerando')


# # crear objeto de la clase coche

# mi_coche = Coche('Renault', 'Clio', 'Negro')
# print(mi_coche)

class CuentaBancaria:
    
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = saldo_inicial
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo_inicial += cantidad
            
    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo_inicial:
            self.saldo_inicial -=cantidad
    def mostrar_saldo(self):
        return self.saldo_inicial

cuenta = CuentaBancaria('Ana', 1000)

cuenta.depositar(500)
cuenta.retirar(450)
print(cuenta.mostrar_saldo)
cuenta.retirar(1100)
print(cuenta.mostrar_saldo)