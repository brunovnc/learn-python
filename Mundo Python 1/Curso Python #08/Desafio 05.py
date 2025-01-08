# O professor quer sorttear a ordem da apresentação de trabalho dos alunos. Leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = str(input("Digite o nome do 1° aluno: "))
aluno2 = str(input("Digite o nome do 2° aluno: "))
aluno3 = str(input("Digite o nome do 3° aluno: "))
aluno4 = str(input("Digite o nome do 4° aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
embaralhar = random.shuffle(lista)

print(f"A ordem de apresentação será: \n1° aluno: {lista[0]}. \n2° aluno: {lista[1]}. \n3° aluno: {lista[2]}. \n4° aluno: {lista[3]}.")