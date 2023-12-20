class Radar:
    """
    Clase que representa un radar de tráfico, con información sobre su ubicación, sentido de circulación y velocidad máxima permitida.

    Atributos:
        km_localizacion (float): Kilómetro en el que se encuentra el radar.
        sentido_circulacion (str): Sentido de circulación del radar (por ejemplo, "norte", "sur").
        velocidad_maxima (int): Velocidad máxima permitida en el tramo controlado por el radar.

    Métodos:
        calcular_velocidad(self, velocidad_actual): Calcula si la velocidad actual supera la velocidad máxima.
        get_datos(self): Devuelve una cadena con los datos del radar.
    """

    def __init__(self, km_localizacion, sentido_circulacion, velocidad_maxima):
        """
        Inicializa una nueva instancia de la clase Radar.

        Parámetros:
            km_localizacion (float): Kilómetro en el que se encuentra el radar.
            sentido_circulacion (str): Sentido de circulación del radar.
            velocidad_maxima (int): Velocidad máxima permitida en el tramo controlado por el radar.
        """
        self.km_localizacion = km_localizacion
        self.sentido_circulacion = sentido_circulacion
        self.velocidad_maxima = velocidad_maxima

    def calcular_velocidad(self, velocidad_actual):
        """
        Calcula si la velocidad actual supera la velocidad máxima permitida.

        Parámetros:
            velocidad_actual (int): La velocidad actual del vehículo.

        Retorna:
            str: Mensaje que indica si el vehículo ha superado o no la velocidad máxima permitida.
        """
        if velocidad_actual > self.velocidad_maxima:
            return f"CAZADO!!! Has superado la velocidad máxima ({self.velocidad_maxima}). Estás viajando a {velocidad_actual} km/h."
        else:
            return f"Estás viajando a {velocidad_actual} km/h. La velocidad máxima es de {self.velocidad_maxima} km/h."

    def get_datos(self):
        """
        Devuelve una cadena con los datos del radar.

        Retorna:
            str: Una cadena que contiene la localización, el sentido de circulación y la velocidad máxima del radar.
        """
        return f"Localización: {self.km_localizacion} km. Sentido de circulación: {self.sentido_circulacion}. Velocidad máxima: {self.velocidad_maxima} km/h."
