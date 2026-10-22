nombre=input("Escribe tu nombre ")
sexo=input("Escribe tu sexo (mujer/hombre) ")
if nombre.lower()[0] < "m" and sexo.lower()[0] == "m":
    print ("Estás en el grupo a")
elif nombre.lower()[0] > "n" and sexo.lower()[0] == "h":
    print ("Estás en el grupo b")
else:
    print ("No estás en ningún grupo ")