a= int(input('ingrese el primer valor'))
b=int(input('ingrese el segundo valor'))
while(a>b):
    print('el segundo valor es menor vuelvalo a intentar')
    b=int(input('ingrese el segundo valor'))

print('los numeros son diferentes')
#numero mas grande
def main():
    print("CADA VEZ MÁS GRANDES")
    primero = int(input("Escriba un número: "))
    segundo = int(input(f"Escriba un número mayor que {primero}: "))

    while segundo > primero:
        primero = segundo
        segundo = int(input(f"Escriba un número mayor que {primero}: "))

    print()
    print(f"{segundo} no es mayor que {primero}.")


if __name__ == "__main__":
    main()
#Suma hasta llegar el limite 
def main():
    print("HASTA EL LÍMITE")
    limite = float(input("Escriba el valor límite: "))
    while limite <= 0:
        limite = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

    print()
    numero = float(input("Escriba un número: "))
    suma = numero

    while suma < limite:
        numero = float(input("Escriba otro número: "))
        suma += numero

    print()
    print(f"Ha superado el límite. La suma de los números introducidos es {suma}.")


if __name__ == "__main__":
    main()
#numeros divisibles entre 7
divisor = 7

min = 100
max = 999

print('Los números del {} al {} divisibles por {} son:'.format(min, max, divisor))
num = min
while num <= 999:
    if (num % divisor == 0):
        print('- {}'.format(num))
    num += 1
#numeros divisibles entre 5
divisor2=5
min2=100
max2=999
print('Los números del {} al {} divisibles por {} son:'.format(min2, max2, divisor2))
num1 = min2
while num1 <= 999:
    if (num1 % divisor2 == 0):
        print('- {}'.format(num1))
    num1 += 1
    
def digitos_pares():
    pares = []

    for n in range(100, 401):
        cadena = str(n)

        if int(cadena[0]) % 2 == 0 and int(cadena[1]) % 2 == 0 and int(cadena[2]) % 2 == 0:
            pares.append(cadena)
    
    return pares


resultado = digitos_pares()

print(', '.join(resultado))