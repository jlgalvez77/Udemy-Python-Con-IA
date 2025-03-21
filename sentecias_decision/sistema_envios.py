print('*** Sistema de envíos ***')

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

destino = input('¿Dónde se envía el paquete? (Nacional/Internacional): ').lower()
peso = float(input('¿Cuál es el peso del paquete? (en kg): '))

if destino == 'nacional':
    coste_envio = TARIFA_NACIONAL * peso
elif destino == 'internacional':
    costo_envio = TARIFA_INTERNACIONAL * peso
else:
    print('Destino no válido')

print(f'El coste del envío es de {coste_envio}€')
