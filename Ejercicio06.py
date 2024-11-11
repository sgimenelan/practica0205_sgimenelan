#Escribir una función que convierta un número decimal en 
# binario y otra que convierta un número binario en decimal.
def binario_decimal(n):
    return int(n,2)

def decimal_binario(n):
    return bin(n)

condicion = input("Dime que quieres pasar: ")
numero = input("Dime el numero: ")
if condicion == "binario a decimal":
    resultado = binario_decimal(numero)
    print(resultado)
else:
    numero = int(numero)
    resultado = decimal_binario(numero)
    print(resultado[2:len(resultado)])