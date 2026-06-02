#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tarea 1 -- Algoritmos Genéticos (Problema de la Mochila)

"""

import argparse
import random
import matplotlib.pyplot as plt
from pathlib import Path

# --- CONFIGURACIÓN DEL PROBLEMA ---
# Objetos disponibles: (nombre, peso, valor)
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


def crear_individuo():
    """Crea un individuo representado como un cromosoma binario."""
    return [random.randint(0, 1) for _ in range(len(OBJETOS))]


def crear_poblacion(tamano):
    """Crea una población inicial de individuos."""
    return [crear_individuo() for _ in range(tamano)]


def evaluar_fitness(individuo):
    """Calcula la aptitud (fitness) de un individuo con penalización por peso."""
    peso_total = 0
    valor_total = 0
    for i, gen in enumerate(individuo):
        if gen == 1:
            peso_total += OBJETOS[i][1]
            valor_total += OBJETOS[i][2]

    return valor_total if peso_total <= CAPACIDAD_MAXIMA else 0


def seleccion_torneo(poblacion, fitnesses, k=TAMANO_TORNEO):
    """Selecciona un individuo por torneo (el mejor entre k aleatorios)."""
    seleccionados = random.sample(range(len(poblacion)), k)
    mejor_indice = max(seleccionados, key=lambda idx: fitnesses[idx])
    return list(poblacion[mejor_indice])


def cruzamiento(padre1, padre2):
    """Cruzamiento de un punto entre dos padres."""
    if random.random() < TASA_CRUZAMIENTO:
        punto = random.randint(1, len(OBJETOS) - 1)
        hijo1 = padre1[:punto] + padre2[punto:]
        hijo2 = padre2[:punto] + padre1[punto:]
        return hijo1, hijo2
    return list(padre1), list(padre2)


def mutacion(individuo):
    """Mutación por gen con probabilidad `TASA_MUTACION`."""
    mutado = list(individuo)
    for i in range(len(mutado)):
        if random.random() < TASA_MUTACION:
            mutado[i] = 1 - mutado[i]
    return mutado


def ejecutar_algoritmo_genetico(seed=42, tamano_poblacion=TAMANO_POBLACION, generaciones=GENERACIONES):
    random.seed(seed)
    poblacion = crear_poblacion(tamano_poblacion)

    historial_mejor_fitness = []
    historial_fitness_promedio = []

    mejor_solucion_global = None
    mejor_fitness_global = -1

    print("--- Iniciando Simulación Evolutiva ---")

    for gen in range(generaciones):
        fitnesses = [evaluar_fitness(ind) for ind in poblacion]
        mejor_fit = max(fitnesses)
        promedio_fit = sum(fitnesses) / len(fitnesses)

        historial_mejor_fitness.append(mejor_fit)
        historial_fitness_promedio.append(promedio_fit)

        mejor_ind_gen = poblacion[fitnesses.index(mejor_fit)]
        if mejor_fit > mejor_fitness_global:
            mejor_fitness_global = mejor_fit
            mejor_solucion_global = list(mejor_ind_gen)

        print(f"Generación {gen + 1:02d}: Mejor Fitness = {mejor_fit} | Promedio = {promedio_fit:.2f}")

        nueva_poblacion = []
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = seleccion_torneo(poblacion, fitnesses)
            padre2 = seleccion_torneo(poblacion, fitnesses)
            hijo1, hijo2 = cruzamiento(padre1, padre2)
            nueva_poblacion.append(mutacion(hijo1))
            if len(nueva_poblacion) < tamano_poblacion:
                nueva_poblacion.append(mutacion(hijo2))

        poblacion = nueva_poblacion

    print("\n--- Simulación Finalizada ---")
    print(f"Mejor Aptitud Encontrada: {mejor_fitness_global} puntos")

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
    plt.grid(True, linestyle=":" , alpha=0.6)

    ruta_guardado = Path(__file__).resolve().parent / "evolucion_fitness.png"
    plt.savefig(ruta_guardado)
    print(f"\n[Éxito] Gráfica de convergencia guardada en '{ruta_guardado}'")
    plt.show()

def parse_args():
    parser = argparse.ArgumentParser(description="Ejecutar AG para problema de la mochila")
    parser.add_argument("--seed", type=int, default=42, help="Semilla aleatoria")
    parser.add_argument("--generaciones", type=int, default=GENERACIONES, help="Número de generaciones")
    parser.add_argument("--poblacion", type=int, default=TAMANO_POBLACION, help="Tamaño de la población")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    mejores, promedios = ejecutar_algoritmo_genetico(seed=args.seed, tamano_poblacion=args.poblacion, generaciones=args.generaciones)
    graficar_convergencia(mejores, promedios)
