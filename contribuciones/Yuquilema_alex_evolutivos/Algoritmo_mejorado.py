import random
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt

# ==========================================================
# DATOS DEL PROBLEMA
# ==========================================================

Objetos = [
    ("Saco de dormir",     3,  80),
    ("Linterna",           1,  20),
    ("Botiquin",           2,  50),
    ("Botella de agua",    4,  70),
    ("Comida enlatada",    5,  60),
    ("Tienda de campaña",  7, 100),
    ("Brujula",            1,  30),
    ("Ropa de dormir",     3,  40),
]

Capacidad_Maxima = 15

# Valores iniciales
Tamaño_poblacion = 20
Tasa_cruzamiento = 0.8
Tasa_mutacion = 0.05
Tamano_torneo = 3
Generaciones = 50


# ==========================================================
# ALGORITMO GENETICO
# ==========================================================

def objeto_individuo():
    return [random.randint(0, 1) for _ in range(len(Objetos))]


def poblacion(tamano):
    return [objeto_individuo() for _ in range(tamano)]


def evaluar_fitness(objeto):

    peso_total = 0
    valor_total = 0

    for i, gen in enumerate(objeto):

        if gen == 1:
            peso_total += Objetos[i][1]
            valor_total += Objetos[i][2]

    if peso_total > Capacidad_Maxima:
        return 0

    return valor_total


def seleccion_torneo(poblacion_actual, fitnesses, k):

    seleccionados = random.sample(range(len(poblacion_actual)), k)

    mejor = max(
        seleccionados,
        key=lambda idx: fitnesses[idx]
    )

    return list(poblacion_actual[mejor])


def cruzamiento(padre_1, padre_2):

    if random.random() < Tasa_cruzamiento:

        punto = random.randint(1, len(Objetos) - 1)

        hijo_1 = padre_1[:punto] + padre_2[punto:]
        hijo_2 = padre_2[:punto] + padre_1[punto:]

        return hijo_1, hijo_2

    return list(padre_1), list(padre_2)


def mutacion(individuo):

    mutado = list(individuo)

    for i in range(len(mutado)):

        if random.random() < Tasa_mutacion:
            mutado[i] = 1 - mutado[i]

    return mutado


def ejecutar_algoritmo_genetico():

    poblacion_actual = poblacion(Tamaño_poblacion)

    historial_mejor = []
    historial_promedio = []

    registro_generaciones = []

    mejor_fitness_global = -1
    mejor_solucion_global = None

    print("\n--- INICIANDO SIMULACION ---\n")

    for gen in range(Generaciones):

        fitnesses = [
            evaluar_fitness(ind)
            for ind in poblacion_actual
        ]

        mejor_fit = max(fitnesses)
        promedio_fit = sum(fitnesses) / len(fitnesses)

        historial_mejor.append(mejor_fit)
        historial_promedio.append(promedio_fit)

        texto_generacion = (
            f"Generacion {gen+1:02d}: "
            f"Mejor Fitness = {mejor_fit}"
        )

        registro_generaciones.append(texto_generacion)

        print(texto_generacion)

        mejor_ind = poblacion_actual[
            fitnesses.index(mejor_fit)
        ]

        if mejor_fit > mejor_fitness_global:
            mejor_fitness_global = mejor_fit
            mejor_solucion_global = list(mejor_ind)

        nueva_poblacion = []

        while len(nueva_poblacion) < Tamaño_poblacion:

            padre_1 = seleccion_torneo(
                poblacion_actual,
                fitnesses,
                Tamano_torneo
            )

            padre_2 = seleccion_torneo(
                poblacion_actual,
                fitnesses,
                Tamano_torneo
            )

            hijo_1, hijo_2 = cruzamiento(
                padre_1,
                padre_2
            )

            nueva_poblacion.append(
                mutacion(hijo_1)
            )

            if len(nueva_poblacion) < Tamaño_poblacion:
                nueva_poblacion.append(
                    mutacion(hijo_2)
                )

        poblacion_actual = nueva_poblacion

    peso_total = 0
    objetos_seleccionados = []

    if mejor_solucion_global is not None:
        for i, gen in enumerate(mejor_solucion_global):

            if gen == 1:

                nombre, peso, valor = Objetos[i]

                peso_total += peso

                objetos_seleccionados.append(
                    f"• {nombre} | Peso: {peso} kg | Valor: {valor}"
                )

    return (
        historial_mejor,
        historial_promedio,
        mejor_fitness_global,
        peso_total,
        objetos_seleccionados,
        registro_generaciones
    )


# ==========================================================
# GRAFICO
# ==========================================================

def mostrar_grafico(mejores, promedios):

    plt.figure(figsize=(10, 6))

    plt.plot(
        mejores,
        label="Mejor Aptitud",
        linewidth=2
    )

    plt.plot(
        promedios,
        "--",
        label="Promedio"
    )

    plt.title(
        "Resultado de la convergencia del algoritmo genético | Figura 1 |"
    )

    plt.xlabel("Generación")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.legend()

    plt.show()

# ==========================================================
# LIMPIAR
# ==========================================================

def limpiar_datos():

    area_texto.delete(1.0, tk.END)





# ==========================================================
# INTERFAZ GRAFICA
# ==========================================================

