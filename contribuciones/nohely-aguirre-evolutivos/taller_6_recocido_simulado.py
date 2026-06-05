import math 
import random 
 
def calcular_distancia_total(ruta, matriz_distancias): 
    """ 
    Función de aptitud: Calcula la distancia total recorrida de una ruta (viaje redondo). 
    """ 
    distancia = 0 
    n = len(ruta) 
    for i in range(n): 
        origen = ruta[i] 
        destino = ruta[(i + 1) % n]  # Retorna al punto de partida (UAE) 
        distancia += matriz_distancias[origen][destino] 
    return distancia 
 
def generar_vecino(ruta): 
    """ 
    Genera una solución vecina intercambiando dos paradas aleatoriamente. 
    Se mantiene la UAE (índice 0) fija al inicio. 
    """ 
    nueva_ruta = list(ruta) 
    idx1, idx2 = random.sample(range(1, len(ruta)), 2) 
    nueva_ruta[idx1], nueva_ruta[idx2] = nueva_ruta[idx2], nueva_ruta[idx1] 
    return nueva_ruta 
 
def recocido_simulado(matriz_distancias, temp_inicial, temp_final, alfa): 
    """ 
    Implementa el algoritmo de Recocido Simulado para resolver el TSP. 
    """ 
    # Solución inicial: UAE (0) seguido de los demás centros ordenados 
    solucion_actual = list(range(len(matriz_distancias))) 
    random.shuffle(solucion_actual[1:])  # Mezclar fincas experimentalmente 
     
    distancia_actual = calcular_distancia_total(solucion_actual, matriz_distancias) 
    mejor_solucion = list(solucion_actual) 
    mejor_distancia = distancia_actual 
     
    T = temp_inicial 
    iteracion = 0 
     
    while T > temp_final: 
        vecino = generar_vecino(solucion_actual) 
        distancia_vecino = calcular_distancia_total(vecino, matriz_distancias) 
        diff = distancia_vecino - distancia_actual 
         
        # Criterio de Metrópolis para aceptación de soluciones 
        if diff < 0 or random.random() < math.exp(-diff / T): 
            solucion_actual = vecino 
            distancia_actual = distancia_vecino 
             
            if distancia_actual < mejor_distancia: 
                mejor_solucion = list(solucion_actual) 
                mejor_distancia = distancia_actual 
         
        T *= alfa  # Enfriamiento geométrico 
        iteracion += 1 
         
    return mejor_solucion, mejor_distancia, iteracion 
 
# Matriz de distancias en km entre UAE Milagro (0) y 5 fincas agrícolas (1 a 5) 
distancias = [ 
    [0, 12, 25, 18, 30, 22],  # 0: UAE Milagro (Sede Central) 
    [12, 0, 15, 28, 40, 10],  # 1: Finca Experimental A 
    [25, 15, 0, 20, 18, 35],  # 2: Finca Experimental B 
    [18, 28, 20, 0, 12, 25],  # 3: Finca Experimental C 
    [30, 40, 18, 12, 0, 16],  # 4: Finca Experimental D 
    [22, 10, 35, 25, 16, 0]   # 5: Finca Experimental E 
] 
 
# Ejecución del algoritmo 
mejor_ruta, menor_distancia, total_iter = recocido_simulado(distancias, 100.0, 0.1, 0.95) 
print("Mejor ruta de insumos encontrada:", mejor_ruta) 
print("Distancia mínima total (km):", menor_distancia) 
print("Total de iteraciones del algoritmo:", total_iter) 
