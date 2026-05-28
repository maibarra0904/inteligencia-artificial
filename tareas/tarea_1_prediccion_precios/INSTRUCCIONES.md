# 🏠 Tarea 1: Predicción de Precios de Viviendas (Regresión Lineal)
> **Módulo: Introducción al Aprendizaje Supervisado**
> **Curso de Python - UNIR**

En esta tarea práctica, implementarás un modelo de **Regresión Lineal Múltiple** para predecir el precio de viviendas basándose en características clave (tamaño, número de habitaciones, antigüedad y ubicación). 

El objetivo es familiarizarse con el flujo de trabajo típico de Machine Learning en Python utilizando las librerías **Pandas**, **Numpy**, **Matplotlib** y **Scikit-Learn**.

---

## 🎯 Objetivos de Aprendizaje
1. Cargar e inspeccionar datos estructurados en formato CSV usando `pandas`.
2. Dividir un conjunto de datos en subconjuntos de **entrenamiento (train)** y **prueba (test)**.
3. Entrenar y ajustar un modelo de regresión lineal.
4. Evaluar el desempeño del modelo usando métricas clave como el **Error Cuadrático Medio (MSE)** y el **Coeficiente de Determinación ($R^2$)**.
5. Analizar el impacto y la importancia de cada variable a través de sus coeficientes.

---

## 📂 Archivos en esta Tarea
* `datos_viviendas.csv`: Dataset con 15 registros de viviendas (área, habitaciones, edad, distancia al centro y precio en miles de USD).
* `plantilla_tarea_1.py`: Archivo de script de Python que contiene la estructura básica y las funciones con etiquetas `# TODO` que debes implementar.

---

## 🛠️ Instrucciones de Entrega y Flujo Colaborativo

1. **Crear una rama de trabajo:**
   Abre tu consola de comandos en el directorio del proyecto y ejecuta:
   ```bash
   git checkout -b tarea1-tu_nombre_apellido
   ```
2. **Crear tu carpeta de entrega:**
   Copia la plantilla `plantilla_tarea_1.py` y el dataset `datos_viviendas.csv` a una nueva subcarpeta dentro de `contribuciones/`:
   ```text
   contribuciones/tu_nombre_apellido/
   ├── tarea_1.py
   └── datos_viviendas.csv
   ```
3. **Completar la Tarea:**
   Trabaja sobre tu archivo `contribuciones/tu_nombre_apellido/tarea_1.py` completando todos los bloques de código marcados con `# TODO`.
4. **Instalar Dependencias:**
   Asegúrate de tener instaladas las dependencias del curso:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
   ```
5. **Ejecutar y Validar:**
   Ejecuta tu archivo y valida que se genere la gráfica de resultados:
   ```bash
   python tarea_1.py
   ```
6. **Subir los cambios y abrir Pull Request (PR):**
   Envía tu rama a GitHub y abre un Pull Request hacia la rama `main` original. Recuerda etiquetar a al menos un compañero de clase para que actúe como revisor (Reviewer).

---

## 📝 Preguntas de Análisis (Para tu Entrega)
Agrega un archivo `RESPUESTAS.md` dentro de tu carpeta `contribuciones/tu_nombre_apellido/` y responde de manera justificada a las siguientes preguntas basándote en los resultados que obtengas al entrenar tu modelo:

1. **Interpretación de Coeficientes:** ¿Cuál de las variables predictoras (metros cuadrados, habitaciones, antigüedad o distancia al centro) tiene la mayor influencia positiva en el precio de la vivienda? ¿Cuál tiene la mayor influencia negativa? ¿Tiene sentido intuitivo?
2. **Evaluación de Métricas:** ¿Qué indica el coeficiente de determinación ($R^2$) obtenido? Explica detalladamente qué significa su valor cercano a 1 o cercano a 0 en el contexto de tu modelo.
3. **Reflexión sobre los Datos:** El dataset provisto contiene solo 15 registros. Si este modelo fuera a utilizarse para predecir precios en la vida real, ¿qué problemas o sesgos consideras que presentaría y cómo los solucionarías?

---
*¡Mucho éxito en tu primera práctica de IA! Si tienes dudas, abre un "Issue" en el repositorio para que tus compañeros o el profesor puedan ayudarte.*
