class Libro:
    def __init__(self, isbn, titulo, autor, año_publicacion, disponible_para_prestamo):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible_para_prestamo = disponible_para_prestamo
        
    def prestar_libro(self):
        self.disponible_para_prestamo = False

        
    def __str__(self):
        prestamo_estado = "Sí" if self.disponible_para_prestamo else "No"
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}, Disponible para préstamo: {prestamo_estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
        return resultados

    def mostrar_libros_disponibles(self):
        disponibles = [libro for libro in self.libros if libro.disponible_para_prestamo]
        if disponibles:
            for libro in disponibles:
                print(libro)
        else:
            print("No hay libros disponibles para préstamo en este momento.")
            
    def eliminar_libro(self, libro):
        self.libros.remove(libro)
            


# Ejemplo de uso
biblioteca = Biblioteca()

libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez", 1967, True)
libro2 = Libro(2, "Don Quijote de la Mancha", "Miguel de Cervantes", 1605, False)
# # # libro3 = Libro("1984", "George Orwell", 1949, True)
# # # libro4 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, True)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
# # # biblioteca.agregar_libro(libro3)
# # # biblioteca.agregar_libro(libro4)

while True:
    opcion= int(input('''Ingrese la operación deseada:
    1.- Agregar Libro a la Biblioteca
    2.- Mostrar Libros disponibles
    3.- Eliminar Libro de la biblioteca
    4.- Prestar Libro
    5.- Buscar por titulo
    6.- Buscar por Autor
    7.- Salir\n'''))

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




print("\nBuscar libros por título 'Cien':")
for libro in biblioteca.buscar_por_titulo("Cien"):
    print(libro)

print("\nBuscar libros por autor 'Orwell':")
for libro in biblioteca.buscar_por_autor("Orwell"):
    print(libro)

print("\nMostrar todos los libros disponibles para préstamo:")
biblioteca.mostrar_libros_disponibles()