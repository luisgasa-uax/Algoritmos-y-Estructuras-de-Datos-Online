class Ciudad:
    """
    Clase que representa una ciudad con su nombre, población y coordenadas GPS.

    Atributos:
        nombre (str): El nombre de la ciudad.
        poblacion (int): La población de la ciudad.
        coordenadas_gps (tuple): Las coordenadas GPS de la ciudad, usualmente en formato (latitud, longitud).

    Métodos:
        __eq__(self, other): Compara esta ciudad con otra para ver si tienen el mismo nombre.
        __hash__(self): Genera un valor hash basado en el nombre de la ciudad.
        __str__(self): Devuelve una representación en cadena de la ciudad.
    """

    def __init__(self, nombre, poblacion, coordenadas_gps):
        """
        Inicializa una nueva instancia de la clase Ciudad.

        Parámetros:
            nombre (str): El nombre de la ciudad.
            poblacion (int): La población de la ciudad.
            coordenadas_gps (tuple): Las coordenadas GPS de la ciudad, en formato (latitud, longitud).
        """
        self.nombre = nombre
        self.poblacion = poblacion
        self.coordenadas_gps = coordenadas_gps

    def __eq__(self, other):
        """
        Compara esta ciudad con otra ciudad para ver si tienen el mismo nombre.

        Parámetros:
            other (Ciudad): La otra ciudad a comparar.

        Retorna:
            bool: True si ambas ciudades tienen el mismo nombre, False en caso contrario.
        """
        if not isinstance(other, Ciudad):
            # No se compara contra instancias de otros tipos
            return NotImplemented
        return self.nombre == other.nombre
    
    def __hash__(self):
        """
        Retorna un valor hash para la ciudad, basado en su nombre.

        Retorna:
            int: El valor hash de la ciudad.
        """
        return hash(self.nombre)

    def __str__(self):
        """
        Representación en cadena de la ciudad.

        Retorna:
            str: Una cadena que representa la ciudad, incluyendo su nombre, población y coordenadas GPS.
        """
        return f"Ciudad: {self.nombre}, Población: {self.poblacion}, Coordenadas GPS: {self.coordenadas_gps}"
