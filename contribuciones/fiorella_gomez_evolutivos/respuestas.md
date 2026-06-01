Efecto de la Mutación: Si cambias la tasa de mutación a un valor extremadamente alto (ej. 0.5) o extremadamente bajo (ej. 0.0), ¿cómo se comporta la gráfica de convergencia y la calidad de la mejor solución encontrada? Explica el fenómeno.
Si se cambia la mutación a 0.0, el algoritmo converge muy rápido y la aptitud promedio junto con la mejor aptitud alcanzan los 290 puntos en las primeras generaciones y permanecen constantes.
Si se cambia la mutación a 0.5, la gráfica muestra fuertes oscilaciones tanto en la aptitud promedio como en la mejor aptitud.
Una mutación muy baja favorece la explotación de buenas soluciones, mientras que una mutación muy alta introduce demasiada aleatoriedad y dificulta la convergencia.

Presión de Selección: En la plantilla implementamos la selección por torneo. ¿Qué sucede si incrementas el tamaño del torneo (ej. de 3 a 7)? ¿Cómo afecta esto a la diversidad de la población y a la velocidad de convergencia?
Si se incrementa el tamaño del torneo a 7, los individuos con mayor aptitud tienen más probabilidad de ser seleccionados y la convergencia es más rápida porque las mejores características se propagan con mayor facilidad, pero la diversidad genética se disminuye. Entonces, un torneo más grande acelera la convergencia pero reduce la diversidad de la población.

Análisis de la Solución: ¿Cuál es la mejor combinación de objetos que encontró tu algoritmo? ¿Cuál es su peso total y su valor? Compara este resultado con el máximo teórico si hicieras una búsqueda por fuerza bruta.
La mejor combinación de objetos fue:
 - Saco de dormir (Peso: 3 kg | Valor: 80 puntos)
 - Linterna (Peso: 1 kg | Valor: 20 puntos)
 - Botiquín (Peso: 2 kg | Valor: 50 puntos)
 - Botella de agua (Peso: 4 kg | Valor: 70 puntos)
 - Brújula (Peso: 1 kg | Valor: 30 puntos)
 - Ropa de abrigo (Peso: 3 kg | Valor: 40 puntos)
El peso total fue de 14 kg.
El valor fue de 290 puntos.

Si se hiciera por fuerza bruta, analizando las 256 combinaciones posibles, se obtendría el mismo resultado. Esto quiere decir que el algoritmo encontró la solución óptima global que es de 290 punto como valor máximo posible.