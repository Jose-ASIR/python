renta=int(input("Escribe tu renta anual"))
if renta < 10000:
    print ("Te corresponde el 5%")
elif renta >= 10000 and renta <= 20000:
    print ("Te corresponde el 15%")
elif renta > 20000 and renta <= 35000:
    print ("Te corresponde el 20%")
elif renta > 35000 and renta <=60000:
    print ("Te corresponde el 30%")
else:
    print("Te corresponde el 45%")