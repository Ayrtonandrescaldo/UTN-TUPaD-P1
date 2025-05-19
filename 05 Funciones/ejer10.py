def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("ingrese la primer nota: "))
b = float(input("ingrese la segunda nota: "))
c = float(input("ingrese la tercer nota: "))
resultado = calcular_promedio(a, b, c)
print(f"el promedio final es: {resultado}")
