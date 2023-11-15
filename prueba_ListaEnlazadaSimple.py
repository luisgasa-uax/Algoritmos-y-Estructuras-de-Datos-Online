# -*- coding: utf-8 -*-

from ListaEnlazadaSimple import ListaEnlazadaSimple
from Pelicula import Pelicula

# Creando un script de prueba
if __name__ == '__main__':
    lista = ListaEnlazadaSimple()

    # Probando la inserción
    peli1 = Pelicula(1, "Django", "Tarantino", 2012)
    peli2 = Pelicula(2, "Pulp Fiction", "Tarantino", 1994)
    peli3 = Pelicula(3, "Los siete samuráis", "Kurosawa", 1954)

    lista.insertar_al_final(peli1)
    lista.insertar_al_final(peli2)
    print(lista)
    print()

    lista.insertar_en_posicion(peli3, 1)  # Insertar el número 3 en la posición 1
    print(f"Lista después de inserciones: {lista}")
    
    # Verificando si la lista es vacía
    if lista.es_vacia():
        print("La lista está vacía.")
    else:
        print("La lista no está vacía.")

    # Mostrando el tamaño de la lista
    print(f"El tamaño de la lista es: {lista.tamano}")

    # Añadir más pruebas según sea necesario...

    print("Eliminamos la peli 2")
    lista.eliminar(2)
    print(lista)