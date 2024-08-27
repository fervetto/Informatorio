import csv

lista_de_diccionarios = [
    {"nombre": "Ana", "edad": 28, "ciudad": "Madrid"},
    {"nombre": "Juan", "edad": 34, "ciudad": "Barcelona"},
    {"nombre": "María", "edad": 31, "ciudad": "Valencia"}
]


def escribir_lista_de_diccionarios_en_csv(nombre_archivo, lista_de_diccionarios):
    # Obtén los nombres de las claves (columnas) del primer diccionario
    claves = lista_de_diccionarios[0].keys()
    
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
        escritor_csv = csv.DictWriter(file, fieldnames=claves)
        
        # Escribe la cabecera
        escritor_csv.writeheader()
        
        # Escribe las filas
        escritor_csv.writerows(lista_de_diccionarios)

# Uso de la función
nombre_archivo = 'archivo.csv'
escribir_lista_de_diccionarios_en_csv(nombre_archivo, lista_de_diccionarios)
