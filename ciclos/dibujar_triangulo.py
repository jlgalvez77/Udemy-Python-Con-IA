print('*** Dibujar Triangulo ***')

filas = int(input('Proporciona el número de filas: '))

# Iterar sobre cada fila del triángulo
for fila in range(1, filas + 1):
    # Calculo de la cantidad de espacios en blanco
    espacios_en_blanco = ' ' * (filas - fila)
    # Calcular caracteres para la fila actual
    caracteres = '*' * (2 * fila - 1)
    # Imprime los espacios y los asteriscos
    print(f'{espacios_en_blanco}{caracteres}')