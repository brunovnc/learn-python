#Criar produtos e colocar descontos de acordo com a forma de pagamento:
produto = int(input('O que você deseja comprar?\n1 - Camisa | R$60.00\n2 - Calça | R$80.00\n3 - Tênis | R$120.00\n'))
pagamento = int(input('Qual será a forma de pagamento?\n1 - À vista/Cheque (10% OFF)\n2 - 1x Cartão de Crédito (5% OFF)\n3 - 2x Cartão de Crédito\n4 - 3x ou + Cartão de Crédito (20% Juros)\n'))

#À vista/Cheque (10% OFF):
camisa = 60 - (10/100 * 60)
calça = 80 - (10/100 * 80)
tênis = 120 - (10/100 * 120)

if produto == 1 and pagamento == 1:
    print(f'O valor do produto à vista é de R${camisa}.')
elif produto == 2 and pagamento == 1:
    print(f'O valor do produto à vista é de R${calça}.')
elif produto == 3 and pagamento == 1:
    print(f'O valor do produto à vista é de R${tênis}')

#1x Cartão de Crédito (5% OFF):
camisa2 = 60 - (5/100 * 60)
calça2 = 80 - (5/100 * 80)
tênis2 = 120 - (5/100 * 120)

if produto == 1 and pagamento == 2:
    print(f'O valor do produto à vista no cartão de crédito é de R${camisa2}.')
elif produto == 2 and pagamento == 2:
    print(f'O valor do produto à vista no cartão de crédito é de R${calça2}.')
elif produto == 3 and pagamento == 2:
    print(f'O valor do produto à vista no cartão de crédito é de R${tênis2}.')

#2x Cartão de Crédito:
if produto == 1 and pagamento == 3:
    print(f'O valor do produto parcelado 2x no cartão de crédito é de R$60.')
elif produto == 2 and pagamento == 3:
    print(f'O valor do produto parcelado 2x no cartão de crédito é de R$80.')
elif produto == 3 and pagamento == 3:
    print(f'O valor do produto parcelado 2x no cartão de crédito é de R$120.')

#3x ou + Cartão de Crédito (20% Juros):
camisa3 = (20/100 * 60) + 60
calça3 = (20/100 * 80) + 80
tênis3 = (20/100 * 120) + 120

if produto == 1 and pagamento == 4:
    print(f'O valor do produto parcelado 3x ou + no cartão de crédito é de R${camisa3}.')
elif produto == 2 and pagamento == 4:
    print(f'O valor do produto parcelado 3x ou + no cartão de crédito é de R${calça3}.')
elif produto == 3 and pagamento == 4:
    print(f'O valor do produto parcelado 3x ou + no cartão de crédito é de R${tênis3}.')