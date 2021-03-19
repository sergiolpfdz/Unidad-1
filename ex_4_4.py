n=int(input('ingrese el factorial'))
factorial=1
while(n<=1 and n>=20):
    print('error ingrese un numero del 1 al 20')
    n=int(input('ingrese el fatorial'))

       
for i in range (n):
    factorial= factorial*n
    n = n-1
    print(factorial)   