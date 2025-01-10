# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km p/ viagens de até 200Km e R$0.45 para mais longas.
km = float(input('Qual é a distância da viagem em Km? '))

if km <= 200:
    valor1 = km * 0.50
    print(f'O orçamento da viagem é no valor de R${valor1}.')
else:
    valor2 = km * 0.45
    print(f'O orçamento da viagem é no valor de R${valor2}.')