import random
#Digite o nome de 4 alunos e mostre a ordem da apresentação dos mesmos.
aluno1 = input('Qual o nome do primeiro aluno?')
aluno2 = input('Qual o nome do segundo aluno?')
aluno3 = input('Qual o nome do terceiro aluno?')
aluno4 = input('Qual o nome do quarto aluno?')

sequencia = f'{aluno1} {aluno2} {aluno3} {aluno4}'.split()
random.shuffle(sequencia)

print(f'A sequência da apresentação será respectivamente: {sequencia}')