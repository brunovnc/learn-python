# Faça um programaque leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
nome = str(input('Digite o seu nome completo: '))
divisor = nome.split()

print(f'Primeiro nome: {divisor[0]}.')
print(f'Segundo nome: {divisor[1]}.')