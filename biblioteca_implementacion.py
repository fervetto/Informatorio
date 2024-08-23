from biblioteca import crear_libro, agregar_libro, buscar_libro

biblioteca = []

libro1 = crear_libro('Harry Potter', 1810, 'J.K. Rowling')
agregar_libro(biblioteca,libro1)

print(biblioteca)