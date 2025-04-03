# Cree una función que reciba como argumentos dos números y retorne el mayor de estos números, luego haga el llamado a la función y guarde su valor de retorno en una variable e imprima ese valor por consola.
def numero_mayor (numero1,numero2):
    if numero1 > numero2:
        return print(f" el numero mayor es {numero1}")
    else:
        print("el nuemro dos es menor")


numero1= input("ingrese el primer numero: ")
numero2= input("ingrese el segundo numero: ")
numero_mayor(numero1,numero2)