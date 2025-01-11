# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input('Digite o seu peso atual: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O peso MAIOR lido foi de {maior}Kg.')
print(f'O peso MENOR lido foi de {menor}Kg.')