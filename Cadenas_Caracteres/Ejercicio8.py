precio=input("Escribe el precio de un producto en euros con dos decimales ")
precio = precio.replace(',')('.')
euros = precio.split('.')[0]
centimos = precio.split('.')[1]
print (f"El número de euros es de {euros}€ y el número de céntimos es {centimos}")