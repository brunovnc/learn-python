n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
print(f'A soma entre {n1} e {n2} é {n1+n2}')

#Ou para facilitar:

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))

soma = (n1+n2)
sub = (n1-n2)
mult = (n1*n2)
div = (n1/n2)
pot = (n1**n2)
divi = (n1//n2)
rest = (n1%n2)

print(f'A potência de {n1} por {n2} é {pot}')
print(f'A soma é {soma} , a potencia é {pot} , a subtração é {sub}...')

#Dica sobre flutuantes:
print(f'A divisão dos valores é {div:.3f}')
#O comando :3.f fez com que o número flutuante se restriginsse em apenas 3 casas. Ex. 4/3 = 1,333

#Dica sobre quebrar linha:
print(f'A potência de {n1} por {n2} é {pot}' , end=' >>> ')
print(f'A soma é {soma} , a potencia é {pot} , a subtração é {sub}...')
#O comando end=' ' serve para que a linha não seja quebrada.
print(f'A potência de {n1} \n por {n2} \n é {pot}')
#O comando \n serve para quebrar a linha.