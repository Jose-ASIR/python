barra=3.49
descuento=0.60
panantiguo=int(input("Escribe el número de barras de pan vendidas que no sean de hoy "))
importedescontadototal=round(barra*descuento*panantiguo,2)
costefinal=round((barra*panantiguo)-importedescontadototal,2)
print (f"El precio habitual de una barra de pan es de {barra} €. El descuento es de {importedescontadototal} €. El precio final es de {costefinal} €")
