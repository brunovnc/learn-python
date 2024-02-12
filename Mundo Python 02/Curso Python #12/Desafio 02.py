print('=-'*20)
print('Conversor de Números:')
print('=-'*20)

num = int(input('Digite um número: '))

binário = bin(num)
octal = oct(num)
hexadecimal = hex(num)

conversão =  int(input(f'Digite qual será a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))

if conversão == 1:
    print(f'O número {num} convertido em binário é: {binário}.')

elif conversão == 2:
    print(f'O número {num} convertido em octal é: {octal}.')

elif conversão ==3:
    print(f'O número {num} convertido em hexadecimal é: {hexadecimal}.')

else:
    print('Esse número não está na lista acima!')