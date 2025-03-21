print('*** Sistema de descuentos ***')
CANTIDAD_MINIMA = 1000
cantidad_gastada = float(input('Introduce la cantidad gastada: '))
miembro = input('Eres miembro de la tienda? (si/no): ').lower()
descuento = 0
if cantidad_gastada >= CANTIDAD_MINIMA and miembro == 'si':
    descuento = 0.1
elif cantidad_gastada < CANTIDAD_MINIMA and miembro == 'si':
    descuento = 0.05
else:
    print('No tienes descuentos')
    descuento = 0

if descuento != 0:
    print(f'Tienes un descuento de {descuento * 100}%')
    print(f'El total a pagar es: {cantidad_gastada - (cantidad_gastada * descuento)}')
else:
    print(f'Valor de la compra: {cantidad_gastada}')