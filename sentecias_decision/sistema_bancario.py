print('*** Bienvenido al sistema bancario ***')

salir_sistema = input('¿Quieres salir del sistema (si/no)?: ').lower()

if not salir_sistema == 'si':
    print('Continuamoa dentro del sistema...')
else:
    print('Salimos del sistema...')