#OPERADORES ARITMÉTICOS:
print(5 + 2)
# + Adição

print(5 - 2)
# - Subtração

print(5 * 2)
# * Multiplicação

print(6 / 2)
# / Divisão

print(5 ** 2)
# ** Potência

print(5 // 2) # O 2 vai ser multiplicado por 2 (Divisão Inteira) que vai dar 4, subtraindo pelo 5 vai faltar 1 (Resto da Divisão).
# // Divisão Inteira

print(5 % 2) # O 2 vai ser multiplicado por 2 (Divisão Inteira) que vai dar 4, subtraindo pelo 5 vai faltar 1 (Resto da Divisão).
# % Resto da Divisão

# ORDEM DE PROCEDÊNCIA:
# () >>> ** >>> * / // % >>> + -

print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

print(81 ** (1/2)) 
# Raíz Quadrada

print(81 ** (1/3)) 
# Raíz Cúbica

# ALINHAMENTOS:
nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer {nome :>20}!') 
# Alinhar para direita >

print(f'Prazer em te conhecer {nome :<20}!') 
# Alinhar para esquerda <

print(f'Prazer em te conhecer {nome :^20}!') 
print(f'Prazer em te conhecer {nome :=^20}!')
# Centralizar ^

print('Vitórias: 44 \nDerrotas: 2') 
# \n Serve para pular linhas.

print('Meu nome é Bruno e tenho', end= " >>> ")
print('999 vitórias no Brawlhalla.')
# end= " " Serve para unir a linha atual com a linha abaixo