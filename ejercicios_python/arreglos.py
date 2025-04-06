
# Dado el siguiente arreglo  [200, -100, 45, 78, 32] , imprimir los elementos de índice 2 y 4 
arr1 = [200, -100, 45, 78, 32]
print(arr1[2])  # 45
print(arr1[4])  # 32
# Dado el siguiente arreglo ["ab", "cd", "ef", "gh"] , imprimir los elementos cd y gh. 
arr2 = ["ab", "cd", "ef", "gh"]
print(arr2[1])  # cd    
print(arr2[3])  # gh
# 3. Dado el siguiente arreglo [10, true, "k200", 20.7], imprimir todos sus elementos usando foreach
arr3 = [10, True, "k200", 20.7]
for elem in arr3:
    print(elem)
# 4. Dado el arreglo [17, 4, 64, 79, 109, 112], imprimir los elementos impares usando foreach
arr4 = [17, 4, 64, 79, 109, 112]
for num in arr4:
    if num % 2 != 0:
        print(num)

# 5. Dado el arreglo [true, true, false, true, false], cambiar índice 2 por true, y 3 por false
arr5 = [True, True, False, True, False]
arr5[2] = True
arr5[3] = False
print(arr5)
# 6. Dado el arreglo ["wc", "jp", "zx", "qr"], cambiar "jp" por true y "qr" por 30
arr6 = ["wc", "jp", "zx", "qr"]
arr6[1] = True
arr6[3] = 30
print(arr6)
# 7. Crear una función que reciba [2, 5, 7, 9] y recorra imprimiendo cada elemento
def imprimir_elementos(arr):
    for elem in arr:
        print(elem)

imprimir_elementos([2, 5, 7, 9])
# 8. Crear una función que reciba un arreglo y retorne el número de elementos
def contar_elementos(arr):
    return len(arr)

print(contar_elementos([10, 20, 30]))
# 9. Usar index para mostrar los índices de 44, 89, 70 en el arreglo [30, 44, 54, 89, 100]
arr9 = [30, 44, 54, 89, 100]
print(arr9.index(44))  # 1
print(arr9.index(89))  # 3

if 70 in arr9:
    print(arr9.index(70))
else:
    print("70 no está en el arreglo")
# 10. Imprimir el número de elementos de los siguientes arreglos
print(len([1,2,3,4,5,6,7,8,9,10]))  # a) 10
print(len([]))                     # b) 0
print(len(["a", True, -1]))        # c) 3
print(len([2, 4, 5, 7, 1, 34, 89, 0]))  # d) 8
# 11. Agregar elementos a un arreglo con append y extend
arr11 = [1,2,3,4,5,6,7,8,9,10]

# a) Agregar 345
arr11.append(345)
print(arr11)

# b) Agregar true
arr11.append(True)
print(arr11)

# c) Agregar "ADSO"
arr11.append("ADSO")
print(arr11)

# d) Agregar 455, 78, false
arr11.extend([455, 78, False])
print(arr11)

# e) Agregar "ABcd", true, 21
arr11.extend(["ABcd", True, 21])
print(arr11)

# 12. Eliminar elementos de arreglos por índice

# a) Eliminar índice 2
a = [1, 2, False]
del a[2]
print(a)

# b) Eliminar índice 6
b = [99, False, 17, 45, 7, "abc", 78]
del b[6]
print(b)

# c) Eliminar índice 1
c = [-1, -55, -89, -30, 1000]
del c[1]
print(c)

# d) Eliminar elementos desde índice 1 hasta 4
d = ["zxc", 767, 1298, True, False, [3], 1]
del d[1:5]
print(d)

# e) Eliminar elementos desde índice 3 hasta 4
e = [34, ["q"], 67, 1, 99, 1/2]
del e[3:5]
print(e)
# 13. Usar for para recorrer el arreglo ["x", "y", "z", 0, 1, 2, 3]
arr13 = ["x", "y", "z", 0, 1, 2, 3]
for elem in arr13:
    print(elem)

# 14. Recorrer arreglo [1, 17, 8, 9, 3] e imprimir cada elemento +1
arr14 = [1, 17, 8, 9, 3]
for num in arr14:
    print(num + 1)
# 15. Crear una función que reciba un arreglo y retorne su longitud
def longitud(arr):
    return len(arr)

print(longitud(["a", "b", "c"]))
# 16. Función que reciba una letra y verifique si está en ["a", "b", "c", "d", "e", "f", "g"]
def buscar_letra(letra):
    letras = ["a", "b", "c", "d", "e", "f", "g"]
    for l in letras:
        if l == letra:
            print("Sí está en el arreglo")
            return
    print("No está en el arreglo")

buscar_letra("c")  # Sí está
buscar_letra("z")  # No está
