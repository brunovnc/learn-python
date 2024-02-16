#Variável Composta:
lanche1 = 'Hamburguer'
#Variável Composta: Tuplas
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3]) #O último número (elemento) nunca aparece.

print('-'*20)

print(len(lanche))

print('-'*20) #DIFERENTES FORMAS E RESULTADOS IGUAIS:

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')

print('-'*20) #Os dois resultam no mesmo resultado porém abaixo podemos utilizar coisas a mais.

for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}.')
print('Comi pra caramba!')

#Outra maneira de fazer a mesma situação:

for posiçao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posiçao}.')
print('Comi pra caramba!')

#Para deixar os elementos em ordem alfabética:

print(sorted(lanche))