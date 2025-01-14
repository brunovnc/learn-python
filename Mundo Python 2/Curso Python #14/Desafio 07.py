# Escreva um programa que leia um númer n inteiro e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 > 1 > 1 > 2 > 3 > 5 > 8
n = int(input('Digite um número para a Sequência de Fibonacci: '))

contador = 3
t1 = 0
t2 = 1

print(f'{t1} -> {t2}' ,end='')
while contador <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')

# OU

n2 = int(input('Digite um número para a Sequência de Fibonacci: '))
a = 0
b = 1
c = 0
cont = 0
while cont < n2:
    print(f'{c} → ', end='')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')