# Leia o nome completo de uma pessoa e mostre:
# O nome com todas letras maiúsculas;
# O nome com todas minúsculas;
# Quantas letras ao todo sem contar o espaço;
# Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')

maiusculas = print(nome.upper())

minusculas = print(nome.lower())

semespacos = nome.replace(' ', '')
print(semespacos)
print(len(semespacos))

primeironome = nome.split()
print(len(primeironome[0]))