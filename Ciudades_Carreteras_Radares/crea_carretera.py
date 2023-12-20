from carretera import Carretera, TipoCarretera, VelocidadesCarreteras


if __name__ == "__main__":
    # Crear una nueva carretera
    nueva_carretera = Carretera(
        nombre="Carretera de Prueba",
        distancia=100,  # en kilómetros
        tipo=TipoCarretera.AUTOVIA,
        velocidad_maxima=VelocidadesCarreteras.VEL_AUTOVIA,
        peaje=False
    )

    # Imprimir detalles de la carretera
    print(nueva_carretera)
