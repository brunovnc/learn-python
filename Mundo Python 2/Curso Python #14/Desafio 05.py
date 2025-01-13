# Refaça o Desafio de Progressão Aritmétrica, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando While.
termo = int(input('Digite o primeiro número da Progressão Aritmétrica: '))
razao = int(input('Digite a razão (quantas casas pular) da Progressão Aritmétrica: '))

contador = 1
pa = 0

print(termo, end='')
while contador != 10:
    pa += razao
    if razao == 1 or razao == 0:
        termo += 1
        print(f' > {termo}', end='')
    elif razao > 1:
        print(f' > {termo + pa}', end='')
    contador += 1
print(' > FIM')