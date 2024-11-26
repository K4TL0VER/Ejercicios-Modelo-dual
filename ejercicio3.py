#Primera edición cambiada
def comprimir_cadena(cadena):
    if not cadena:
        return ""

    comprimida = ""
    count = 1

    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i - 1]:
            count += 1
        else:
            comprimida += cadena[i - 1] + str(count)
            count = 1

    comprimida += cadena[-1] + str(count)

    resultado = min(cadena, comprimida, key=len)
    print(f'Cadena original: {cadena}, Cadena comprimida: {resultado}')
    return resultado

# Pruebas unitarias
def pruebas_unitarias():
    assert comprimir_cadena("aaabbbcc") == "a3b3c2"
    assert comprimir_cadena("aabb") == "aabb"  # La cadena comprimida no es más corta
    assert comprimir_cadena("abc") == "abc"    # La cadena comprimida no es más corta
    assert comprimir_cadena("aaaaa") == "a5"
    assert comprimir_cadena("bbbbb") == "b5"
    assert comprimir_cadena("") == ""

pruebas_unitarias()

# Entrada no válida. Cuando esto sucede, la función asume que se le proporcionará
# una cadena de caracteres como entrada.
# Si la cadena es muy grande, el método actual puede no ser el 
# más eficiente en términos de rendimiento
# El algoritmo actual comprime los caracteres consecutivos,
# si la cadena original no tiene caracteres consecutivos repetidos,
# la cadena comprimida podría ser más larga que la original
#  La función actual utiliza la compresión básica de contar caracteres consecutivos.
# Si tienes requisitos específicos para un tipo de compresión
# diferente, el algoritmo actual puede no ser adecuado.
