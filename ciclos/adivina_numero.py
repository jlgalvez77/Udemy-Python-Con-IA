import random

print('*** Adivina el número ***')

numero_secreto = random.randint(1, 50)
intentos = 0
INTENTOS_MAXIMOS = 6
numero_jugador = None

while numero_jugador != numero_secreto and intentos < INTENTOS_MAXIMOS:
    print('Tienes que adivinar un número entre 1 y 50')
    numero_jugador = int(input('Introduce un número entre 1 y 50: '))
    intentos += 1
    if numero_jugador > numero_secreto:
        print('El número secreto es menor, prueba otra vez.')
    elif numero_jugador < numero_secreto:
        print('El número secreto es mayor, prueba de nuevo.')
if numero_jugador == numero_secreto:
    print(f'Felicidades, adivinaste el número secreto en {intentos} intentos')
else:
    print(f'Has agotado los intentos para adivinar el número secreto')
    print(f'El número secreto era {numero_secreto}')