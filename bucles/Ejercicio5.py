cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés anual (%)? "))
años = int(input("¿Número de años? "))

for i in range(1, años + 1):
    cantidad *= 1 + interes / 100
    print(f"Año {i}: tendrás {cantidad:.2f}€ totales")