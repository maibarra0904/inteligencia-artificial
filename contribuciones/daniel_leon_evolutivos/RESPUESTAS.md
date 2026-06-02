# RESPUESTAS - Tarea 1 Algoritmos Genéticos

## 1. Efecto de la Mutación

La tasa de mutación controla la diversidad genética de la población.  
Si la mutación es muy alta (ej. 0.5), el algoritmo se vuelve inestable porque los individuos cambian demasiado y no logra converger a buenas soluciones.  
Si la mutación es muy baja (ej. 0.0), la población pierde diversidad y puede quedarse atrapada en soluciones subóptimas sin mejorar.

---

## 2. Presión de Selección (Torneo)

Al aumentar el tamaño del torneo (por ejemplo de 3 a 7), se incrementa la presión de selección.  
Esto significa que los mejores individuos tienen más probabilidad de ser elegidos, lo que acelera la convergencia.  
Sin embargo, también reduce la diversidad genética, lo que puede causar convergencia prematura a soluciones no óptimas.

---

## 3. Análisis de la Solución

El algoritmo encontró una solución con un valor total de **290 puntos** y un peso de **14 kg**.

Los objetos seleccionados fueron:
- Saco de dormir
- Linterna
- Botiquín
- Botella de agua
- Brújula
- Ropa de abrigo

Este resultado es cercano al óptimo para este conjunto de objetos y capacidad de mochila.

Una búsqueda por fuerza bruta confirmaría que esta combinación es una de las mejores posibles, ya que maximiza el valor sin exceder la capacidad.