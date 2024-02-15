#for c in range(1, 5):
#    n = int(input('Digite um valor: '))
#print('Fim.')

#E se vc quiser somente parar o input quando a pessoa digitar um número específico? Ou seja, não tem um final determinado.

n = 1 #n começa com 1:
while n != 0: #n for diferente de 0 então:
    n = int(input('Digite um valor: '))
print('Fim.')

#outro exemplo:

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim.')
