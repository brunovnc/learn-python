#Leia 6 números inteiros e realize a soma deles caso os números sejam pares:

print('Digite 6 números inteiros respectivamente abaixo.')

par = 0
for c in range(1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += n
print(par)