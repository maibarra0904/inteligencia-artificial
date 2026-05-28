#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Plantilla de Tarea 1: Algoritmos Genéticos - Problema de la Mochila
Carrera de Computación (Sede Milagro) - Universidad Agraria del Ecuador

Instrucciones:
1. Complete los bloques de código marcados con "# TODO".
2. Ejecute el archivo para iniciar la simulación evolutiva y ver los resultados.
3. Responda a las preguntas de análisis en el archivo INSTRUCCIONES.md de su entrega.
"""

import random
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN DEL PROBLEMA ---
# Objetivos disponibles: (nombre, peso, valor)
OBJETOS = [
    ("Saco de dormir", 3, 80),
    ("Linterna", 1, 20),
    ("Botiquín", 2, 50),
    ("Botella de agua", 4, 70),
    ("Comida enlatada", 5, 60),
    ("Tienda de campaña", 7, 100),
    ("Brújula", 1, 30),
    ("Ropa de abrigo", 3, 40)
]

CAPACIDAD_MAXIMA = 15  # Peso máximo que soporta la mochila

# --- PARÁMETROS DEL ALGORITMO GENÉTICO ---
TAMANO_POBLACION = 20
GENERACIONES = 50
TASA_CRUZAMIENTO = 0.8
TASA_MUTACION = 0.05
TAMANO_TORNEO = 3

# --- FUNCIONES AUXILIARES Y OPERADORES EVOLUTIVOS ---

def crear_individuo():
    """
    Crea un individuo representado como un cromosoma binario.
    Ejemplo: [0, 1, 1, 0, 0, 1, 0, 1]
    """
    # TODO: Retorne una lista de longitud len(OBJETOS) con valores 0 o 1 generados aleatoriamente
    return [random.randint(0, 1) for _ in range(len(OBJETOS))]

def crear_poblacion(tamano):
    """
    Crea una población inicial de individuos.
    """
    # TODO: Retorne una lista con 'tamano' cantidad de individuos creados
    return [crear_individuo() for _ in range(tamano)]

def evaluar_fitness(individuo):
    """
    Calcula la aptitud (fitness) de un individuo.
    Debe sumar el valor de los objetos seleccionados.
    Si el peso total supera CAPACIDAD_MAXIMA, se debe aplicar una penalización extrema (ej. retornar 0).
    """
    peso_total = 0
    valor_total = 0
    
    # TODO: Calcule el peso_total y el valor_total recorriendo el individuo
    # e indexando en la lista de OBJETOS.
    for i, gen in enumerate(individuo):
        if gen == 1:
            peso_total += OBJETOS[i][1]
            valor_total += OBJETOS[i][2]
            
    # TODO: Si peso_total supera CAPACIDAD_MAXIMA, penalice la aptitud retornando 0 o 1.
    # En caso contrario, retorne el valor_total como aptitud.
    if peso_total > CAPACIDAD_MAXIMA:
        return 0
        
    return valor_total

def seleccion_torneo(poblacion, fitnesses, k=3):
    """
    Selecciona un individuo de la población mediante el método de torneo.
    Se eligen 'k' individuos al azar y se selecciona el que tenga el mejor fitness.
    """
    # TODO: Elija k índices aleatorios de la población
    seleccionados = random.sample(range(len(poblacion)), k)
    
    # TODO: Identifique cuál de los individuos seleccionados tiene la mayor aptitud
    mejor_indice = max(seleccionados, key=lambda idx: fitnesses[idx])
    
    return list(poblacion[mejor_indice])

def cruzamiento(padre1, padre2):
    """
    Realiza el cruzamiento de un punto entre dos padres para generar dos hijos.
    """
    if random.random() < TASA_CRUZAMIENTO:
        # TODO: Seleccione un punto de corte aleatorio entre 1 y len(OBJETOS) - 1
        punto = random.randint(1, len(OBJETOS) - 1)
        
        # TODO: Cree los hijos combinando las partes de los padres en el punto de corte
        hijo1 = padre1[:punto] + padre2[punto:]
        hijo2 = padre2[:punto] + padre1[punto:]
        
        return hijo1, hijo2
    else:
        # Si no hay cruzamiento, los hijos son copias idénticas de los padres
        return list(padre1), list(padre2)

def mutacion(individuo):
    """
    Aplica una mutación de un solo gen en el cromosoma basándose en la TASA_MUTACION.
    Para cada gen, si un número aleatorio es menor que TASA_MUTACION, se invierte su valor (0 a 1 o 1 a 0).
    """
    mutado = list(individuo)
    for i in range(len(mutado)):
        if random.random() < TASA_MUTACION:
            # TODO: Invierta el gen (si es 0 pasa a 1, si es 1 pasa a 0)
            mutado[i] = 1 - mutado[i]
    return mutado

# --- SIMULACIÓN DEL ALGORITMO GENÉTICO ---

def ejecutar_algoritmo_genetico():
    # Inicializar población
    poblacion = crear_poblacion(TAMANO_POBLACION)
    
    # Historial para graficar la convergencia
    historial_mejor_fitness = []
    historial_fitness_promedio = []
    
    mejor_solucion_global = None
    mejor_fitness_global = -1
    
    print("--- Iniciando Simulación Evolutiva ---")
    
    for gen in range(GENERACIONES):
        # Evaluar la aptitud de toda la población
        fitnesses = [evaluar_fitness(ind) for ind in poblacion]
        
        # Registrar métricas
        mejor_fit = max(fitnesses)
        promedio_fit = sum(fitnesses) / len(fitnesses)
        
        historial_mejor_fitness.append(mejor_fit)
        historial_fitness_promedio.append(promedio_fit)
        
        # Identificar y guardar al mejor individuo de la historia
        mejor_ind_gen = poblacion[fitnesses.index(mejor_fit)]
        if mejor_fit > mejor_fitness_global:
            mejor_fitness_global = mejor_fit
            mejor_solucion_global = list(mejor_ind_gen)
            
        print(f"Generación {gen + 1:02d}: Mejor Fitness = {mejor_fit} | Promedio = {promedio_fit:.2f}")
        
        # Crear la nueva generación (Población Siguiente)
        nueva_poblacion = []
        
        # TODO: Implemente el ciclo para llenar la nueva población.
        # En cada iteración, seleccione dos padres usando seleccion_torneo,
        # crúcelos usando cruzamiento, aplique mutacion a cada hijo y agréguelos a nueva_poblacion.
        # Nota: Asegúrese de no exceder el TAMANO_POBLACION.
        while len(nueva_poblacion) < TAMANO_POBLACION:
            padre1 = seleccion_torneo(poblacion, fitnesses, TAMANO_TORNEO)
            padre2 = seleccion_torneo(poblacion, fitnesses, TAMANO_TORNEO)
            
            hijo1, hijo2 = cruzamiento(padre1, padre2)
            
            nueva_poblacion.append(mutacion(hijo1))
            if len(nueva_poblacion) < TAMANO_POBLACION:
                nueva_poblacion.append(mutacion(hijo2))
                
        poblacion = nueva_poblacion
        
    print("\n--- Simulación Finalizada ---")
    print(f"Mejor Aptitud Encontrada: {mejor_fitness_global} puntos")
    
    # Mostrar la solución detallada
    peso_solucion = 0
    print("\nObjetos seleccionados en la mejor mochila:")
    for i, gen in enumerate(mejor_solucion_global):
        if gen == 1:
            nombre, peso, valor = OBJETOS[i]
            peso_solucion += peso
            print(f" - {nombre} (Peso: {peso} kg | Valor: {valor} puntos)")
    print(f"Peso Total: {peso_solucion} kg / {CAPACIDAD_MAXIMA} kg")
    
    return historial_mejor_fitness, historial_fitness_promedio

def graficar_convergencia(mejores, promedios):
    plt.figure(figsize=(10, 6))
    plt.plot(mejores, label="Mejor Aptitud (Fitness)", color="forestgreen", linewidth=2)
    plt.plot(promedios, label="Aptitud Promedio de la Población", color="royalblue", linestyle="--")
    plt.xlabel("Generación")
    plt.ylabel("Aptitud (Valor total en la Mochila)")
    plt.title("Convergencia del Algoritmo Genético")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    
    # Guardar gráfica
    plt.savefig("evolucion_fitness.png")
    print("\n[Éxito] Gráfica de convergencia guardada como 'evolucion_fitness.png'")
    plt.show()

if __name__ == "__main__":
    # Asegurar reproducibilidad para comparar
    random.seed(42)
    
    mejores, promedios = ejecutar_algoritmo_genetico()
    graficar_convergencia(mejores, promedios)
