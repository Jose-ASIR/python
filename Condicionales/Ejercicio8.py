puntuacion=float(input("Escribe la puntuación "))
if (puntuacion<0.4):
    print (f"El rendimiento es inaceptable, percibirá {puntuacion*2400} €")
elif (puntuacion >= 0.4 and puntuacion < 0.6):
    print (f"El rendimiento es aceptable, percibirá {puntuacion*2400} €")
else:
    print (f"El rendimiento es meritorio, percibirá {puntuacion*2400} €")
