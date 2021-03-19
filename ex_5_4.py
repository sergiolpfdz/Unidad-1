print("calificacion de los alumnos")

lista2_calificaciones=[]
for i in range (0,5):
    lista2_calificaciones.append(int(input(f"ingrese la calificacion corresponfiente al alumno")))
    print(lista2_calificaciones)

for n in range(0,len(lista2_calificaciones)):
    if lista2_calificaciones[i] >=0 and lista2_calificaciones[i]<=5:
        print("valor insuficiente, repetir el curso")
    else:
        if lista2_calificaciones[i] >5 and lista2_calificaciones[i]<=7:
            print("Valor es aprobatorio")
        else:
            if lista2_calificaciones[i]>7 and lista2_calificaciones[i]<9:
                print("valor es notable")  
            else:
                if lista2_calificaciones[i] ==9 and lista2_calificaciones[i]==10:
                 print("el valor es notable")
                else:
                   
                 print("Valor muy alto vuelvalo a intentar")