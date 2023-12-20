# -*- coding: utf-8 -*-
from enum import Enum 

class TipoCarretera(Enum):
    """
    Enumeración para los tipos de carreteras.
    """
    CARRETERA_GENERAL = "Carretera General"
    CARRETERA_NACIONAL = "Carretera Nacional"
    AUTOVIA = "Autovía"
    AUTOPISTA = "Autopista"

class VelocidadesCarreteras(Enum): 
    """
    Enumeración para las velocidades máximas permitidas en diferentes tipos de carreteras.
    """
    VEL_CARRETERA_GENERAL = 80
    VEL_CARRETERA_NACIONAL = 90
    VEL_AUTOVIA = 120
    VEL_AUTOPISTA = 120

class Carretera:
    """
    Clase que representa una carretera, con atributos para su nombre, distancia, tipo, velocidad máxima y si tiene peaje.

    Atributos:
        nombre (str): El nombre de la carretera.
        distancia (int): La distancia de la carretera en kilómetros.
        tipo (TipoCarretera): El tipo de carretera.
        velocidad_maxima (VelocidadesCarreteras): La velocidad máxima permitida en la carretera.
        peaje (bool): Indica si la carretera tiene peaje.
        radares (list): Lista de radares en la carretera.
    """

    def __init__(self, nombre: str, distancia: int, tipo: TipoCarretera, 
                 velocidad_maxima: VelocidadesCarreteras, peaje: bool):
        """
        Inicializa una instancia de Carretera.

        Parámetros:
            nombre (str): El nombre de la carretera.
            distancia (int): La distancia de la carretera en kilómetros.
            tipo (TipoCarretera): El tipo de carretera.
            velocidad_maxima (VelocidadesCarreteras): La velocidad máxima permitida en la carretera.
            peaje (bool): Indica si la carretera tiene peaje.
        """
        self.nombre = nombre
        self.distancia = distancia
        self.tipo = tipo
        self.velocidad_maxima = velocidad_maxima
        self.peaje = peaje
        self.radares = []

    def agregar_radar(self, radar):
        """
        Agrega un radar a la lista de radares de la carretera.

        Parámetros:
            radar: El radar a agregar.
        """
        self.radares.append(radar)

    def __eq__(self, otra: 'Carretera') -> bool:
        """
        Determina si dos carreteras son iguales basado en su nombre.

        Parámetros:
            otra (Carretera): La otra carretera a comparar.

        Retorna:
            bool: True si las carreteras tienen el mismo nombre, False en caso contrario.
        """
        if not isinstance(other, Carretera):
            return NotImplemented
        return self.nombre == other.nombre
    
    def __hash__(self) -> str:
        """
        Retorna el valor hash de la carretera, basado en su nombre.

        Retorna:
            str: El valor hash de la carretera.
        """
        return hash((self.nombre))
    
    def __str__(self) -> str:
        """
        Representación en cadena de la carretera.

        Retorna:
            str: Una representación en cadena de la carretera.
        """
        return (f"Carretera: {self.nombre}, Distancia: {self.distancia} km, "
                f"Tipo: {self.tipo.value}, Velocidad Máxima: {self.velocidad_maxima} km/h, "
                f"Peajes: {self.peajes}")
