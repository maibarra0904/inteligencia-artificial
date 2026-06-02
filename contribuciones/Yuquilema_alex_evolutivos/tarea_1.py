import random
import matplotlib.pyplot as plt

Objetos = [

    ("Saco de dormir",     3,  80),
    ("Limterna      ",     1,  20),
    ("Botiquin"      ,     2,  50),
    ("Botella de agua",    4,  70),
    ("Comida enlatada   ", 5,  60),
    ("Tienda de comapaña", 7, 100),
    ("Brujula ",           1,  30),
    ("Ropa de dormir ",    3,  40),
]

Capacidad_Maxima = 15
  

Tamaño_poblacion = 20   # Se crean 20 mochilas iniciales.

Tasa_cruzamiento = 0.8  # Probabilidad (80%) de cruzar dos padres para generar hijos.

Tasa_mutacion = 0.05    # Probabilidad (5%) de mutar cada gen de una mochila hija.

Tamano_torneo = 3       # Para seleccionar un padre:
                        # se eligen 3 mochilas al azar y gana la de mejor fitness.
                        # Se repite el proceso para obtener el segundo padre.

Generaciones = 50       # Se repiten 50 rondas evolutivas.
                        # En cada ronda:
                        # 1. Selección
                        # 2. Cruzamiento
                        # 3. Mutación
                        # 4. Creación de una nueva población de 20 mochilas
                        # La nueva población pasa a la siguiente generación.


def  objeto_invidio ():
    return [random.randint(0,1)for _ in range(len(Objetos))]        
# Crea una mochila aleatoria| Ejemplo: [0, 1, 1, 0, 0, 1, 0, 1] = mochila 1 .

################################################################################

def poblacion(tamano):
    return [objeto_invidio() for _ in range(tamano)]
# crea una lista  de datos para almacenar las 20 mochilas: ejemplo

#  tamano [
#       [0, 1, 1, 0, 0, 1, 0, 1] = mochila 1
#       [0, 1, 1, 0, 0, 1, 0, 1] = mochila 2
#       [0, 1, 1, 0, 0, 1, 0, 1] = mochila 3
#       ]

###############################################################################
def evaluar_firness (objeto):
    peso_total = 0
    valor_total = 0

    for i , gen in enumerate(objeto):
        if gen == 1:
            peso_total += Objetos[i][1]
            valor_total += Objetos[i][2]
    
    if peso_total > Capacidad_Maxima:
        return 0 
    return valor_total

# En resumen, este bloque de código:
#
# Recibe una mochila
#        ↓
# Calcula el peso total
#        ↓
# Calcula el valor total
#        ↓
# ¿Peso > 15 kg?
#        ↓
#    Sí      No
#    ↓        ↓
# return 0  return valor_total
#
######################################################################################
def selecciona_torneo(poblacion,Fitnesses, k=3):

    seleccionados = random.sample(range(len(poblacion)),k)
    mejor_mochila = max(seleccionados, key=lambda idx:Fitnesses[idx])

    return list(poblacion[mejor_mochila])

# En resumen, este bloque de código:
#
# Escoge 3 mochilas al azar de la población
#          ↓
# Calcula o consulta el fitness (valor) de cada mochila
#          ↓
# Ejemplo:
# Mochila_4  = 180
# Mochila_11 = 320
# Mochila_17 = 250
#          ↓
# Compara los fitness de las 3 mochilas
#          ↓
# Gana la mochila con el mayor fitness
#          ↓
# Gana Mochila_11 = 320
#          ↓
# Mochila_11 es seleccionada como padre para la siguiente etapa
# (cruzamiento).
#
# Este proceso se conoce como selección por torneo (tamaño = 3).

#########################################################################################

def cruzamineto (padre_1 , padre_2):
    if random.random() < Tasa_cruzamiento:
        punto = random.randint(1,len(Objetos)-1)

        hijo_1 = padre_1[:punto] + padre_2 [punto:]
        hijo_2 = padre_2[:punto] + padre_1 [punto:]
        return hijo_1, hijo_2
    else:
        return list(padre_1), list(padre_2)
    # En resumen, este bloque de código:
#
# Se seleccionan dos mochilas padre mediante el proceso de selección.
#
# Padre1: [1,1,1,0 | 0,0,1,0]  (mochila_11)
# Padre2: [0,0,0,1 | 1,1,0,1]  (mochila_8)
#
#                 ↓
# Se elige un punto de corte para realizar el cruzamiento.
#
# Padre1: [1,1,1,0 | 0,0,1,0]
# Padre2: [0,0,0,1 | 1,1,0,1]
#
#                 ↓
# Se intercambian las partes derechas de ambos padres.
#
# Hijo1 : [1,1,1,0 | 1,1,0,1]
# Hijo2 : [0,0,0,1 | 0,0,1,0]
#
#                 
# Se generan dos nuevas mochilas (hijos) que combinan
# características de ambos padres.
#
# Hijo1 = nueva mochila generada a partir de Padre1 y Padre2
# Hijo2 = nueva mochila generada a partir de Padre2 y Padre1
#
# Este proceso se conoce como cruzamiento de un punto (One-Point Crossover).

