num1 = int(input('Introduce el primer número entero: '))
num2 = int(input('Introduce el segundo número entero: '))

if num1 > num2:
    print(f'El primer número es el mayor de los dos, {num1}')
elif num1 < num2:
    print(f'El segundo número es el mayor de los dos, {num2}')
else:
    print('Los dos números son iguales')