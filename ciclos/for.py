print('*** Repetición de un Mensaje ***')

mensaje = input('Introduce un mensaje a repetir: ')
repeticiones = int(input('Introduce las veces a repetir: '))

# Iterar sobre el rango de repeticiones
for _ in range(repeticiones):
    print(mensaje)