#########################################################################################

def cruzamiento (padre_1 , padre_2):
    if random.random() < Tasa_cruzamiento:
        punto = random.randint(1,len(Objetos)-1)

        hijo_1 = padre_1[:punto] + padre_2 [punto:]
        hijo_2 = padre_2[:punto] + padre_1 [punto:]
        return hijo_1, hijo_2
    else:
        return list(padre_1), list(padre_2)

# Esta función realiza el cruzamiento entre dos mochilas padre.
# Con una probabilidad del 80% (Tasa_cruzamiento), selecciona
# un punto de corte aleatorio e intercambia parte de los genes
# de ambos padres para generar dos nuevas mochilas (hijos).
# Si no ocurre el cruzamiento, los hijos son copias exactas
# de los padres.

#############################################################################

def mutaciones (inviduio):
    mutado = list(inviduio)
    for i in range(len(mutado)):
        if random.random() < Tasa_mutacion:
            mutado[i] = 1 - mutado[i]
    return mutado
# La mutación modifica aleatoriamente algunos 0 y 1 de la mochila 
# para generar nuevas combinaciones de objetos.

################################################################################

def ejecutar_algoritmo_genetico ():
    crea_poblacion = poblacion(Tamaño_poblacion)
    historial_mejor_fitnes = []
    historial_fitnes_promedio = []


    mejor_solicion_global = None 
    mejor_fitness_global = -1

    print("--- Iniciando Simulacion Evolutiva")

    for gen in range(Generaciones):
        fitnesses = [evaluar_firness(ind) for ind in crea_poblacion]

        mejor_fit = max(fitnesses)
        promedio_fit =sum(fitnesses)/ len(fitnesses)

        historial_mejor_fitnes.append(mejor_fit)
        historial_fitnes_promedio.append(promedio_fit)


        mejor_ind_gen = crea_poblacion[fitnesses.index(mejor_fit)]
        if mejor_fit > mejor_fitness_global:
            mejor_fitness_global =mejor_fit
            mejor_solucion_global = list(mejor_ind_gen)

        print(f"Generacion {gen+1:02d}: Mejor Fitness = {mejor_fit}")
    
    
    
        nueva_poblacion = []

        while len( nueva_poblacion) < Tamaño_poblacion:
            padre_1 = selecciona_torneo(crea_poblacion,fitnesses,Tamano_torneo)
            padre_2 = selecciona_torneo(crea_poblacion,fitnesses,Tamano_torneo)
        
            hijo_1,hijo_2 = cruzamiento(padre_1,padre_2)

            nueva_poblacion.append(mutaciones(hijo_1))
            if len(nueva_poblacion) < Tamaño_poblacion:
                nueva_poblacion.append(mutaciones(hijo_2))

        crea_poblacion = nueva_poblacion

    print("\n--- Simulación Finalizada ---")
    print(f"Mejor Aptitud Encontrada: {mejor_fitness_global} puntos")

    peso_solucion = 0
    print("\nObjetos seleccionados en la mejor mochila:")
    for i, gen in enumerate(mejor_solucion_global):
        if gen == 1:
            nombre, peso , valor = Objetos[i]
            peso_solucion += peso 
            print(f" - {nombre} |Peso: {peso} kg | valor: {valor} | puntos ")

    print(f"Peso Total: {peso_solucion} kg | {Capacidad_Maxima} kg")

    return historial_mejor_fitnes,historial_fitnes_promedio

def graficar_convergencia(mejores, promedios):
    plt.figure(figsize=(10,6))
    plt.plot(mejores, label="Mejor Aptitud (Fitness)", color="forestgreen", linewidth=2)
    plt.plot(promedios, label="Aptitud Promedio de la Población", color="royalblue", linestyle="--")
    plt.xlabel("Generación")
    plt.ylabel("Aptitud (Valor total en la Mochila)")
    plt.title("Convergencia del Algoritmo Genético")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)

     # Guardar gráfica
    plt.savefig("evolucion_fitness.png")
    print("\n[Éxito] Gráfica de convergencia guardada como 'evolucion_fitness.png'")
    plt.show()

if __name__ == "__main__":
    # Asegurar reproducibilidad para comparar
    random.seed(42)
    
    mejores, promedios = ejecutar_algoritmo_genetico()
    graficar_convergencia(mejores, promedios)