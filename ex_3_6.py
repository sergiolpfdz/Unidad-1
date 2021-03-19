l=float(input("ingrese la longitud 1"))
l2=float(input("ingrese la longitud 2"))
l3=float(input("ingrese la longitud 3"))
if ((l==l2)and (l2==l3) and (l3==l3)):
    print("es un triangulo equilatero")
else:
    if ((l==l2) and (l2==l3) and (l3<l)) or ((l==l2) and (l2==l3) and (l3>l)):
        print("es un triangulo isoseles")
    else:
        print("es un triangulo escaleno")