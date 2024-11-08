#Escribir una función a la que se le pase una cadena <nombre>
# y muestre por pantalla el saludo ¡hola <nombre>!.
def bienvenido(nombre):
    """"función a la que se le pase una cadena <nombre>
    y muestre por pantalla el saludo ¡hola <nombre>!.
    Parámetros:
...   - nombre: Un nombre de una persona
... Salida:
      - ¡hola <nombre>!.  
"""
    print("¡Hola", nombre + "!")
bienvenido(input("Dime tu nombre: "))