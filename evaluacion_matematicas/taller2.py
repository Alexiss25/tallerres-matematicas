#Cree una función que reciba el nombre de una persona como argumento y retorne el número de letras 
#de tal nombre, luego haga el llamado a la función y guarde su valor de retorno en una variable e imprima 
#ese valor por consola

def nuemro_letras(nombre):
    return len(nombre)

nombre= input("ingrese su nombre: ")
resultado= nuemro_letras(nombre)
print(f"el nombre tiene {resultado} letras")