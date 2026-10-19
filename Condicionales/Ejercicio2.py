contraseña=("contraseña")
contraseñaUsuario=input("Escribe la contraseña ")
if contraseña.lower() == contraseñaUsuario.lower():
    print ("La contraseña es la misma que la almacenada sin tener en cuenta mayusculas y minusculas ")
else:
    print ("La contraseña introducida no es igual a la guardada ")
