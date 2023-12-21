'''
Los árboles B y B+ son estructuras de datos de árbol utilizadas en bases de datos 
y sistemas de archivos para permitir la búsqueda, secuencialización, inserción y 
eliminación de datos en tiempo logarítmico. Son una generalización de los árboles 
binarios de búsqueda, donde un nodo puede tener más de dos hijos.

Más info: https://runestone.academy/ns/books/published/pythoned/Trees/ImplementacionArbolBusqueda.html

'''
class NodoB:
    ''' 
    Clase para representar un nodo en un árbol B.

    Atributos:
    claves (list): Lista de claves almacenadas en el nodo.
    hijos (list): Lista de referencias a los nodos hijos.
    es_hoja (bool): Indica si el nodo es una hoja.
    '''

    def __init__(self, t):
        self.claves = []
        self.hijos = []
        self.es_hoja = True
        self.t = t  # t es el grado mínimo del árbol

class ArbolB:
    ''' 
    Clase para representar un árbol B.

    Atributos:
    raiz (NodoB): La raíz del árbol.
    t (int): Grado mínimo del árbol.
    '''

    def __init__(self, t):
        self.raiz = NodoB(t)
        self.t = t

    # Métodos como insertar, buscar, etc., se agregarían aquí.
