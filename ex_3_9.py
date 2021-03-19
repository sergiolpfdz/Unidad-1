from math import sqrt
a = float(input('Valor de a:'))
b=float(input('valor de b:'))

if a!= 0:
    x=(-b/a)
    print ('solucion de la ecuacion: x = %4.3f  ' % (x))
else:
    if a==0 and b!=0:
        print("le ecuacion no tiene solucion")
    else:
        print('la ecuacion tiene infinitas soluciones.')
        