print('=-'*15)
print('          BANCO BV:')
print('=-'*15)

valor = int(input('Digite o valor a ser sacado: '))
total = valor
ced = 50 #50 pois é a cédula de maior valor do Desafio, se não tiver ela diminui o valor da cédula.
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1 #Contagem do total de cédulas utilizados.
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50: #Se não tiver mais cédulas de 50 então ced = 20 e assim vai progressivamente.
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('Volte sempre ao BANCO BV!')