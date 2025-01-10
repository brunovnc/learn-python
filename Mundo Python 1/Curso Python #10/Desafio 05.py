# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais outro número: '))

maior = 0
menor = 0

if n1 > n2 and n2 > n3:
    maior = n1
    menor = n3
if n1 > n2 and n3 > n2:
    maior = n1
    menor = n2
if n2 > n1 and n1 > n3:
    maior = n2
    menor = n3
if n2 > n1 and n3 > n1:
    maior = n2
    menor = n1
if n3 > n1 and n2 > n1:
    maior = n3
    menor = n1
if n3 > n1 and n1 > n2:
    maior = n3
    menor = n2
if n3 > n2 and n2 > n1:
    maior = n3
    menor = n1
if n3 > n2 and n1 > n2:
    maior = n3
    menor = n2

print(f'O número maior é {maior} e o menor é {menor}.')