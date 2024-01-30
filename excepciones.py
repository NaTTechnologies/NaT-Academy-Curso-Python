a = 0
b = 0

def dividir(a, b):
    if a == 0 and b == 0:
        raise ZeroDivisionError("La division es por 0")
    else:
        return a / b

try:
    print(dividir(a, b))
except ZeroDivisionError:
    print("Hay una division de 0")
finally:
    print("El programa termino")


print(dividir(a, b))