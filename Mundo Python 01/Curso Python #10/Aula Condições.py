#se significa if / se não significa else:

tempo = int(input('Quantos anos tem o seu carro?'))

if tempo <=3:
    print('Seu carro é novo!')
else:
    print('Seu carro é antigo!')
print('Análise encerrada!')

#ou

tempoo = int(input('Quantos anos tem o seu carro?'))
print('Seu carro é novo!' if tempoo <=3 else 'Seu carro é antigo!')
print('Análise encerrada!')