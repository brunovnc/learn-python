largura = float(input('Qual a largura da parede em metros?'))
altura = float(input('Qual a altura da parede em metros?'))

área = largura*altura
tinta = área/2
#Cada litro de tinta pinta 2m².
print(f'Sua parede têm uma área de {área}m² e consequentemente precisará comprar {tinta} litros de tinta.')
