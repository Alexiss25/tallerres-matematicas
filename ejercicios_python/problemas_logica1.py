import math
import random
print("ejrcicio 1")
def ejercicio_1():
    edad = int(input("Ingrese su edad: "))
    anos = int(input("¿Cuántos años desea agregar?: "))
    print(f"En {anos} años, usted tendrá {edad + anos} años")

ejercicio_1()
print("ejercicio 2")
def ejercicio_2():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Producto: {num1 * num2}")
    print(f"Cociente: {num1 / num2 if num2 != 0 else 'Indefinido'}")
    print(f"Módulo: {num1 % num2}")

ejercicio_2()

print("ejercicio 3")
def ejercicio_3():
    precio = float(input("Ingrese el precio del electrodoméstico: "))
    meses = int(input("Ingrese el plazo en meses: "))
    precio_final = precio * (1.05 ** meses)
    cuota_mensual = precio_final / meses if meses > 0 else 0
    print(f"El valor de la cuota mensual será: {cuota_mensual:.2f}")

ejercicio_3()

print("ejercicio 4")
def ejercicio_4():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    print(f"Área: {(base * altura) / 2}")

ejercicio_4()

print("ejercicio 5")
def ejercicio_5():
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {math.pi * radio**2}")
    print(f"Perímetro: {2 * math.pi * radio}")

ejercicio_5()

print("ejercicio 6")
def ejercicio_6():
    lado = float(input("Ingrese el lado del cubo: "))
    print(f"Volumen: {lado**3}")

ejercicio_6()

print("ejercicio 7")
def ejercicio_7():
    precio = float(input("Ingrese el precio del producto: "))
    print(f"Precio con IVA: {precio * 1.19}")

ejercicio_7()

print("ejercicio 8")
def ejercicio_8():
    precio = float(input("Ingrese el precio del producto: "))
    print(f"Precio con descuento: {precio * 0.9}")

ejercicio_8()

print("ejercicio 9")
def ejercicio_9():
    cantidad = float(input("Ingrese la cantidad: "))
    porcentaje = float(input("Ingrese el porcentaje a calcular: "))
    print(f"Resultado: {cantidad * (porcentaje / 100)}")

ejercicio_9()

print("ejercicio 10")
def ejercicio_10():
    numero = float(input("Ingrese un número: "))
    print(f"Valor absoluto: {abs(numero)}")

ejercicio_10()

print("ejercicio 11")
def ejercicio_11():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Lanzamiento: {dado1} y {dado2}, suma: {dado1 + dado2}")

ejercicio_11()

def ejercicio_12():
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"Fahrenheit: {(celsius * 9/5) + 32}")

ejercicio_12()

print("ejercicio 13")
def ejercicio_13():
    n = 5
    factorial = math.factorial(n)
    print(f"Factorial de 5: {factorial}")

ejercicio_13()

def ejercicio_14():
    inicio = int(input("Ingrese el inicio del rango: "))
    fin = int(input("Ingrese el fin del rango: "))
    print(f"Número aleatorio: {random.randint(inicio, fin)}")

ejercicio_14()

print("ejercicio 15")
def ejercicio_15():
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    print(f"{segundos} segundos equivalen a {horas} horas y {minutos} minutos.")

ejercicio_15()

print("ejercicio 16")
def ejercicio_16():
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("No hay soluciones reales.")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Solución única: {x}")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Soluciones: {x1}, {x2}")

ejercicio_16()
