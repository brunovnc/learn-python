# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h mostre uma mensagem falando que foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('VOCÊ PASSOU POR UM RADAR! Qual a velocidade em que estava conduzindo o veículo? '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade e o radar foi acionado! Multa de R${multa},00.')
else:
    print('Parabéns. Você está dentro do limite de velocidade.')