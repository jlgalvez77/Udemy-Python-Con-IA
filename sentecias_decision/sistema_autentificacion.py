print('*** Sistema de autenticación ***')

USER = 'admin'
PASSWORD = '123456'

user = input('Introduce tu nombre de usuario: ')
password = input('Introduce tu contraseña: ')

if user == USER and password == PASSWORD:
    print('Acceso permitido')
elif user == USER and password != PASSWORD:
    print('Contraseña incorrecta')
elif user != USER and password == PASSWORD:
    print('Usuario incorrecto')
else:
    print('Usuario y contraseña incorrectos')
    
