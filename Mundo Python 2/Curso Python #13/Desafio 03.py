# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram de 1 até 500.
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        print(c, end=' ')
print(f'\nO valor total dos números ímpares múltiplos de 3 é igual a {s}.')