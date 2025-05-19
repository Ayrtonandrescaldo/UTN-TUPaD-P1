def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=int(input("ingrese su edad: "))
residencia=input("ingrese su lugar de residencia: ")
val_ingresados = informacion_personal(nombre, apellido, edad, residencia)
print(val_ingresados)