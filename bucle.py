# While
i = 1
print("Imprimiendo los numeros del 1 al 10 con While")
while i <= 10:
    print(i)
    i += 1

# For
print("Imprimiendo los numeros del 1 al 10 con For")
i = 0
for i in range(0, 10):
    print(i)

# For r if anidado
print("Imprimiendo los numeros pares del 1 al 10 con For")
i = 0
for i in range(0, 10):
    if i % 2 == 0:
        print(i)

frutas = ["manzana", "banana", "kiwi"]
for fruta in frutas:
    print(fruta)
