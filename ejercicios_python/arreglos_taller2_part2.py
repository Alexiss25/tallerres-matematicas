
"""
8. Cree una función que reciba un arreglo de números enteros y retorne el número mayor en él. Se le
debe pedir al usuario que introduzca el arreglo.
"""

def mayor_usuario():
    try:
        datos = input("Introduce números separados por espacios: ")
        arr = [int(x) for x in datos.split()]
    except ValueError:
        print("Entrada inválida.")
        return None
    if not arr:
        print("Arreglo vacío.")
        return None
    m = arr[0]
    for x in arr[1:]:
        if x > m:
            m = x
    return m

print("Mayor:", mayor_usuario())


"""
9. Cree una función que reciba dos arreglos de números enteros y muestre cual arreglo tiene un
promedio mayor de sus elementos. Se le debe pedir al usuario que introduzca los arreglos.
"""

def promedio(arr):
    return sum(arr) / len(arr) if arr else 0

def comparar_promedios():
    try:
        a1 = [int(x) for x in input("Primer arreglo: ").split()]
        a2 = [int(x) for x in input("Segundo arreglo: ").split()]
    except ValueError:
        print("Entrada inválida")
        return
    p1, p2 = promedio(a1), promedio(a2)
    if p1 > p2:
        print("El primer arreglo tiene mayor promedio")
    elif p2 > p1:
        print("El segundo arreglo tiene mayor promedio")
    else:
        print("Los promedios son iguales.")

comparar_promedios()

"""
10. Cree una función que reciba un arreglo de nombres de personas y muestre si la letra “c” se
encuentra entre tales nombres, en caso de que la letra “c” se encuentre, mostrar las veces que se
encuentra(considerando las apariciones entre todos los nombres) . Se le debe pedir al usuario que
introduzca el arreglo.
"""

def contar_c():
    nombres = input("Introduce nombres separados por comas: ").split(",")
    total = sum(nombre.lower().count('c') for nombre in nombres)
    if total:
        print(f"La letra 'c' aparece {total} veces.")
    else:
        print("No se encontró la letra 'c'.")

contar_c()

"""
11. Cree una función que reciba un arreglo de números enteros positivos y muestre cuantos números
impares posee el arreglo. Se le debe pedir al usuario que introduzca el arreglo

"""
def contar_impares():
    try:
        arr = [int(x) for x in input("Introduce números positivos separados por espacios: ").split()]
    except ValueError:
        print("Entrada inválida.")
        return
    impares = [x for x in arr if x % 2 != 0]
    print(f"Hay {len(impares)} números impares: {impares}")

contar_impares()

"""
12. Cree una función que reciba un arreglo de cadenas de ADN (las cadenas estarán formadas por las
letras A o C o T o G referirse a taller de ADN pasado) y muestre la cadena de ADN con mayor número
de Timina (T). Se le debe pedir al usuario que introduzca los arreglos
"""

def mas_timinas():
    adn_list = input("Introduce secuencias de ADN separadas por comas: ").split(",")
    if not adn_list:
        print("Nada para procesar.")
        return
    mejor = max(adn_list, key=lambda s: s.upper().count('T'))
    print("Cadena con más 'T':", mejor)

mas_timinas()

"""
13 Cree una versión informática del juego conocido como ahorcado, en Python
"""
import random

def ahorcado():
    palabras = ["python", "arbol", "computador", "programa"]
    palabra = random.choice(palabras)
    letras_acertadas = set()
    intentos = 6

    while intentos > 0:
        display = "".join([c if c in letras_acertadas else "_" for c in palabra])
        print("Palabra:", display)
        if "_" not in display:
            print("¡Ganaste!")
            return

        letra = input("Adivina una letra: ").lower()
        if letra in letras_acertadas:
            print("Ya la intentaste.")
        elif letra in palabra:
            letras_acertadas.add(letra)
            print("¡Bien!")
        else:
            intentos -= 1
            print(f"Mal. Te quedan {intentos} intentos.")

    print("Perdiste. La palabra era:", palabra)

ahorcado()

"""
14. Cree una función que reciba un arreglo de números enteros no repetidos y lo retorne ordenado de
menor a mayor según el valor de tales elementos. Se le debe pedir al usuario que introduzca el arreglo
"""

def ordenar_enteros():
    try:
        arr = [int(x) for x in input("Introduce enteros: ").split()]
    except ValueError:
        print("Entrada inválida.")
        return []
    # Método sencillo: selección
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("Ordenado:", ordenar_enteros())

"""
15. Cree una función que reciba un arreglo de letras no repetidas y lo retorne ordenado alfabéticamente.
Se le debe pedir al usuario que introduzca el arreglo.
"""
def ordenar_letras():
    arr = input("Introduce letras separadas por espacios: ").split()
    # Burbuja
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print("Alfabético:", ordenar_letras())
