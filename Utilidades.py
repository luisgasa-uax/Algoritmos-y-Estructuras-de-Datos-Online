# -*- coding: utf-8 -*-

# Paquete de utilidades

import sys
import os
import time
import time

class Cronometro:
    """
    ⏱ Un cronómetro para medir el tiempo transcurrido. Se utiliza para cronometrar
    operaciones o la duración de ejecución de un script.
    
    Ejemplo de uso:
    
    with Cronometro() as crono:
        # Ejecutar algunas operaciones
        pass
    
    print(f"Tiempo transcurrido: {crono.tiempo_transcurrido} segundos")
    """

    def __init__(self):
        """
        Inicializa el cronómetro, pero no comienza a contar el tiempo todavía.
        """
        self.inicio = None
        self.fin = None
        self.tiempo_transcurrido = None

    def __enter__(self):
        """
        Comienza a contar el tiempo cuando se entra en el contexto.
        """
        self.inicio = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Detiene el cronómetro cuando se sale del contexto y calcula
        el tiempo transcurrido.
        
        Parámetros:
            exc_type: Tipo de excepción
            exc_val: Valor de la excepción
            exc_tb: Traza de la excepción
        """
        self.fin = time.time()
        self.tiempo_transcurrido = self.fin - self.inicio
        print(f"Tiempo transcurrido: {self.tiempo_transcurrido} segundos")


class SuppressPrint:
    """
    Un gestor de contexto para suprimir la salida impresa en la consola
    dentro de un bloque de código. Redirige sys.stdout a /dev/null,
    y luego lo restaura a su valor original al salir del bloque.
    
        Ejemplo de uso:
        
        with SuppressPrint():
            print("Esto no se imprimirá en la consola")
    
    Después del bloque with, la salida a la consola se comportará normalmente.
    """

    def __enter__(self):
        """
        Método especial que se ejecuta al entrar en el bloque del gestor de contexto.
        Guarda la referencia actual de sys.stdout y lo reemplaza con un nuevo stream
        que descarta lo que se le envíe.
        """
        self._original_stdout = sys.stdout
        # Redireccionamos sys.stdout a /dev/null
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método especial que se ejecuta al salir del bloque del gestor de contexto.
        Cierra el stream de salida actual y restaura sys.stdout a su valor original.
        
        Parámetros:
            exc_type: Tipo de excepción
            exc_val: Valor de la excepción
            exc_tb: Traza de la excepción
        """
        # Restauramos sys.stdout a su valor original
        sys.stdout.close()
        sys.stdout = self._original_stdout
