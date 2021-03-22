#Reto 1 Misión MinTIC 2022
#Yesid Barragan

#Entrada valores
producto = input("Ingrese el nombre del producto: ")
costo_unitario = int(input("Ingrese el costo unitario del producto CU: "))
precio_venta = int(input("Ingrese el precio de venta al publico PVP: "))
unidades_disponibles = int(input("Ingrese la cantidad de unidades disponibles: "))

#Calculo ganancia
ganancia = (unidades_disponibles*precio_venta)-(unidades_disponibles*costo_unitario)

#Salida valores
print("Producto " + producto )
print("CU: $" + str(costo_unitario))
print("PVP: $" + str(precio_venta))
print("Unidades Disponibles: " + str(unidades_disponibles))
print("Ganancia: $" + str(ganancia))

"""
Cómo usar la función  .format():
producto = input('Nombre producto: ')
print('Producto: {pr}'.format(pr=producto))
"""