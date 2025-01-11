# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplo: APOS A SOPA, A SACADA DA CASA, O LOBO AMA O BOLO.
n = str(input('Digite uma frase: ')).upper().replace(' ', '')
inverter = n[::-1].replace(' ', '')

print(f'Frase digitada: {n}.')
print(f'Frase invertida: {inverter}.')

if n == inverter:
    print('A frase É um palíndromo.')
else:
    print('A frase NÃO é um palíndromo.')