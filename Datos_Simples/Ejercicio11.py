dinerodepositado = float(input("Introduce la cantidad de dinero depositada en la cuenta: "))
interes = 0.04
año1 = inversion * (1 + interes)
año2 = año1 * (1 + interes)
año3 = año2 * (1 + interes)

print(f"Ahorros tras el primer año: {round(año1, 2)} €")
print(f"Ahorros tras el segundo año: {round(año2, 2)} €")
print(f"Ahorros tras el tercer año: {round(año3, 2)} €")