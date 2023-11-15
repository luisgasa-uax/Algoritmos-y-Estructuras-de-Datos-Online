class Pelicula:
    """
    Representa una película con información como identificador, título, director y año.

    Attributes:
        id_pelicula (int): Un identificador único para la película.
        titulo (str): El título de la película.
        director (str): El director de la película.
        anio (int): El año en que la película fue lanzada.
    """

    def __init__(self, id_pelicula, titulo, director, anio):
        """
        Inicializa una instancia de la clase Pelicula con los datos proporcionados.

        Args:
            id_pelicula (int): El identificador único de la película.
            titulo (str): El título de la película.
            director (str): El director de la película.
            anio (int): El año de lanzamiento de la película.
        """
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.director = director
        self.anio = anio

    def equals(self, id_pelicula):
        """
        Verifica si el identificador de la película es igual al proporcionado.

        Args:
            id_pelicula (int): El identificador de la película a comparar.

        Returns:
            bool: True si los identificadores son iguales, False en caso contrario.
        """
        return self.id_pelicula == id_pelicula
    
    def compare_to(self, otra_pelicula):
        """
        Compara esta película con otra basada en su identificador.

        Args:
            otra_pelicula (Pelicula): La otra película a comparar.

        Returns:
            int: -1 si esta película tiene un ID menor, 1 si es mayor, o 0 si son iguales.
        """
        if self.id_pelicula < otra_pelicula.get_id():
            return -1
        elif self.id_pelicula > otra_pelicula.get_id():
            return 1
        else:
            return 0
    
    def get_id(self):
        """
        Devuelve el identificador de la película.

        Returns:
            int: El identificador de la película.
        """
        return self.id_pelicula
    
    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de la película.

        Returns:
            str: Una cadena que representa la película.
        """
        resultado = f"{self.id_pelicula}, {self.titulo}, {self.director}, {self.anio}"
        return resultado
