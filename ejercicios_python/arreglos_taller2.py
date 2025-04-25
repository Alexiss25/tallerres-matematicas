# 1. Dado el arreglo [1,2,3,4,5,6]:


# a) Iterar por todos los elementos dentro del arreglo utilizando while y mostrarlos en pantalla.

arreglo = [1, 2, 3, 4, 5, 6]

# a) While

i = 0
while i < len(arreglo):
    print(arreglo[i])
    i += 1

# b) For

for x in arreglo:
    print(x)

# c) Copia con +1

arr_plus_one = []
for x in arreglo:
    arr_plus_one.append(x + 1)
print("Incrementados:", arr_plus_one)

# d) Promedio

suma = 0
for x in arreglo:
    suma += x
promedio = suma / len(arreglo)
print("Promedio:", promedio)

"""
2.  Dado el arreglo de cadenas de ADN [“AATGAAC”, “GTTTTTC”, “GGTAAA”, “CCCCATGGG”]
cree una función que reciba como argumento tal arreglo y muestre las cadenas de una sola base
(cadenas formadas solo de A, o solo de T, o solo de C o solo de G) que se pueden formar entre todos los
elementos del arreglo
"""

def bases_comunes(adn_list):
    if not adn_list:
        return []
    
    comunes = set(adn_list[0])
    for seq in adn_list[1:]:
        comunes &= set(seq)
    
    return sorted([b for b in comunes if b in {'A','C','G','T'}])

dna = ["AATGAAC", "GTTTTTC", "GGTAAA", "CCCCATGGG"]
print("Bases comunes:", bases_comunes(dna))

""" 3. Cree una función que reciba un arreglo de números y retorne el número menor entre todos los
elementos del arreglo.
"""
def minimo(arr):
    if not arr:
        raise ValueError("El arreglo está vacío.")
    m = arr[0]
    for x in arr[1:]:
        if x < m:
            m = x
    return m

print(minimo([5, 3, 9, 1, 4]))

""" 4. Cree una función que reciba un arreglo de números naturales y muestre todos los números primos en
él.
"""
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mostrar_primos(arr):
    for x in arr:
        if es_primo(x):
            print(x)

naturales = [2, 4, 5, 9, 11, 16, 17]
mostrar_primos(naturales)

""" 
5. Cree una función que pida a n número de usuarios su nombre y edad y retorne un arreglo con los
nombres de los usuarios que son mayores de edad, luego muestre cuantos usuarios hay mayores de
edad.
"""
def mayores_de_edad():
    try:
        n = int(input("¿Cuántos usuarios vas a ingresar? "))
    except ValueError:
        print("Debe ingresar un número entero.")
        return []
    adultos = []
    for _ in range(n):
        nombre = input("Nombre: ")
        try:
            edad = int(input("Edad: "))
        except ValueError:
            print("Edad inválida, se asume 0.")
            edad = 0
        if edad >= 18:
            adultos.append(nombre)
    print(f"Hay {len(adultos)} mayores de edad.")
    return adultos

adultos = mayores_de_edad()
"""
6. Dado los arreglos valle = [“Cali” , “Tulua”, “Cartago”, “Salento”] quindio = [“Cordoba”,
“Armenia”, “Palmira”, “Circasia”] Ordene los arreglos de tal manera que los elementos(ciudades)
queden en el arreglo que les corresponde. Use ciclos.
"""
valle = ["Cali", "Tulua", "Cartago", "Salento"]
quindio = ["Cordoba", "Armenia", "Palmira", "Circasia"]

ciudades_valle = {"Cali", "Tulua", "Cartago", "Palmira"}
ciudades_quindio = {"Armenia", "Cordoba", "Circasia", "Salento"}

for city in valle[:]:
    if city not in ciudades_valle:
        valle.remove(city)
        quindio.append(city)

for city in quindio[:]:
    if city not in ciudades_quindio:
        quindio.remove(city)
        valle.append(city)

print("Valle:", valle)
print("Quindío:", quindio)

"""
7. Dados los arreglos arreglo1 = [“Pera”, “Cebolla”, “Limón”, “Pimentón”] arreglo2 = [“Manzana”,
“Banano”, “Lechuga”, “Perejíl”] Ordene los arreglos de tal manera que los elementos(frutas y
verduras) queden en el arreglo que les corresponde. Use ciclos.

"""
arreglo1 = ["Pera", "Cebolla", "Limón", "Pimentón"]
arreglo2 = ["Manzana", "Banano", "Lechuga", "Perejíl"]

frutas = {"Pera", "Manzana", "Banano", "Limón"}
verduras = {"Cebolla", "Lechuga", "Pimentón", "Perejíl"}

# Mover mal asignadas
for item in arreglo1[:]:
    if item not in frutas:
        arreglo1.remove(item)
        arreglo2.append(item)

for item in arreglo2[:]:
    if item not in verduras:
        arreglo2.remove(item)
        arreglo1.append(item)

print("Frutas:", arreglo1)
print("Verduras:", arreglo2)
