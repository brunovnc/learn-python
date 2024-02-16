a = (1, 5, 4)
b = (2, 3, 7, 6, 7)
c = a + b

print(c)
print(sorted(c))
print(len(c))
print(c.count(5)) #Quantas vezes aparece "5" na variável c.
print(c.index(7)) #Para informar qual a posição que o "8" está na variável c.
print(c.index(7, 6)) #Para informar qual a posição que "7" está após a posição 5 pois já sabemos que na posição 5 têm um "7".

print('-'*20)

pessoa = ('Bruno', 21, 'M', 1.70)
print(pessoa)
#O comando del() serve para deletar uma variável. Ex. del(pessoa)