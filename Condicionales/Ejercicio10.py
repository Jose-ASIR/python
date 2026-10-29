tipopizza=input("¿Quieres una pizza vegetariana (sí/no) ")
if tipopizza.lower()[0]=="s":
    ingrediente=int(
        input("Dispones de estos ingredientes: Pimiento(0) y tofu(1). Sólo puedes elegir uno escribiendo el número ")
    )
    
    if ingrediente == 0:
        ingrediente="Pimiento"
        print (f"La pizza elegida es vegetariana y tiene los siguientes ingredientes: Mozzarella, tomate y {ingrediente}")
    elif ingrediente == 1:
        ingrediente ="tofu"
        print (f"La pizza elegida es vegetariana y tiene los siguientes ingredientes: Mozzarella, tomate y {ingrediente}")
    else:
        print ("Opción seleccionada no válida")
else:
    ingrediente=int(input("Dispones de estos ingredientes: Peperoni(0), Jamón(1) y Salmón(2). Sólo puedes elegir uno escribiendo el número "))
    if ingrediente == 0:
        ingrediente = "Peperoni"
        print (f"El tipo de pizza elegido no es vegetariana y tiene mozzarella, tomate y {ingrediente}")
    elif ingrediente == 1:
        ingrediente = "Jamón"
        print (f"El tipo de pizza elegido no es vegetariana y tiene mozzarella, tomate y {ingrediente}")
    elif ingrediente == 2:
        ingrediente = "Salmón"
        print (f"El tipo de pizza elegido no es vegetariana y tiene mozzarella, tomate y {ingrediente} ")
    else:
        print("Opción seleccionada no válida")