import time
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
time.sleep(1)

print('=-'*15)
print(' '*12, 'MENU:')
print('=-'*15)

while True:
    menu = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Digitar novamente\n[ 5 ] Sair\nDigite a opção desejada: '))
    if menu > 5:
        print('Comando invalido. Digite novamente!')
        time.sleep(1)
        print('=-'*15)
        print(' '*12, 'MENU:')
        print('=-'*15)
        menu = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Digitar novamente\n[ 5 ] Sair\nDigite a opção desejada: '))
    if menu == 5:
        print('Encerrando...')
        break
    if menu == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    if menu == 3 and n1 > n2:
        print(f'O maior número é o {n1}')
        break
    if menu == 3 and n2 > n1:
        print(f'O maior número é o {n2}')
        break
    if menu == 2:
        multiplicação = (n1 * n2)
        print(f'O resultado da multiplicação é {multiplicação}.')
        break
    if menu == 1:
        soma = (n1 + n2)
        print(f'O resultado da soma é {soma}.')
        break
print('Menu encerrado!')