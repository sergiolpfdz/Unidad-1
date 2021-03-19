a = float( input('Introduce el primer valor: ') )
minimo = a
maximo = a
b = float( input('Introduce el segundo valor: ') )
if b < minimo:
    minimo = b
else:
 maximo = b   

c = float( input('Introduce el tercer valor: ') )
if c < minimo:
    minimo = c

elif c > maximo:
    maximo = c

print('El mínimo es', minimo)
print('El máximo es', maximo)