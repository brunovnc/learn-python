n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim.')

#ou

inicio = int(input('Digite o número inicial: '))
fim = int(input('Digite o número final: '))
passo = int(input('Digite quantos números quer pular: '))

for c in range(inicio, fim+1, passo):
    print(c)
print('Fim.')

#ou

for c in range(0, 3):
    n2 = int(input('Digite um valor: '))
print('Fim.')