nome = str(input('Qual o seu nome?'))
if nome == 'Bruno':
    print('Que nome lindo!')
print(f'Bom dia! Seja bem vindo {nome}!')

#outro exemplo

n1 = float(input('Digite a sua primeira nota:'))
n2 = float(input('Digite a sua segunda nota:'))

media = (n1+n2) /2

print(f'A sua média foi {media:.2f}')
if media >=6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais na próxima!')