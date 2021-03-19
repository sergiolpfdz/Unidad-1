n=float(input('escribe el numero de veces'))
a=0
suma=0
while n<10000:
     a+=1
     a=float(a)
     suma+=1/pow(a,2)
     n+=1
print (suma)