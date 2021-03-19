contraseñacorrecta="iloveyou123"
contraseña=input("ingrese la contraseña")
contador=1
while (contraseña!=contraseñacorrecta and contador<=3):
  contraseña=input('ingrese la contraseña')
  contador=contador + 1
if contador<=3:
    print("acceso concedido")
    print("bienvenido")
else:
    print("acceso denegado")
       
print("llegastes a la vez", contador) 