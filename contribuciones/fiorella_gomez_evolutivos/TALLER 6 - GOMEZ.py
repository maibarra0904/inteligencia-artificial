import math
import random

def calcular_distancia_total(ruta, matriz_distancias):
    """
    Función de aptitud: Calcula la distancia total recorrida de una ruta.
    """
    distancia = 0
    n = len(ruta)

    for i in range(n):
        origen = ruta[i]
        destino = ruta[(i + 1) % n]  # Regresa al punto inicial
        distancia += matriz_distancias[origen][destino]

    return distancia


def generar_vecino(ruta):
    """
    Genera una solución vecina intercambiando dos fincas.
    La UAE (0) permanece fija.
    """
    nueva_ruta = list(ruta)

    idx1, idx2 = random.sample(range(1, len(ruta)), 2)

    nueva_ruta[idx1], nueva_ruta[idx2] = (
        nueva_ruta[idx2],
        nueva_ruta[idx1]
    )

    return nueva_ruta


def recocido_simulado(matriz_distancias,
                      temp_inicial=100.0,
                      temp_final=0.1,
                      alfa=0.95):

    # UAE fija al inicio
    solucion_actual = [0]

    restantes = list(range(1, len(matriz_distancias)))
    random.shuffle(restantes)

    solucion_actual.extend(restantes)

    distancia_actual = calcular_distancia_total(
        solucion_actual,
        matriz_distancias
    )

    mejor_solucion = list(solucion_actual)
    mejor_distancia = distancia_actual

    T = temp_inicial
    iteracion = 0

    while T > temp_final:

        vecino = generar_vecino(solucion_actual)

        distancia_vecino = calcular_distancia_total(
            vecino,
            matriz_distancias
        )

        diff = distancia_vecino - distancia_actual

        # Criterio de aceptación de Metrópolis
        if diff < 0 or random.random() < math.exp(-diff / T):

            solucion_actual = vecino
            distancia_actual = distancia_vecino

            if distancia_actual < mejor_distancia:
                mejor_solucion = list(solucion_actual)
                mejor_distancia = distancia_actual

        T *= alfa
        iteracion += 1

    return mejor_solucion, mejor_distancia, iteracion


# Matriz de distancias (km)
distancias = [
    [0, 12, 25, 18, 30, 22],  # UAE
    [12, 0, 15, 28, 40, 10],  # Finca A
    [25, 15, 0, 20, 18, 35],  # Finca B
    [18, 28, 20, 0, 12, 25],  # Finca C
    [30, 40, 18, 12, 0, 16],  # Finca D
    [22, 10, 35, 25, 16, 0]   # Finca E
]

# Ejecución
mejor_ruta, menor_distancia, total_iter = recocido_simulado(
    distancias,
    100.0,
    0.1,
    0.95
)

print("Mejor ruta encontrada:", mejor_ruta)
print("Distancia mínima total (km):", menor_distancia)
print("Total de iteraciones:", total_iter)