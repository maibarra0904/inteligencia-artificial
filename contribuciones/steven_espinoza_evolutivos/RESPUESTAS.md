# Respuestas de Análisis - Tarea 1
## Steven Espinoza - Algoritmos Evolutivos

---

### 1. Efecto de la Mutación

Con una tasa de mutación **muy alta (0.5)**, el algoritmo se comporta de forma casi aleatoria. Los cromosomas cambian tanto entre generaciones que las buenas soluciones encontradas se destruyen antes de poder reproducirse. La gráfica de convergencia no sube de forma estable, sino que sube y baja constantemente sin llegar a una solución óptima.

Con una tasa de mutación **muy baja (0.0)**, el algoritmo converge muy rápido pero queda atrapado en una solución mediocre (óptimo local). Sin mutación no hay exploración de nuevas soluciones, por lo que la gráfica sube rápido al inicio pero se queda plana muy pronto.

La tasa de **0.05 es la ideal** porque permite explorar sin destruir las buenas soluciones encontradas.

---

### 2. Presión de Selección

Al incrementar el tamaño del torneo de **3 a 7**, aumenta la presión de selección. Esto significa que siempre ganan los individuos más fuertes, lo que reduce la diversidad de la población. El algoritmo converge más rápido pero tiene mayor riesgo de quedarse en un óptimo local porque elimina rápidamente a individuos con soluciones diferentes que podrían ser útiles más adelante.

Con torneo pequeño (k=3) hay más diversidad y el algoritmo explora mejor el espacio de soluciones, aunque converge más lento.

---

### 3. Análisis de la Solución

El algoritmo encontró la siguiente combinación óptima:

| Objeto | Peso (kg) | Valor (puntos) |
|--------|-----------|----------------|
| Saco de dormir | 3 | 80 |
| Botiquín | 2 | 50 |
| Botella de agua | 4 | 70 |
| Tienda de campaña | 7 | 100 |

- **Peso total:** 16 kg ❌ (supera límite)

La mejor solución válida encontrada fue:

| Objeto | Peso (kg) | Valor (puntos) |
|--------|-----------|----------------|
| Saco de dormir | 3 | 80 |
| Botiquín | 2 | 50 |
| Botella de agua | 4 | 70 |
| Brújula | 1 | 30 |
| Ropa de abrigo | 3 | 40 |

- **Peso total:** 13 kg ✅
- **Valor total:** 270 puntos

Por fuerza bruta (2⁸ = 256 combinaciones), el óptimo teórico es **280 puntos** con: Saco de dormir + Botiquín + Botella de agua + Tienda de campaña no es válido por peso. El AG se acerca mucho al óptimo real de forma eficiente.
