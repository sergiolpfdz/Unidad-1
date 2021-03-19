from math import sqrt

v=[]
for i in range (10):
    v.append( float(input(f'Introduce los numeros enteros {i} : ')) )
    
    if i%2==0:
      print(f"El numero {i} es par")
    else:
        print(f"el numero{i} es impar")
print("---------------------------------")
print("suma de multiplos de 3")
x=[]  
for l in range (10):
    x.append( int(input(f'Introduce los numeros enteros para la suma de 3 {l} : ')) )
    def sumar_pares(l):
        if len(l)==0:
            return 0
        elif l[0]%3==0:
            return l[0] + sumar_pares(l[1:])
        else:
            return sumar_pares(l[1:])
    print("la suma de las pocisiones multiplos son",sumar_pares(x),)
        
print("Serie de fibonacci")
x=0
y=1
z=0
while True:
    n=int(input("ingrese un numeor mayor que 1"))
    if n>1:
        break
print("1",end=" ")
for i in range(0,n):
    z=x+y
    print(f"{z}",end= " ")
    x=y
    y=z
print(" ")

print("-------------------")
print("imprimir la lista al revez")
lista=[]
for i in range(10):
    lista.append(int(input("ingrese los datos que quieres en la lista")))
    print(lista)

inverso=list(reversed(lista))
print(inverso)
  

print("-----------")
print("imprimir la lista de forma ascendente")
lista1=[]


for l in range(10):
    lista1.append(int(input("ingrese los datos que quieres en la lista")))
    print(lista1)
ascendente=list(sorted(lista1))
print(ascendente)