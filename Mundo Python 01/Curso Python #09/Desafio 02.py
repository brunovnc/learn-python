#Leia os números de 0 a 9999 e mostre na tela cada um dos digitos separados:
#n = int(input('Digite um número de 0 a 9999:'))
#num = str(n)

#print(f'Analisando o número {n}...')

#print(f'Unidade: {num[3]}')
#print(f'Dezena: {num[2]}')
#print(f'Centena: {num[1]}')
#print(f'Milhar: {num[0]}')
#Dessa maneira mais "fácil", não será possível ler números com 3 casas decimais ou menos, vai dar erro.

n = int(input('Digite um número de 0 a 9999:'))

print(f'Analisando o número {n}...')

unidade = n // 1 % 10
#Dividimos por inteiro o número por 1 e depois pegamos o resto da divisão dividindo por 10.
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
