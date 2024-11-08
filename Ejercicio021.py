#Escribir una función que reciba un número entero positivo y devuelva 
# su factorial. Realiza el ejercicio mediante bucles interactivos y 
# mediante una función recursiva.
def factorial(numero):
    """La funcion recibe un número entero positivo y devuelve 
    su factorial"""
    i = numero
    resultado = 1
    while i > 0:
        resultado = resultado * i
        i = i - 1
    return resultado
print(factorial(int(input("Dime un numero: "))))