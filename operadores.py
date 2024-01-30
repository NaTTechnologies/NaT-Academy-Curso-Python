# Operadores aritmeticos
a = 2
b = 4

print("a =" + str(a) + " y b =" + str(b))
print("La suma")
print(a + b)
print("La resta")
print(a - b)
print("La multiplicacion")
print(a * b)
print("La division")
print(a/b)
print("El modulo")
print(a % b)
print("La potencia")
print(a**b)

# Operadores de comparacion
x = 5
y = 3

# Igualdad
print(x == y)

# Desigualdad
print(x != y)

# Mayor que
print(x > y)

# Menor que
print(x < y)

# Mayor e igual que
print(x >= y)

# Menor e igual que
print(x <= y)

# Operadores logicos
print("Operadores logicos")
# Operador and (ambas verdaderas) = verdadera
print(x > 2 and y < 5)

# Operador or (una de las dos verdadera) = verdaera
print(x > 7 or y < 2)

# Operador and (negacion)
print(not (x > y))

# Operadores de asignacion

# Asignación simple
x = 10

# Asignación con suma
x += 5  # es equivalente a x = x + 5

# Asignación con resta
x -= 3  # es equivalente a x = x - 3

# Asignación con multiplicación
x *= 2  # es equivalente a x = x * 2

# Asignación con división
x /= 4  # es equivalente a x = x / 4

# Asignación con módulo
x %= 3  # es equivalente a x = x % 3

# Asignación con potencia
x **= 2  # es equivalente a x = x ** 2


# Operadores aritméticos
x = 10
y = 3
print(x + y)   # Suma
print(x - y)   # Resta
print(x * y)   # Multiplicación
print(x / y)   # División
print(x % y)   # Módulo
print(x ** y)  # Potencia

# Operadores de comparación
x = 10
y = 3
print(x > y)    # Mayor que
print(x < y)    # Menor que
print(x == y)   # Igual que
print(x != y)   # Distinto que
print(x >= y)   # Mayor o igual que
print(x <= y)   # Menor o igual que

# Operadores lógicos
x = True
y = False
print(x and y)  # AND lógico
print(x or y)   # OR lógico
print(not x)    # NOT lógico

# Expresiones condicionales
x = 10
y = 3
z = 5
resultado = x + y if x > z else x - y
print(resultado)
