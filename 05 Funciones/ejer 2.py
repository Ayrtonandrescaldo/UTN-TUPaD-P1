def saludar_usuario(nombre):
    return f"hola {nombre}"

nombre_usuario = input("ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)