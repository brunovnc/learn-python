#Digite um nome completo e reconheça o primeiro e último nome:
nome = input('Digite seu nome completo:').split()

primeironome = nome[0]
ultimonome = nome[-1]

print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é {primeironome}')
print(f'Seu último nome é {ultimonome}')

#ou utilizando len:

nomee = input('Digite seu nome completo:').split()

primeironomee = nomee[0]
ultimonomee = nomee[len(nomee)-1]

print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é {primeironomee}')
print(f'Seu último nome é {ultimonomee}')