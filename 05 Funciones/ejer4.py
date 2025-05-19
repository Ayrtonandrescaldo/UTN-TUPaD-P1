def calcular_area_circulo(radio):
    return radio * 3.14
def calcular_perimetro_circulo(radio): 
    return (radio * 2) * 3.14
radio = int(input("Ingrese el radio a calcular: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")