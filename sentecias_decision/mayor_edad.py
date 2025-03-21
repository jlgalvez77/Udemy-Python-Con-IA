print('*** Comprobación si es mayor de edad ***')

MAYORIA_EDAD = 18

edad = int(input('Introduce la edad: '))

if edad >= MAYORIA_EDAD:
    print(f'La persona con {edad} años, es mayor de edad')
else:
    print(f'La persona con {edad} años, es menor de edad')
