1. Efecto de Mutación
   Una vez se aumente la tasa de mutación a 0.5, los genes cambian en cada generacion
  ,lo mismo que genera que las soluciones encontradas puedan ser modificadas constantemente
  haciendo que sea mas dificil que el algoritmo pueda conservar individuos de calidad alta.
  Lo que generaria una convergencia que podria presentar fluctuaciones y dara una solucion menos adecuada.
  En caso de que la tasa de mutacion se de 0.0, no podrian generarse nuevas variaciones
  geneticas y el algoritmo converge de forma rapida pero en esta existiria el riesgo
  de que se quede atrapado a falta de diversidad de poblacion. Es decir si se tiene una tasa
  moderada de mutacion se puede equilibrar la exploracion de solucioness nuevas.
2. Presión de Selección
   Una seleccion por torneo favorece a individuos de mejor aptitud, es decir que cuando el
   tamano del torneo aumenta de 3 a 7 la presion de seleccion aumenta. Generaria que
   los mejores individuos con mayor frecuencia aceleren la convergencia del algoritmo.
   En cambio la diversidad genetica disminuye rapidamente y aumenta la probabilidad de convergencia.
   Si fuera un torneo mas pequeño se puede mantener una mayor diversidad genetica y mas lenta.
3. Análisis de la Solución
   La mejor combinacion fue la de una mochila con capacidad maxima de 15 kg
   Saco de dormir (peso=3kg, puntos= 80)
   Botiquín (peso=2 kg, puntos=50)
   Botella de agua (peso=4 kg, puntos= 70)
   Comida enlatada (peso=5 kg, puntos=60)
   Brújula (peso=1 kg, puntos=30)
   peso total= 3+2+4+5+1=15
   valor total= 80+50+70+60+30=290
   2⁸ = 256 total combinaciones
   Una vez se evaluan 256 combianciones se obtiene un valor maximo alcanzable sin necesidad de superar
   los 15kg y es de 290 puntos. Entonces el algortimo generico logro encontrar la solucion optima
   de forma general obteniendo un mismo resultado de una busqueda exhaustiva, solo que usando un
   proceso evolutivo, usando seleccion, cruzamiento y mutacion.
   
