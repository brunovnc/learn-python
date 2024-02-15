#O "True" é um looping infinito que só para com o break. 

contador = 1
while True:
    print(contador, '-> ', end='')
    contador += 1
    if contador == 101:
        break
print('Fim.')

#Repetindo o Desafio 08 do Curso Python #14 sem a gambiarra (-999) utilizando Break.

n = 0
contador2 = 0
soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    contador2 += 1
    soma += n
print(f'No total foram digitados {contador2} números e a soma entre eles é igual é {soma}.')