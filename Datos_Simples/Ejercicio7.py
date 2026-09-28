masa=float(input("Escribe tu peso en kg"))
altura=float(input("Escribe tu estatura en metros"))
imc= round (masa/ (altura ** 2), 2 )
print(f"Tu indice de masa corporal es {imc}")
