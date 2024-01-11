# Variables numericas
x = 10
y = 5.5
z = x + y

print("El valor de z es: " + str(z))

# Variables cadena

nombre = "Juan"
apellido = "Perez"

nombre_completo = nombre + " " + apellido

print("El nombre es: " + nombre_completo)

# Variables logicas o booleanas

es_verdadero = True
es_falso = not es_verdadero

print(es_falso)

# Variables de secuencia
mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (6, 7, 8, 9, 10)

print(mi_tupla)
print("Mi primer elemento " + str(mi_tupla[0]))
print("Mi ultimo elemento " + str(mi_tupla[len(mi_tupla) - 1]))

# Variable diccionario
mi_diccionario = {
    "nombre": "Jose",
    "apellido": "Briones",
    "edad": 23,
    "ciudad": "Roatan"
}

print(mi_diccionario)
print("El nombre es: " + mi_diccionario["nombre"])