# 🧬 Tarea 1: Optimización con Algoritmos Genéticos (Problema de la Mochila)
> **Módulo: Algoritmos Evolutivos y Optimización**
> **Curso de Python - UNIR**

En esta tarea práctica, diseñarás e implementarás un **Algoritmo Genético (AG)** básico para resolver el clásico **Problema de la Mochila (Knapsack Problem)**. Este problema de optimización combinatoria consiste en seleccionar un subconjunto de objetos (cada uno con un peso y valor específicos) para maximizar el valor total sin exceder la capacidad máxima de peso de la mochila.

El objetivo es comprender los fundamentos de la computación evolutiva mediante la simulación de procesos de selección natural, cruzamiento y mutación.

---

## 🎯 Objetivos de Aprendizaje
1. Comprender la representación cromosómica (codificación binaria) de un problema de optimización.
2. Diseñar e implementar una **Función de Aptitud (Fitness Function)** con penalizaciones por restricciones de peso.
3. Implementar operadores evolutivos clave: **Selección** (por torneo), **Cruzamiento** (un punto) y **Mutación**.
4. Simular el ciclo de vida evolutivo a lo largo de varias generaciones.
5. Analizar la convergencia del algoritmo mediante la visualización de la evolución de la aptitud a lo largo del tiempo.

---

## 📂 Archivos en esta Tarea
* `plantilla_tarea_1.py`: Archivo de script de Python que contiene la estructura básica del algoritmo genético y las funciones con etiquetas `# TODO` que debes implementar.

---

## 🎒 Definición del Problema
Imagina que vas a realizar una expedición y tienes una mochila con una capacidad máxima de **15 kg**. Tienes a tu disposición los siguientes objetos:

| Objeto | Peso (kg) | Valor (Puntos) |
| :--- | :---: | :---: |
| 1. Saco de dormir | 3 | 80 |
| 2. Linterna | 1 | 20 |
| 3. Botiquín | 2 | 50 |
| 4. Botella de agua | 4 | 70 |
| 5. Comida enlatada | 5 | 60 |
| 6. Tienda de campaña | 7 | 100 |
| 7. Brújula | 1 | 30 |
| 8. Ropa de abrigo | 3 | 40 |

### Representación del Cromosoma
Cada individuo (solución candidata) se representará como un vector binario (lista de 0s y 1s) de longitud 8.
* Un `1` indica que el objeto correspondiente está en la mochila.
* Un `0` indica que el objeto se queda fuera.
* *Ejemplo:* `[1, 0, 1, 1, 0, 0, 1, 0]` representa una mochila con el Saco de dormir, Botiquín, Botella de agua y Brújula. Peso total = 10 kg, Valor total = 230 puntos.

---

## 🛠️ Instrucciones de Entrega y Flujo Colaborativo

1. **Crear una rama de trabajo:**
   ```bash
   git checkout -b tarea1-evolutivos-tu_nombre_apellido
   ```
2. **Crear tu carpeta de entrega:**
   Copia la plantilla `plantilla_tarea_1.py` a una nueva subcarpeta dentro de `contribuciones/`:
   ```text
   contribuciones/tu_nombre_apellido_evolutivos/
   └── tarea_1.py
   ```
3. **Completar la Tarea:**
   Trabaja sobre tu archivo completando todos los bloques de código marcados con `# TODO`.
4. **Ejecutar y Validar:**
   Ejecuta tu archivo y valida que se genere la gráfica de convergencia (`evolucion_fitness.png`):
   ```bash
   python tarea_1.py
   ```
5. **Subir los cambios y abrir Pull Request (PR):**
   Envía tu rama a GitHub y abre un Pull Request hacia la rama `main` original.

---

## 📝 Preguntas de Análisis (Para tu Entrega)
Agrega un archivo `RESPUESTAS.md` dentro de tu carpeta `contribuciones/tu_nombre_apellido_evolutivos/` y responde a las siguientes preguntas basándote en los resultados de tu simulación:

1. **Efecto de la Mutación:** Si cambias la tasa de mutación a un valor extremadamente alto (ej. `0.5`) o extremadamente bajo (ej. `0.0`), ¿cómo se comporta la gráfica de convergencia y la calidad de la mejor solución encontrada? Explica el fenómeno.
2. **Presión de Selección:** En la plantilla implementamos la selección por torneo. ¿Qué sucede si incrementas el tamaño del torneo (ej. de 3 a 7)? ¿Cómo afecta esto a la diversidad de la población y a la velocidad de convergencia?
3. **Análisis de la Solución:** ¿Cuál es la mejor combinación de objetos que encontró tu algoritmo? ¿Cuál es su peso total y su valor? Compara este resultado con el máximo teórico si hicieras una búsqueda por fuerza bruta.
