 #Declaro la estructura de datos Alumno
class Alumno():
def __init__(self):
     self.nombre = ''
 self.notas = []
 self.final = 0
# Pido el número de alumnos
num_alum = int( input('¿Cuántos alumnos tenemos? ') )
while num_alum < 1:
 num_alum = int( input('¿Cuántos alumnos tenemos? ') )
clase = []
for i in range(0, num_alum):
 # Añado un Alumno al vector
 clase.append( Alumno() )
 # Pido los datos del alumno
 print()
 clase[i].nombre = input(f'Introduce el nombre del alumno {i} : ')
 clase[i].notas = [] # innecesario (ya era el valor inicial)
 notas = input(f'Introduce las notas del alumno {i} separadas por espacio: ')
 for n in notas.split(' '):
 clase[i].notas.append( float(n) )
# Calculo la nota final de los alumnos
print('Informe de notas finales')
print('------------------------')
for i in range(0, num_alum):
 clase[i].final = 0 # innecesario (ya era el valor inicial)
 if len(clase[i].notas) == 0:
 print(clase[i].nombre, ': sin notas')
 else:
 for j in range(0, len(clase[i].notas)):
 clase[i].final = clase[i].final + float(clase[i].notas[j])
 clase[i].final = clase[i].final / len(clase[i].notas)
 # Escribo el resultado de la nota final de cada alumno
 print(clase[i].nombre , ':' , clase[i].final)