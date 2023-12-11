def buscar_palabra(matriz, palabra):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Verificar horizontal
    for i in range(filas):
        for j in range(columnas - len(palabra) + 1):
            if matriz[i][j:j + len(palabra)] == palabra:
                return True

    # Verificar vertical
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas):
            if all(matriz[i + k][j] == palabra[k] for k in range(len(palabra))):
                return True

    # Verificar diagonal hacia la derecha y hacia abajo
    for i in range(filas - len(palabra) + 1):
        for j in range(columnas - len(palabra) + 1):
            if all(matriz[i + k][j + k] == palabra[k] for k in range(len(palabra))):
                return True

    # Verificar diagonal hacia la izquierda y hacia abajo
    for i in range(filas - len(palabra) + 1):
        for j in range(len(palabra) - 1, columnas):
            if all(matriz[i + k][j - k] == palabra[k] for k in range(len(palabra))):
                return True

    return False

# Ejemplo de uso
matriz = [
    ['G', 'B', 'C', 'D'],
    ['E', 'A', 'G', 'H'],
    ['I', 'J', 'T', 'L'],
    ['M', 'N', 'O', 'O']
]

palabra = "GATO"

resultado = buscar_palabra(matriz, palabra)
print(f"¿La palabra '{palabra}' se encuentra en la matriz? {resultado}")

# Si la palabra es más larga que la matriz, el algoritmo puede arrojar
# un índice fuera de rango.
# Matriz vacía, se debe verificar que la matriz no esté vacía.
# El algoritmo no verifica si la palabra solo contiene caracteres
# presentes en la matriz.
# Si la matriz no es cuadrada, puede haber problemas en los bucles y
# en la comparación de índices.
