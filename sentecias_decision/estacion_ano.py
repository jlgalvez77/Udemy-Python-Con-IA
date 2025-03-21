print('*** Estacion del año ***')

mes = int(input('Introduce el número ddel mes: '))

if mes == 12 or mes == 1 or mes == 2:
    print('La estación es invierno')
elif mes == 3 or mes == 4 or mes == 5:
    print('La estación es primavera')
elif mes == 6 or mes == 7 or mes == 8:
    print('La estación es verano')
elif mes == 9 or mes == 10 or mes == 11:
    print('La estación es otoño')
else:
    print('El número de mes no es válido')