def generar_simulacion():

    global Tamaño_poblacion
    global Generaciones
    global Tasa_cruzamiento
    global Tasa_mutacion
    global Tamano_torneo

    try:

        Tamaño_poblacion = int(entry_poblacion.get())
        Generaciones = int(entry_generaciones.get())
        Tasa_cruzamiento = float(entry_cruzamiento.get())
        Tasa_mutacion = float(entry_mutacion.get())
        Tamano_torneo = int(entry_torneo.get())

    except ValueError:

        messagebox.showerror(
            "Error",
            "Verifica los parametros."
        )
        return

    (
        mejores,
        promedios,
        mejor_fitness,
        peso_total,
        objetos,
        historial
    ) = ejecutar_algoritmo_genetico()

    area_texto.delete(1.0, tk.END)

    # -----------------------------------
    # PARÁMETROS UTILIZADOS
    # -----------------------------------

    area_texto.insert(
        tk.END,
        "PARÁMETROS UTILIZADOS\n"
    )

    area_texto.insert(
        tk.END,
        "==============================\n"
    )

    area_texto.insert(
        tk.END,
        f"Tamaño de población : {Tamaño_poblacion}\n"
    )

    area_texto.insert(
        tk.END,
        f"Generaciones        : {Generaciones}\n"
    )

    area_texto.insert(
        tk.END,
        f"Tasa cruzamiento    : {Tasa_cruzamiento}\n"
    )

    area_texto.insert(
        tk.END,
        f"Tasa mutación       : {Tasa_mutacion}\n"
    )

    area_texto.insert(
        tk.END,
        f"Tamaño torneo       : {Tamano_torneo}\n"
    )

    area_texto.insert(
        tk.END,
        "\n==============================\n\n"
    )

    # -----------------------------------
    # RESUMEN DE LA MEJOR MOCHILA
    # -----------------------------------

    area_texto.insert(
        tk.END,
        "RESUMEN DE LA MEJOR MOCHILA\n"
    )

    area_texto.insert(
        tk.END,
        "==============================\n"
    )

    area_texto.insert(
        tk.END,
        f"MEJOR APTITUD: {mejor_fitness} puntos\n\n"
    )

    area_texto.insert(
        tk.END,
        "OBJETOS SELECCIONADOS:\n\n"
    )

    for linea in objetos:
        area_texto.insert(
            tk.END,
            linea + "\n"
        )

    area_texto.insert(
        tk.END,
        f"\nPeso Total: {peso_total} kg / {Capacidad_Maxima} kg\n"
    )

    # -----------------------------------
    # HISTORIAL DE GENERACIONES
    # -----------------------------------

    area_texto.insert(
        tk.END,
        "\n\n=========================\n"
    )

    area_texto.insert(
        tk.END,
        "HISTORIAL DE GENERACIONES\n"
    )

    area_texto.insert(
        tk.END,
        "=========================\n\n"
    )

    for linea in historial:
        area_texto.insert(
            tk.END,
            linea + "\n"
        )

    # Mostrar gráfica una sola vez al final
    mostrar_grafico(
        mejores,
        promedios
    )



# ==========================================================
# VENTANA
# ==========================================================

ventana = tk.Tk()

ventana.title(
    "Algoritmo Genetico - Problema de la Mochila"
)

ventana.geometry("900x700")

# ----------------------------------------------------------

frame = ttk.Frame(ventana)
frame.pack(pady=10)

ttk.Label(
    frame,
    text="Tamaño Poblacion"
).grid(row=0, column=0)

entry_poblacion = ttk.Entry(frame, width=10)
entry_poblacion.insert(0, "20")
entry_poblacion.grid(row=0, column=1)

ttk.Label(
    frame,
    text="Generaciones"
).grid(row=0, column=2)

entry_generaciones = ttk.Entry(frame, width=10)
entry_generaciones.insert(0, "50")
entry_generaciones.grid(row=0, column=3)

ttk.Label(
    frame,
    text="Cruzamiento"
).grid(row=1, column=0)

entry_cruzamiento = ttk.Entry(frame, width=10)
entry_cruzamiento.insert(0, "0.8")
entry_cruzamiento.grid(row=1, column=1)

ttk.Label(
    frame,
    text="Mutacion"
).grid(row=1, column=2)

entry_mutacion = ttk.Entry(frame, width=10)
entry_mutacion.insert(0, "0.05")
entry_mutacion.grid(row=1, column=3)

ttk.Label(
    frame,
    text="Torneo"
).grid(row=2, column=0)

entry_torneo = ttk.Entry(frame, width=10)
entry_torneo.insert(0, "3")
entry_torneo.grid(row=2, column=1)

# ----------------------------------------------------------
# BOTONES
# ----------------------------------------------------------

frame_botones = ttk.Frame(ventana)
frame_botones.pack(pady=10)

btn_generar = ttk.Button(
    frame_botones,
    text="Generar Simulación",
    command=generar_simulacion
)

btn_generar.grid(
    row=0,
    column=0,
    padx=5
)

btn_limpiar = ttk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar_datos
)

btn_limpiar.grid(
    row=0,
    column=1,
    padx=5
)

# ----------------------------------------------------------




# ----------------------------------------------------------

area_texto = ScrolledText(
    ventana,
    width=100,
    height=30
)

area_texto.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

# ----------------------------------------------------------

ventana.mainloop()
