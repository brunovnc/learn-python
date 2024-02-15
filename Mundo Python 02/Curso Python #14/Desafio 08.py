n = 0
contador = 0
soma = 0

while n < 999:
    n = int(input('Digite um número: '))
    contador += 1
    soma += n
print(f'No total foram digitados {contador - 1} números e a soma entre eles é igual é {soma - 999}.')