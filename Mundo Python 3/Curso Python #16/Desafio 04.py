# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9;
# Em que posição foi digitado o primeiro valor 3;
# Quais foram os números pares.
num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))

print(f'Você digitou os valores {num}.')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro número 3 está na {num.index(3)+1}ª posição.')
else:
    print('O número 3 não foi encontrado.')
print('Números pares: ', end='')
for c in (num):
    if c % 2 == 0:
        print(c, end=' ')