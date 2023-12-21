def problema_mochila(valores, pesos, capacidad):
    n = len(valores)
    K = [[0 for x in range(capacidad + 1)] for x in range(n + 1)]

    # Construir la tabla K[][] de manera ascendente
    for i in range(n + 1):
        for w in range(capacidad + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif pesos[i-1] <= w:
                K[i][w] = max(valores[i-1] + K[i-1][w-pesos[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][capacidad]

# Ejemplo de uso
valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50

valor_maximo = problema_mochila(valores, pesos, capacidad)
print(f"Valor máximo que se puede obtener: {valor_maximo}")




