# 🧠 Proyecto Colaborativo: Inteligencia Artificial en Python
> **Curso de Python - UNIR**
>
> ¡Bienvenidos al repositorio central de prácticas y proyectos de Inteligencia Artificial! Este es un espacio diseñado para el aprendizaje colaborativo, donde compartiremos códigos, resolveremos retos y realizaremos revisiones de código entre compañeros.

---

## 🚀 ¿Cómo Colaborar en este Repositorio?

Para mantener el orden y garantizar que todos puedan aportar sin generar conflictos de código, seguiremos el siguiente flujo de trabajo colaborativo basado en **Git & GitHub**:

### 1. Bifurcar (Fork) o Clonar el Repositorio
Si eres miembro directo, clona este repositorio en tu máquina:
```bash
git clone https://github.com/maibarra0904/inteligencia-artificial.git
cd inteligencia-artificial
```

### 2. Crear una Rama para tu Tarea
Nunca trabajes directamente sobre la rama `main`. Crea una rama con tu nombre y el número de la tarea:
```bash
git checkout -b tarea1-evolutivos-tu_nombre_apellido
```
*Ejemplo:* `git checkout -b tarea1-evolutivos-mario_ibarra`

### 3. Estructura de tus Archivos
Coloca todas tus entregas en la carpeta `contribuciones/` dentro de una subcarpeta con tu nombre:
```text
inteligencia-artificial/
├── contribuciones/
│   └── tu_nombre_apellido_evolutivos/
│       ├── tarea_1.py
│       └── README.md
```

### 4. Guardar y Subir tus Cambios
```bash
git add .
git commit -m "feat: entrega de Tarea 1 - Tu Nombre"
git push origin tarea1-evolutivos-tu_nombre_apellido
```

### 5. Crear un Pull Request (PR)
Ve al repositorio original en GitHub y abre un **Pull Request**. Describe brevemente tu solución y pide a al menos un compañero que revise tu código antes de fusionarlo.

---

## 📅 Lista de Tareas y Retos

| Tarea | Descripción | Estado | Enlace |
| :--- | :--- | :---: | :---: |
| **Tarea 1** | **Optimización con Algoritmos Genéticos (Problema de la Mochila)** | 🟢 Activo | [Ir a Tarea 1](tareas/tarea_1_algoritmos_evolutivos/INSTRUCCIONES.md) |
| **Tarea 2** | Clasificación de Flores Iris (Árboles de Decisión) | 🟡 Próximamente | - |
| **Tarea 3** | Procesamiento de Lenguaje Natural (Análisis de Sentimiento) | 🔴 Planificado | - |

---

## 🛠️ Buenas Prácticas de Código
* **Documentación:** Comenta tus funciones explicando qué hacen, sus parámetros y lo que retornan.
* **Limpieza:** No subas archivos temporales ni carpetas `.venv` o `__pycache__` (ya están configurados en el `.gitignore`).
* **Modularidad:** Separa la lógica de carga de datos, entrenamiento del modelo y visualización en funciones independientes.
* **Aprende de otros:** ¡Tómate unos minutos para ver y comentar los Pull Requests de tus compañeros!

---
*Este repositorio es de uso exclusivo didáctico para la clase de Inteligencia Artificial de la UNIR.*
