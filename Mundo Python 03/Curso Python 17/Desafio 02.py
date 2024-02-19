valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não foi possível adicionar.')
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        print(f'Você digitou os valores: {valores}.')
        break