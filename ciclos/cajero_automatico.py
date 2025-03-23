print('*** Cajero Automatico ***')

saldo = 1000

while True:
    print('''Operaciones que puedes realizar:
          1. Consultar Saldo
          2. Retirar
          3. Depositar
          4. Salir''')
    
    opcion = int(input('Selecciona una opción: '))

    if opcion == 1:
        print(f'Tu saldo es: {saldo}')
    elif opcion == 2:
        retirada = int(input('¿Cuanto quieres retirar?: '))
        if saldo > retirada:
            print(f'Aqui tienes tus {retirada}€')
            saldo -= retirada
            print(f'Tu nuevo saldo es: {saldo}')
        else:
            print('No tienes saldo suficiente')
    elif opcion == 3:
        deposito = int(input('Introduce la cantidad a depositar: '))
        saldo += deposito
        print(f'Tu nuevo saldo es: {saldo}')
    elif opcion == 4:
        print('Saliendo...')
        break
    else:
        print('Opción no reconocida')