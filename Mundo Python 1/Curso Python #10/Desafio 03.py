# Crie um programa que leia um número inteiro e msotre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número inteiro: '))

if n % 2:
    print(f"O número {n} é IMPAR.")
else:
    print(f"O número {n} é PAR.")