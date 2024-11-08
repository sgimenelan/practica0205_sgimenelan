#Escribir una función que reciba una muestra de números 
# en una lista y devuelva su media.
import statistics
numero = ""
numeros = []
while numero != "no hay mas":
    numero =  input("Dime un numero: ")
    numeros.append((numero))
numeros.pop(len(numeros) - 1)
numeros = list(map(float, numeros))
def media(n):
    return statistics.mean(n)
resultado = media(numeros)
print(round(resultado,2))