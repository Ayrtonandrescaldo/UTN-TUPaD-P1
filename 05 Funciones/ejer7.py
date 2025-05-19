def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division)
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")