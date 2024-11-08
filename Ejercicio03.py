#Escribir una función que calcule el área de un círculo y otra
# que calcule el volumen de un cilindro usando la primera función.
def area_circulo(r):
    """función que calcule el área de un círculo
    Parámetros:
...   - r: radio del circulo
... Salida:
      - el area del circulo
    """
    return 3.1416 * (r**2)
area1 = area_circulo(int(input("Dime el radio: ")))
print(area1)
def area_cilindro(h):
    """función que calcule el área de un cilindro
    Parámetros:
...   - r: radio del cilindro
      - h : altura del cilindro
... Salida:
      - el area del cilindro
    """
    r = int(input("Dime el radio: "))
    return area_circulo(r) * h
area2 = area_cilindro(int(input("Dime la altura: ")))
print(area2)