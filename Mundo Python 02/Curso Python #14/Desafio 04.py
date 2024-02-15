from math import factorial
n = int(input('Digite um valor para calcular seu fatorial: '))
fator = factorial(n)
print(f'O fatorial de {n} é {fator}.')

#Porém, não queremos usar o modolo Math nesse desafio. Então:

n2 = int(input('Digite um valor para calcular seu fatorial: '))
contador = n2
fator2 = 1 #Se começar por 0 a multiplicação vai dar 0.

print(f'Calculando {n2}!...')

while contador > 0:
    print(f'{contador}', end='') #End serve para não pular linhas, continuando na mesma.
    print(' x ' if contador > 1 else ' = ', end='') #Mostre x (indicando multiplicação) para os nómeros maiores que 1, se for 1 significa que é pra mostrar o =.
    fator2 *= contador
    contador -= 1
print(f'{fator2}.')