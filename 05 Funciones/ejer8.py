def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("ingrese su peso: "))
altura = float(input( "ingrese su altura: "))
resultado = calcular_imc(peso,altura)
print(f"su imc es: {resultado}")