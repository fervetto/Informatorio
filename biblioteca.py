def crear_libro(titulo, anio, autor):
    return {'titulo':titulo, 'año': anio, 'autor':autor}

def agregar_libro(biblioteca, libro):
    biblioteca.append(libro)
    
def buscar_libro(biblioteca, titulo):
    for libro in biblioteca:
        if libro['titulo'] == titulo:
            return libro
    return None

