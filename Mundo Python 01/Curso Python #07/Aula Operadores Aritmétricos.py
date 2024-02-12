#Ordem de Procedência: 1. () 2. ** 3. * , / , // , % 4. + , -
#TESTE NO CONSOLE:
5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243

5**3 == 125
19/2 == 9.5
19//2 == 9

#Os operadores podem ser utilizados em strings também:
print('Oi'*5)
print('Oi'+'Olá')

#Pode utilizar os operadores para alinhar a formatação:
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome :>20}!')
#Alinhar para direita >
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome :<20}!')
#Alinhar para esquerda <
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome :^20}!')
#Centralizar ^
nome = input('Qual é o seu nome?')
print(f'Prazer em te conhecer {nome :=^20}!')
