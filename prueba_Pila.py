# -*- coding: utf-8 -*-

from Pila import Pila

if __name__ == "__main__":
    # Creamos una pila
    pila = Pila()

    # Añadimos elementos
    print("Agregando elementos a la pila...")
    pila.push(1)
    pila.push(2)
    pila.push(3)

    # Mostramos el estado actual de la pila
    print(f"Estado actual de la pila: {pila}")

    # Vemos el elemento en el tope de la pila
    print(f"Elemento en el tope: {pila.peek()}")

    # Sacamos un elemento
    print("Sacando un elemento de la pila...")
    pila.pop()

    # Mostramos el estado de la pila nuevamente
    print(f"Estado de la pila después de sacar un elemento: {pila}")

    # Comprobamos si la pila está vacía
    print(f"¿La pila está vacía? {'Sí' if pila.is_empty() else 'No'}")



    pila = Pila()

    p1 = Pelicula(1, "Django", "Tarantino", 2015)
    print(p1)

    '''
    p2 = Pelicula(2, "Star Wars", "Lucas", 1982)


    print("tiene que decir True por que está vacía")
    print(pila.is_empty())

    print("La pila está vacía")
    print(pila)
    

    print("pila con Django")
    pila.push(p1)
    print(pila)

    print("pila con Django y SW")
    pila.push(p2)
    print(pila)

    print("SW sin extraer")
    print(pila.peek())

    print("SW")
    print(pila.pop())
    print(pila)

    print("Django")
    print(pila.pop())
    print(pila)

    print("pila vacía")
    print(pila.pop())
    print(pila)

    '''


    '''
    ()
    () ()
    ((()))
    (()())
    ((())))

    ( [ ( ] ) )
    1 2 3 4 5 6 

    Tope
    6 )
    5 )
    4 ]
    3 (
    2 [
    1 (

    Extracción
    6 ) cierre 
        - OK: 
            - cierre de otro paréntesis del tipo que sea
            - apertura de mi mismo tipo de paréntesis
        - KO: 
            - apertura de otro tipo de paréntesis


    1. Mientras haya elementos
        1.1. Leer caracter por caracter
        1.2. Push agregando el elemento

    3. Mientras haya elementos
        3.1. Extraemos un elemento
        3.2. Comprobamos si el elemento extraído es válido con respecto del elemento siguiente (peek)
            Válidos: cierre de otro paréntesis de cualquier tipo
                    apertura de mi mismo tipo de paréntesis
            No válidos: 
                    apertura de otro tipo de paréntesis --> Error y salimos
    4. Comprar si la pila está vacía
        Sí está vacía: todo Ok
        No está vacía: KO
    5. Finalizar
    '''