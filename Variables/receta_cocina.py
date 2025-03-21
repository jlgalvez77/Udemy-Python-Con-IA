print('*** Receta de Cocina ***')

nombre_receta = input('¿Cual es el nombre de la receta?: ')
ingredientes = input('¿Cuales son los ingredientes?: ')
tiempo = int(input('¿Cual es el tiempo de preparación en minutos?'))
dificultad = input('¿Cual es su dificultad? (Facil/Media/Alta): ')

print(f'Nombre: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de Preparación: {tiempo}')
print(f'Dificultad: {dificultad}')