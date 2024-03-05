alunos = {}

alunos['nome'] = str(input('Digite o seu nome: '))
alunos['média'] = float(input('Digite a sua média: '))

if alunos['média'] < 6:
    print(f'O aluno {alunos['nome']} está reprovado. Média: {alunos['média']}')
else:
    print(f'Parabéns! O aluno {alunos['nome']} está aprovado. Média: {alunos['média']}')