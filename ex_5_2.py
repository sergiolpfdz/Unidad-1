from math import sqrt
print('Cálculo del módulo de un vector')
print('-------------------------------')
# Llenamos el vector con 10 elementos
v = []
for i in range(10):
 v.append( float(input(f'Introduce el elemento {i} : ')) )
# Calculamos la suma de los cuadrados
suma = 0
for i in range(0, len(v)):
 suma = suma + v[i]**2
# Imprimimos el módulo
print('El módulo del vector es', sqrt(suma))