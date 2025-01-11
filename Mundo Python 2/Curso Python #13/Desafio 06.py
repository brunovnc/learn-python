# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input('Digite o primeiro número da Progressão Aritmétrica: '))
razao = int(input('Digite a razão (quantas casas pular) da Progressão Aritmétrica: '))
decimo = termo + 10 * razao

for c in range(termo, decimo, razao):
    print(c, end=' > ')
print('FIM!')