# Crie um programa onde usuário possa digitar vários valores e numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, exiba todos os valores únicos digitados, em ordem crescente.
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    for c, v in enumerate(lista):
        if lista.count(v) > 1:
            del lista[c]
    continuar = str(input('Quer continuar? [S/N]')).upper()[0]
    if continuar == 'N':
        break
lista.sort()
print(lista)