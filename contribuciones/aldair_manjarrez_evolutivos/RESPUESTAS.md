# Análisis - Tarea 1: Algoritmo Genético #

## Pregunta 1: Efecto de la Mutación ##
Si cambias la tasa de mutación a un valor extremadamente alto (ej. 0.5) o extremadamente bajo (ej. 0.0), ¿cómo se comporta la gráfica de convergencia y la calidad de la mejor solución encontrada? Explica el fenómeno.

- Con 0.5: una tasa muy alta de mutación genera muchos cambios aleatorios en los individuos. Esto puede hacer que la gráfica de convergencia sea más ruidosa, con saltos grandes entre generaciones, y dificulta que el algoritmo mantenga soluciones buenas estables. A veces mejora la exploración, pero también perjudica la calidad final porque las soluciones buenas se destruyen con frecuencia.
- Con 0.0: sin mutación, el algoritmo pierde capacidad para explorar nuevas soluciones fuera de los descendientes directos de los padres. La gráfica tiende a estabilizarse rápido, pero el mejor valor puede quedar atrapado en un óptimo local. En este caso la calidad de la mejor solución rara vez mejora tras las primeras generaciones.

## Pregunta 2: Presión de Selección ##
En la plantilla implementamos la selección por torneo. ¿Qué sucede si incrementas el tamaño del torneo (ejemplo: de 3 a 7)? ¿Cómo afecta esto a la diversidad de la población y a la velocidad de convergencia? 

- Cambios en la gráfica: al aumentar el tamaño del torneo a 7, la selección favorece aún más a los individuos con mayor fitness. La gráfica mostraría una convergencia más rápida hacia un valor alto, porque los mejores ejemplares se reproducen más seguido.
- Efecto en la diversidad: un torneo más grande reduce la diversidad de la población, porque los individuos débiles tienen menos probabilidades de ser seleccionados. Esto aumenta el riesgo de que el algoritmo se estanque en soluciones subóptimas y pierda capacidad de exploración.

## Pregunta 3: Solución Encontrada ##
¿Cuál es la mejor combinación de objetos que encontró tu algoritmo? ¿Cuál es su peso total y su valor? Compara este resultado con el máximo teórico si hicieras una búsqueda por fuerza bruta.

- Objetos seleccionados:
  - Saco de dormir (3 kg, 80 puntos)
  - Linterna (1 kg, 20 puntos)
  - Botiquín (2 kg, 50 puntos)
  - Botella de agua (4 kg, 70 puntos)
  - Brújula (1 kg, 30 puntos)
  - Ropa de abrigo (3 kg, 40 puntos)
- Peso total: 14 kg
- Valor total: 290 puntos

### Comparación con fuerza bruta ###
El valor máximo teórico encontrado por búsqueda exhaustiva es también **290 puntos**. Una combinación óptima teórica diferente es:
- Saco de dormir, Botiquín, Botella de agua, Comida enlatada, Brújula

Esa combinación tiene peso **15 kg** y valor **290 puntos**. Por lo tanto, tu algoritmo alcanzó el valor óptimo máximo permitido, aunque con una selección distinta de objetos.
