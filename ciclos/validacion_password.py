print('*** Validación de Password ***')

while True:
    password = input('Introduce la contraseña a validar: ')
    if len(password) < 6:
        print('La contraseña debe de tener al menos 6 caracteres')
    else:
        print('Contraseña valida.')
        break