# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
import time
n = int(input('Digite um número inteiro: '))
conversao = int(input('Escolha a base de conversão 1, 2 ou 3: '))
print('---------CONVERTENDO-----------')
time.sleep(2)

if conversao == 1:
    print(f'Binário: {bin(n)}.')
elif conversao == 2:
    print(f'Octal: {oct(n)}.')
elif(conversao == 3):
    print(f'Hexadecimal: {hex(n)}.')
else:
    print('Essa opção não existe! Tente novamente.')