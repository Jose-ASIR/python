nombre=input("Escribe el nombre de un producto ")
precio=float(input("Escribe el precio del producto "))
unidades=int(input("Escribe el número de unidades "))
coste_total=precio*unidades
print (f"El nombre del producto es {nombre} y el precio del producto es {precio:09.2f} el cual tiene {unidades:03d} unidades y un coste total de {coste_total:011.2f}")
