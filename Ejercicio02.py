#Escribir una función que reciba un número entero positivo y devuelva 
# su factorial. Realiza el ejercicio mediante bucles interactivos y 
# mediante una función recursiva.
def factorial(numero):
    """La funcion recibe un número entero positivo y devuelve 
    su factorial"""
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
resultado = factorial(int(input("Dime un numero: ")))
print(resultado)