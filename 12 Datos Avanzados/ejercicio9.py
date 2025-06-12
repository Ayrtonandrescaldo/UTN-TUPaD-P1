#ejercicio9
agenda = {}
while True:
    accion = input("acción (agregar/consultar/salir): ")
    if accion == "salir":
        break
    dia = input("día: ")
    hora = input("hora: ")
    clave = (dia, hora)
    if accion == "agregar":
        evento = input("evento: ")
        agenda[clave] = evento
    elif accion == "consultar":
        print(agenda.get(clave, "sin evento"))