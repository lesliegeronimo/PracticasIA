# GERONIMO SOTO LESLIE - 320032848 - PRACTICA 03
# implementacion para resolver el problema de n reinas, nxn.

import random

# Función para evaluar cuántos ataques hay en un tablero
def evaluar(tablero):
    ataques = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i + 1, n):
            if tablero[i] == tablero[j] or abs(tablero[i] - tablero[j]) == abs(i - j):
                ataques += 1
    return ataques

# Genera una población inicial aleatoria
def generar_poblacion(tamano, n):
    return [random.sample(range(n), n) for _ in range(tamano)]

# Selecciona los mejores individuos basado en su evaluación
def seleccion(poblacion):
    return sorted(poblacion, key=evaluar)[:len(poblacion)//2]

# Realiza el cruce entre dos padres para generar un hijo
def cruzar(padre, madre):
    punto = random.randint(1, len(padre) - 2)
    hijo = padre[:punto] + [gen for gen in madre if gen not in padre[:punto]]
    return hijo

# Realiza una mutación intercambiando dos posiciones aleatorias
def mutar(tablero):
    if random.random() < 0.2:  # Probabilidad del 20% de mutar
        i, j = random.sample(range(len(tablero)), 2)
        tablero[i], tablero[j] = tablero[j], tablero[i]
    return tablero

# Algoritmo genético principal
def algoritmo_genetico(n, generaciones=1000, tam_poblacion=100):
    poblacion = generar_poblacion(tam_poblacion, n)
    mejor_soluciones = []
    mejor_solucion_final = None
    
    for gen in range(generaciones):
        poblacion = seleccion(poblacion)
        nueva_poblacion = []
        while len(nueva_poblacion) < tam_poblacion:
            padre, madre = random.sample(poblacion, 2)
            hijo = cruzar(padre, madre)
            hijo = mutar(hijo)
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion
        mejor_solucion = min(poblacion, key=evaluar)
        mejor_fit = evaluar(mejor_solucion)
        mejor_soluciones.append(mejor_solucion)
        
        if mejor_solucion_final is None or mejor_fit < evaluar(mejor_solucion_final):
            mejor_solucion_final = mejor_solucion
        
        if gen % 50 == 0 or mejor_fit == 0:  # Imprime cada 50 generaciones o cuando encuentra solución óptima
            fitness_str = "100%" if mejor_fit == 0 else str(mejor_fit)
            print(f"Mejor solución en generación {gen}: {mejor_solucion} | fitness: {fitness_str}")
            imprimir_tablero(mejor_solucion)
            
        if mejor_fit == 0:
            print("Se encontró una solución óptima, terminando ejecución.")
            imprimir_tablero(mejor_solucion)
            break
    
    return mejor_soluciones, mejor_solucion_final

# Imprime una solución en formato de tablero
def imprimir_tablero(solucion):
    n = len(solucion)
    for fila in solucion:
        linea = ['.'] * n
        linea[fila] = '♛'
        print(" ".join(linea))
    print("\n")

n = 10  # Tablero de 10x10
soluciones, mejor_solucion_final = algoritmo_genetico(n)

