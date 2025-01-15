# Faça um programa que jogue par ou ímpar. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas.
import random
cont = 0

while True:
    parimpar = str(input('Par ou Ímpar [P/I]? ')).upper()[0]
    while parimpar not in 'PI':
        parimpar = str(input('Par ou Ímpar [P/I]? ')).upper()[0]
    n = int(input('Um dolasi e já! '))
    sorteiomaquina = random.randint(0,10)
    maquina = print(f'Máquina: {sorteiomaquina}')
    somadedos = n + sorteiomaquina
    if somadedos % 2 == 0 and parimpar == 'P':
        print(f'Você venceu! A soma dos números é {somadedos}, logo é um número PAR.')
        cont += 1
    elif somadedos % 2 == 1 and parimpar == 'I':
        print(f'Você venceu! A soma dos números é {somadedos}, logo é um número IMPAR.')
        cont += 1
    else:
        print(f'Você perdeu HAHA! A soma dos números é {somadedos}, logo é um número IMPAR. \nVitórias consecutivas: {cont}')
        break