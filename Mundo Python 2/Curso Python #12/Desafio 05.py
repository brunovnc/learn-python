# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingido:
# Média abaixo de 5.0: Reprovado;
# Média entre 5.0 e 6.9: Recuperação;
# Média 7.0 ou superior: Aprovado.
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'REPROVADO! Sua média é {media}.')
elif media >= 5 and media <= 6.9:
    print(f'RECUPERAÇÃO! Sua média é {media}.')
else:
    print(f'APROVADO! Sua média é {media}.')