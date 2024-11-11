#Escribir una función que reciba una muestra de números
#en una lista y devuelva otra lista con sus valores al cuadrado.
numero = ""
numeros = []
while numero != "no hay mas":
    numero =  input("Dime un numero: ")
    numeros.append((numero))
numeros.pop(len(numeros) - 1)
numeros = list(map(float, numeros))
def cuadrado(n):
    """función que reciba una muestra de números 
    en una lista y devuelva su cuadrado
    Parámetros:
... - n = lista de numeros
... Salida:
      - cuadrado de esos numeros
    """
    lista = []
    for i in n:
        lista.append(i**2)
    return lista
resultado = cuadrado(numeros)
print(resultado)
