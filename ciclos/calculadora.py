print('*** Calculadora en Python ***')

salir = False
while not salir:
    print('''Operacinoes que puedes realizar:
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir''')
    opcion = int(input('Selecciona una opción: '))
    # Validamos que no sea la opción 5
    if opcion >=1 and opcion <=4:
        # Solicitamos los valores
        operando1 = float(input('Introduce el primer operando: '))
        operando2 = float(input('Introduce el segundo oprando: '))
    if opcion == 1:
        suma = operando1 + operando2
        print(f'El resultado de la suma es: {suma}')
    elif opcion == 2:
        resta = operando1 - operando2
        print(f'El resultado de la resta es: {resta}')
    elif opcion == 3:
        multiplicacion = operando1 * operando2
        print(f'El resultado de la multiplicación es {multiplicacion}')
    elif opcion == 4:
        division = operando1 / operando2
        print(f'El resultado de la división es: {division}')
    elif opcion == 5:
        print('Saliendo...')
        salir = True
    else:
        print('Opción no reconocida')