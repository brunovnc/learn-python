# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma lista de preços em forma tabular.
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
cont = 0

print('-'*40)
print(f'{'LISTA DE PREÇOS':^40}')
print('-'*40)

for c in (lista):
    if cont == 0:
        print(f'{c:.<30}', end='')
        cont += 1
    elif cont % 2 == 0:
        print(f'{c:.<30}', end='')
        cont += 1
    elif cont % 2 == 1:
        print(f'R${c:>7.2f}')
        cont += 1
print('-'*40)

# OU

print('-'*40)
print(f'{'LISTA DE PREÇOS':^40}')
print('-'*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*40)