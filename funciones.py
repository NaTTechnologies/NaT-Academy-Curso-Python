def suma(a, b):
    resultado = a + b
    return resultado

# print("La suma de 10 + 10 es = " + str(suma(10, 10)))

def sumaIterada(a = 2):
    resultado = 0
    valores = []
    for i in range(a):
        resultado += i
        valores.append(i)
    return (a, resultado, valores)

# print(sumaIterada(10))