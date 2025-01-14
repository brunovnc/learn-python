# Crie um programa que leia vários números inteiros. No final, mostre a média entre todos os valores e qual foi o menor e maior. O programa deve perguntar se o usuário quer ou não continuar.
n = int(input('Digite um número: '))
continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]

soma = n
cont = 1
maior = 0
menor = 0

while continuar == 'S':
 n = int(input('Digite um número: '))
 soma += n
 cont += 1
 if cont == 2:
    maior = n
    menor = n
 if n > maior:
    maior = n
 if n < menor:
    menor = n
 continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
 if continuar == 'N' and cont > 1:
    print(f'Média: {soma / cont} \nMaior: {maior} \nMenor: {menor}')
    print('Encerrando...')

if continuar == 'N' and cont == 1:
   print(f'Média: {n} \nMaior: {n} \nMenor: {n}')
   print('Encerrando...')