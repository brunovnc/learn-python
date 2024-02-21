temporario = []
principal = []
maior = menor = 0

while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0: #Se eu não tenho ninguém cadastrado ainda, significa que o maior = menor = 1° peso cadastrado.
           maior = menor = temporario[1]
    else:
         if temporario[1] > maior:
              maior = temporario[1]
         if temporario[1] < menor:
              menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear() #A lista temporária vai sendo limpa toda vez que a repetição acontecer.
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'No total foram cadastrados {len(principal)} indivíduos.') #Nesse caso poderiamos usar um contador, mas essa é uma opção válida também.

print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in principal: #Se o P[1] for igual ao maior peso, mostrar o nome da pessoa.
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} ', end='')