# Melhore o Desafio Anterior, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
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
    if contador == 10:
        print(' > PAUSA')
        continuar = int(input(f'\nSe deseja prosseguir a PA, digite quantos números a mais você quer ver (Para encerrar, digite 0). '))
        contador -= continuar
        if continuar == 0:
            print('\nEncerrando...')