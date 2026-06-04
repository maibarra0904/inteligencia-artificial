import math
import random


def calcular_distancia_total(ruta, matriz_distancias):
    """
    Calcula la distancia total recorrida de una ruta cerrada.
    La ruta empieza en la UAE y al final retorna al punto inicial.
    """
    distancia = 0
    n = len(ruta)

    for i in range(n):
        origen = ruta[i]
        destino = ruta[(i + 1) % n]
        distancia += matriz_distancias[origen][destino]

    return distancia


def generar_vecino(ruta):
    """
    Genera una ruta vecina intercambiando dos fincas.
    El indice 0, correspondiente a la UAE Milagro, permanece fijo al inicio.
    """
    nueva_ruta = list(ruta)
    idx1, idx2 = random.sample(range(1, len(ruta)), 2)
    nueva_ruta[idx1], nueva_ruta[idx2] = nueva_ruta[idx2], nueva_ruta[idx1]
    return nueva_ruta


def recocido_simulado(matriz_distancias, temp_inicial, temp_final, alfa):
    """
    Implementa Recocido Simulado para aproximar una solucion al TSP.
    """
    fincas = list(range(1, len(matriz_distancias)))
    random.shuffle(fincas)
    solucion_actual = [0] + fincas

    distancia_actual = calcular_distancia_total(solucion_actual, matriz_distancias)
    mejor_solucion = list(solucion_actual)
    mejor_distancia = distancia_actual

    temperatura = temp_inicial
    iteracion = 0

    while temperatura > temp_final:
        vecino = generar_vecino(solucion_actual)
        distancia_vecino = calcular_distancia_total(vecino, matriz_distancias)
        diferencia = distancia_vecino - distancia_actual

        if diferencia < 0 or random.random() < math.exp(-diferencia / temperatura):
            solucion_actual = vecino
            distancia_actual = distancia_vecino

            if distancia_actual < mejor_distancia:
                mejor_solucion = list(solucion_actual)
                mejor_distancia = distancia_actual

        temperatura *= alfa
        iteracion += 1

    return mejor_solucion, mejor_distancia, iteracion


def mostrar_ruta(ruta, nombres_lugares):
    """Convierte una ruta numerica en una ruta con nombres."""
    ruta_con_retorno = ruta + [ruta[0]]
    return " -> ".join(nombres_lugares[i] for i in ruta_con_retorno)


if __name__ == "__main__":
    random.seed(42)

    nombres = [
        "UAE Milagro",
        "Finca Experimental A",
        "Finca Experimental B",
        "Finca Experimental C",
        "Finca Experimental D",
        "Finca Experimental E",
    ]

    distancias = [
        [0, 12, 25, 18, 30, 22],
        [12, 0, 15, 28, 40, 10],
        [25, 15, 0, 20, 18, 35],
        [18, 28, 20, 0, 12, 25],
        [30, 40, 18, 12, 0, 16],
        [22, 10, 35, 25, 16, 0],
    ]

    mejor_ruta, menor_distancia, total_iter = recocido_simulado(
        distancias,
        temp_inicial=100.0,
        temp_final=0.1,
        alfa=0.95,
    )

    print("Mejor ruta de insumos encontrada:", mejor_ruta)
    print("Ruta con nombres:", mostrar_ruta(mejor_ruta, nombres))
    print("Distancia minima total (km):", menor_distancia)
    print("Total de iteraciones del algoritmo:", total_iter)
