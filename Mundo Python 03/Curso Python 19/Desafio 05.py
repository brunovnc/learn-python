dados = {}
copia = []
contador = 0
soma = media = 0

while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo: ')).upper()
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    copia.append(dados.copy())
    contador += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break

media = soma / contador
print(f'- No total foram cadastradas {contador} pessoas.')
print(f'- A média de idade do grupo é de {media} anos.')

print('- As mulheres cadastradas foram: ', end='')
for p in copia:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']} ', end='')

print('\n- Lista de pessoas que estão acima da média: ')
for p in copia:
    if p['Idade'] > media:
        print(f'\n{p['Nome']}, {p['Sexo']}, {p['Idade']}.')
print('Encerrado.')