maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f'Peso do {p}° indivíduo: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}kg.')
print(f'O menor peso é {menor}kg.')

#Em resumo, se a primeira pessoa for o maior ou menor (if p == 1:) atribuindo o "maior" ou o "menor" a "peso".
#Caso contrário, se o "peso" for maior que o maior "p" ou menor que o menor "p", "maior" e "menor" serão atribuidos a "peso".