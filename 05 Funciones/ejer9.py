def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) +32

temp = float(input("ingrese la temperatura: "))
resultado = celsius_a_fahrenheit(temp)
print(f"la temperatura en Fahrenheit es {resultado}")