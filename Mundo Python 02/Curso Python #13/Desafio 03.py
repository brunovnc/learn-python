#Calcular todos os números impares que são múltiplos de 3 entre 1 e 500:

impar = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += +1
        impar += c
print(f'A soma de todos os {cont} valores solicitados é: {impar}.')

#O "cont" foi um contador que conta +1 ou seja, o total de valores que está sendo somado ali. 
#Já o impar está sendo somado e acumulando todos os valores solicitados.