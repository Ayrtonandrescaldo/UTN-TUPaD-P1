compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
compras[2].append("jugo") 
compras[1].remove("fideos")
compras[1].append("tallarines")
compras[1].remove("salsa")
compras[1].append("salsa")
compras[0].remove("pan")
print(compras)