class Libro:
    def __init__(self, isbn, titulo, autor, anio_publicacion, ejemplares):
        self.isbn = isbn
        self.ejemplares = ejemplares
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha prestado {libro}")
        else:
            print(f"{libro} no está disponible")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto {libro}")
        else:
            print(f"{self.nombre} no tiene {libro}")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario registrado: {usuario.nombre}")

class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = None
        self.fecha_devolucion = None

    def realizar_prestamo(self):
        self.usuario.prestar_libro(self.libro)
        self.fecha_prestamo = "Fecha de préstamo"

    def realizar_devolucion(self):
        self.usuario.devolver_libro(self.libro)
        self.fecha_devolucion = "Fecha de devolución"

# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro("El Quijote", "Miguel de Cervantes")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez")

usuario1 = Usuario("Juan Pérez")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)

prestamo1 = Prestamo(usuario1, libro1)
prestamo1.realizar_prestamo()

prestamo1.realizar_devolucion()


while True:
    opcion= int(input('''Ingrese la operación deseada:
    1.- Agregar Nuevo Libro
    2.- Mostrar Libros disponibles
    3.- Prestar Libro
    4.- Devolver Libro
    5.- Buscar por titulo
    6.- Salir\n'''))

    if opcion == 1:
        titulo = input("Ingrese el título del libro: ")
        autor = input('Ingrese el autor: ')
        año_publicacion = input('Ingrese año publicacion: ')
        disponible_para_prestamo = True
        
        libro = Libro(titulo, autor, año_publicacion, disponible_para_prestamo)
        biblioteca.agregar_libro(libro)
        
        print(libro)
        biblioteca.mostrar_libros_disponibles()
        
    elif opcion == 2:
        biblioteca.mostrar_libros_disponibles()
        
    elif opcion ==3:
        titulo = input('Ingrese el titulo del libro: ')
        libro = biblioteca.buscar_por_titulo
        biblioteca.eliminar_libro(libro)
    elif opcion == 4:
        titulo = input('Ingrese el titulo del libro: ')
        libro
        biblioteca
    elif opcion == 5:
        titulo = input('Ingrese el titulo del libro: ')
        resultado = biblioteca.buscar_por_titulo(titulo)
        for libro in resultado:
            print(libro)
            
    
    elif opcion ==6:
        break
    else:
        print("Opcion no válida, intente nuevamente: ")

