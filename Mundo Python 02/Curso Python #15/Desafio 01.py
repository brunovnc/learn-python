#Mesmo exercício que o Desafio 08 / Curso Python #14.

contador = 0
soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'No total foram digitados {contador} números e a soma entre eles é igual é {soma}.')
