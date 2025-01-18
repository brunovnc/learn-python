# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No fim, mostre qual foi o maior e o menor valor, e as suas respectivas posições na lista.
lista = []
maior = menor = 0
posicaomaior = posicaomenor = 0

for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    for c, v in enumerate(lista):
        if cont == 0:
            maior = v
            menor = v
            posicaomaior = c
            posicaomenor = c
        elif v > maior:
            maior = v
            posicaomaior = c
        elif v < menor:
            menor = v
            posicaomenor = c
print(f'O maior número é {maior} e está na posição {posicaomaior+1}.')
print(f'O menor número é {menor} e está na posição {posicaomenor+1}.')