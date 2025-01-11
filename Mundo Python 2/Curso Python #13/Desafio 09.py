# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maioridade = 0
menoridade = 0

for c in range(0,7):
    ano = int(input('Digite o ano do seu nascimento: '))
    idade = 2025 - ano
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f'No total {maioridade} pessoas já são MAIOR de idade e {menoridade} pessoas são MENOR de idade.')