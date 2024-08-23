# # class Vehiculo:
    
# #     def __init__(self, ruedas, marca, modelo, color):
# #         self.ruedas = ruedas
# #         self.marca = marca
# #         self.modelo = modelo
# #         self.color = color
    
# #     def acelerar(self):
# #         print(f'El {self.marca} {self.modelo} esta acelerando')
        
# #     def frenar(self):
# #         print(f'El {self.marca} {self.modelo} esta frenando')

# # class Coche(Vehiculo):
    
# #     def tocar_vocina(self):
# #         print('Estoy tocando bocina!!')
    

# # class Motocicleta(Vehiculo):
    
# #     def acelerar(self):
# #         print('Esta moto esta acelerando')

# # miCoche= Coche(4, 'Renault', 'Clio', 'Negro')

# # una_moto = Motocicleta(2, 'Honda', 'Wave', 'Rojo')

# # print(f'El auto: {miCoche.marca} {miCoche.color} tiene {miCoche.ruedas} ruedas')

# # print(f'La moto: {una_moto.marca} {una_moto.color} tiene {una_moto.ruedas} ruedas')

# class A:
#     def __init__(self):
#         print('Creamos un objeto A')
        
# class B:
#     def __init__(self):
#         print('Creamos un objeto B')
        
# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         super().__init__()
#         print('Creamos un Objeto C')
        
# prueba = C()

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.__pi = 3.1415
        
    def calcular_area(self):
        return self.__pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * self.__pi * self.radio
    
circulo = Circulo(4.6)

print(f'el area del circulo es: {circulo.calcular_area()}')
print(f'el perimetro del circulo es: {circulo.calcular_perimetro()}')