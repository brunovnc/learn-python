# Tuplas são IMUTÁVEIS.
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[1])
print(lanche[0:2])
print(lanche[-2])
print(lanche[-2:])
print(lanche[1:])
print(len(lanche))


for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('------------------')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')
print('------------------')
for pos, cont in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')


a = (2, 5, 4)
b = (5, 8, 4)
c = b + a
print(c)
print(c.count(5))
print(c.index(4))