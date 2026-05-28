#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Plantilla de Tarea 1: Predicción del Precio de Viviendas
Curso de Python - UNIR

Instrucciones:
1. Complete los bloques de código marcados con "# TODO".
2. Ejecute el archivo para entrenar su modelo y ver los resultados.
3. Responda a las preguntas de análisis en el archivo INSTRUCCIONES.md o en su entrega.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def cargar_datos(ruta_archivo):
    """
    Carga el conjunto de datos CSV utilizando pandas.
    """
    print(f"--- Cargando datos desde {ruta_archivo} ---")
    # TODO: Utilice pandas para leer el archivo CSV y retorne el DataFrame
    df = None
    return df

def analizar_datos(df):
    """
    Realiza un análisis descriptivo básico del conjunto de datos.
    """
    print("\n--- Análisis Descriptivo Inicial ---")
    if df is not None:
        # TODO: Imprima las primeras 5 filas del DataFrame
        
        # TODO: Muestre información general del DataFrame (tipos de datos, no nulos) con df.info()
        
        # TODO: Muestre las estadísticas descriptivas del DataFrame (df.describe())
        
        pass
    else:
        print("El DataFrame está vacío. Asegúrese de implementar cargar_datos.")

def preparar_datos(df):
    """
    Separa las variables independientes (X) de la variable objetivo (y),
    y realiza la división en conjuntos de entrenamiento y prueba (train/test split).
    """
    print("\n--- Preparando datos para entrenamiento ---")
    if df is not None:
        # TODO: Defina las variables predictoras (X) y la variable objetivo (y)
        # Predictoras: metros_cuadrados, habitaciones, antiguedad_anos, distancia_centro_km
        # Objetivo: precio_miles_usd
        X = None
        y = None
        
        # TODO: Divida el conjunto de datos en 80% entrenamiento y 20% prueba.
        # Use random_state=42 para que los resultados sean reproducibles.
        X_train, X_test, y_train, y_test = None, None, None, None
        
        return X_train, X_test, y_train, y_test
    return None, None, None, None

def entrenar_modelo(X_train, y_train):
    """
    Crea y entrena un modelo de Regresión Lineal.
    """
    print("\n--- Entrenando el Modelo de Regresión Lineal ---")
    # TODO: Inicialice el objeto del modelo LinearRegression de scikit-learn
    modelo = None
    
    # TODO: Entrene (ajuste) el modelo con los datos de entrenamiento (X_train, y_train)
    
    return modelo

def evaluar_modelo(modelo, X_test, y_test):
    """
    Realiza predicciones en el conjunto de prueba y calcula métricas de rendimiento.
    """
    print("\n--- Evaluación del Modelo ---")
    if modelo is not None and X_test is not None:
        # TODO: Realice las predicciones sobre el conjunto X_test
        predicciones = None
        
        # TODO: Calcule el Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R²)
        mse = None
        r2 = None
        
        print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
        print(f"Coeficiente de Determinación (R²): {r2:.2f}")
        
        # Imprimir los coeficientes (pesos) del modelo
        print("\nCoeficientes del modelo:")
        for col, coef in zip(X_test.columns, modelo.coef_):
            print(f" - {col}: {coef:.4f}")
        print(f" - Intercepto (Sesgo): {modelo.intercept_:.4f}")
        
        return predicciones
    else:
        print("El modelo o los datos no están disponibles para evaluación.")
        return None

def graficar_resultados(y_real, y_pred):
    """
    Dibuja un gráfico de dispersión comparando los valores reales frente a los predichos.
    """
    if y_real is not None and y_pred is not None:
        plt.figure(figsize=(8, 6))
        # TODO: Realice un scatter plot (gráfico de dispersión) de los valores reales vs predichos
        
        # Línea de referencia ideal (diagonal perfecta)
        min_val = min(min(y_real), min(y_pred))
        max_val = max(max(y_real), max(y_pred))
        plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='Predicción Perfecta')
        
        plt.xlabel('Valores Reales (miles USD)')
        plt.ylabel('Valores Predichos (miles USD)')
        plt.title('Regresión Lineal: Reales vs Predichos')
        plt.legend()
        plt.grid(True)
        
        # Guardar la gráfica como imagen
        plt.savefig('grafica_predicciones.png')
        print("\n[Éxito] Gráfica guardada como 'grafica_predicciones.png'")
        plt.show()

# --- Bloque Principal de Ejecución ---
if __name__ == "__main__":
    ruta_dataset = "datos_viviendas.csv"
    
    # 1. Cargar datos
    datos = cargar_datos(ruta_dataset)
    
    # 2. Analizar datos
    analizar_datos(datos)
    
    # 3. Preparar datos
    X_train, X_test, y_train, y_test = preparar_datos(datos)
    
    # Proceder solo si se implementó correctamente la preparación
    if X_train is not None:
        # 4. Entrenar modelo
        modelo_entrenado = entrenar_modelo(X_train, y_train)
        
        # 5. Evaluar modelo
        predicciones = evaluar_modelo(modelo_entrenado, X_test, y_test)
        
        # 6. Graficar resultados
        # Convertimos y_test a un array de numpy para evitar problemas de índices con el plot
        if predicciones is not None:
            graficar_resultados(y_test.values, predicciones)
