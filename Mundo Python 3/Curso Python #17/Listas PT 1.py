# Listas são MUTÁVEIS [] / list().
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Sorvete'
print(lanche)

lanche.append('Cookie')
print(lanche)

lanche.insert(0, 'Hotdog')
print(lanche)

del lanche[3]
lanche.pop(2)
lanche.remove('Cookie')
print(lanche)

if 'Pizza' in lanche:
    lanche.remove('Pizza')

# Mais

valores = list(range(4, 11))
print(valores)

valores2 = [8, 2, 5, 4, 9, 3, 0]
valores2.sort()
print(valores2)

valores2.sort(reverse=True)
print(valores2)

valores3 = [] # Ou pode ser usado também list().
for cont in range(0, 5):
    valores3.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores3):
    print(f'Na posição {c} encontrei o valor {v}.')

# Criando uma cópia de uma Lista:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')