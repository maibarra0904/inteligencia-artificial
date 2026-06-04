# 📝 RESPUESTAS - Tarea 1: Algoritmos Genéticos (Problema de la Mochila)
> **Carrera de Computación - Sede Milagro**
> **Universidad Agraria del Ecuador**

---

## Pregunta 1 — Efecto de la Mutación

**¿Cómo se comporta el algoritmo si se cambia la tasa de mutación a un valor extremadamente alto (0.5) o extremadamente bajo (0.0)?**

### Tasa de mutación = 0.0 (sin mutación)

Cuando la tasa de mutación es `0.0`, el algoritmo depende **únicamente** del cruzamiento para generar diversidad. Esto provoca que la población converja rápidamente hacia los mejores individuos de la generación inicial, pero queda atrapada en un **óptimo local**. Si ningún individuo de la población inicial contiene un gen importante (por ejemplo, el bit del "Saco de dormir"), ese gen nunca podrá reaparecer. La gráfica de convergencia muestra una curva que sube en pocas generaciones y luego se aplana de forma definitiva, sin fluctuaciones. La solución encontrada puede ser subóptima, ya que la búsqueda queda limitada al espacio explorado desde el inicio.

### Tasa de mutación = 0.5 (mutación muy alta)

Con una tasa tan alta, aproximadamente la mitad de los genes de cada individuo se invierten en cada generación. Esto destruye la información que el cruzamiento y la selección intentan preservar. El algoritmo se comporta de forma casi aleatoria: el mejor fitness puede subir un poco en algunas generaciones, pero luego cae, porque las buenas soluciones son inmediatamente degradadas. La gráfica muestra una línea muy **irregular y ruidosa**, sin una tendencia clara de mejora. En este caso, el fitness promedio permanece bajo a lo largo de todas las generaciones.

### Conclusión

La mutación cumple el rol de **mecanismo de exploración**. Una tasa adecuada (como `0.05`) permite escapar de óptimos locales sin destruir las soluciones buenas. El equilibrio entre exploración (mutación) y explotación (selección + cruzamiento) es fundamental para que el algoritmo converja hacia buenas soluciones.

---

## Pregunta 2 — Presión de Selección (Tamaño del Torneo)

**¿Qué sucede si se incrementa el tamaño del torneo de k=3 a k=7?**

### Efecto sobre la diversidad

Con un torneo más grande (k=7), la probabilidad de que el mejor individuo de la población sea seleccionado en cada torneo aumenta considerablemente. Esto genera una **alta presión de selección**: los individuos con fitness alto dominan rápidamente la reproducción, mientras que los individuos mediocres o malos casi nunca son elegidos como padres. Como consecuencia, la diversidad genética de la población **disminuye** mucho más rápido. En pocas generaciones, la mayoría de los individuos son copias o variantes mínimas del mejor individuo encontrado.

### Efecto sobre la velocidad de convergencia

La convergencia es **más rápida** con k=7, ya que las buenas soluciones se propagan a toda la población en pocas generaciones. Sin embargo, esta velocidad tiene un costo: el algoritmo puede quedar atrapado prematuramente en un óptimo local antes de haber explorado suficiente el espacio de búsqueda. La gráfica muestra que el mejor fitness alcanza su valor máximo en menos generaciones, pero el fitness promedio también sube rápido y se estabiliza pronto, con poca variación entre generaciones posteriores.

### Comparación con k=3

| Característica | k=3 (torneo pequeño) | k=7 (torneo grande) |
|:---|:---:|:---:|
| Presión de selección | Moderada | Alta |
| Diversidad de la población | Mayor | Menor |
| Velocidad de convergencia | Más lenta | Más rápida |
| Riesgo de óptimo local | Bajo | Alto |

### Conclusión

Un tamaño de torneo intermedio (entre 3 y 5) suele ofrecer el mejor balance entre exploración y explotación para problemas de este tipo. Un torneo de k=7 es útil cuando el espacio de búsqueda es relativamente pequeño y se prioriza la velocidad sobre la exhaustividad.

---

## Pregunta 3 — Análisis de la Solución

### Mejor solución encontrada por el Algoritmo Genético

Con semilla `random.seed(42)` y los parámetros por defecto, el algoritmo encontró la siguiente combinación:

| Objeto | Peso (kg) | Valor (puntos) |
|:---|:---:|:---:|
| Saco de dormir | 3 | 80 |
| Linterna | 1 | 20 |
| Botiquín | 2 | 50 |
| Botella de agua | 4 | 70 |
| Brújula | 1 | 30 |
| Ropa de abrigo | 3 | 40 |
| **TOTAL** | **14 kg** | **290 puntos** |

### Máximo teórico por búsqueda de fuerza bruta

Con 8 objetos existen **2⁸ = 256** combinaciones posibles. Revisando todas ellas, el valor máximo alcanzable sin superar los 15 kg es también de **290 puntos**, logrado por dos combinaciones distintas:

- **Combinación A** (Peso = 15 kg): Saco de dormir + Botiquín + Botella de agua + Comida enlatada + Brújula → **290 puntos**
- **Combinación B** (Peso = 14 kg): Saco de dormir + Linterna + Botiquín + Botella de agua + Brújula + Ropa de abrigo → **290 puntos** *(esta es la que encontró el AG)*

### Comparación

| Métrica | Algoritmo Genético | Fuerza Bruta |
|:---|:---:|:---:|
| Mejor valor encontrado | 290 puntos | 290 puntos |
| Peso total | 14 kg | 15 kg (óptimo A) |
| Tiempo de búsqueda | O(generaciones × población) | O(2ⁿ) |
| ¿Encontró el óptimo global? | ✅ Sí | ✅ Sí |

### Conclusión

El algoritmo genético **encontró el óptimo global** (290 puntos), igualando al resultado de la fuerza bruta. Para este problema con solo 8 objetos, la fuerza bruta es perfectamente viable (256 combinaciones). Sin embargo, si el número de objetos creciera a 50 o más, la fuerza bruta se volvería computacionalmente imposible (2⁵⁰ ≈ 10¹⁵ combinaciones), mientras que el algoritmo genético seguiría encontrando buenas soluciones en tiempo razonable. Esto demuestra la **escalabilidad** como ventaja principal de los algoritmos evolutivos frente a métodos exhaustivos.
