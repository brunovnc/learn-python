# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = int(input("Qual a largura da parede em metros? "))
altura = int(input("Qual a altura da parede em metros? "))
area = largura * altura
tinta = area / 2

print(f'O valor da área total é de {area}m² e serão necessários {tinta} litros de tinta.')
