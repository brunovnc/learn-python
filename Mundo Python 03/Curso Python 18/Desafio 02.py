principal = []
par = []
impar = []

for n in range(1, 8):
    num = int(input(f'Digite o {n}° valor: '))
    principal.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'Os valores inseridos foram: {sorted(principal)}')
print(f'Os valores par são: {sorted(par)}.')
print(f'Os valores impar são: {sorted(impar)}.')

print('=-'*30) #ou usando somente 1 lista:

principal2 = [[], []]
valor = 0

for n2 in range(1, 8):
    valor = int(input(f'Digite o {n2}° valor: '))
    principal2.append(valor)
    if valor % 2 == 0:
        principal2[0].append(valor)
    else:
        principal2[1].append(valor)
principal2[0].sort()
principal2[1].sort()
print(f'Os valores inseridos foram: {sorted(principal2)}')
print(f'Os valores par são: {principal2[0]}.')
print(f'Os valores impar são: {principal2[1]}.')