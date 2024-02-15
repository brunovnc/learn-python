import time
primeirotermo = int(input('Digite o valor do termo aritmétrico: '))
razão = int(input('Digite o valor da razão aritmétrica: '))
contador = 1
termo = primeirotermo
total = 0 #O total é somado no total = total + termosextras. Somando os 10 + os extras e acumulando.
termosextras = 10 #O número 10 pois já foram mostrados 10 termos e depois pergunta se quer mostrar mais termos.

while termosextras != 0:
    total = total + termosextras
    while contador <= total:
        print(f'{termo}', end='-> ')
        termo += razão #termo vai somar a razão e vai acumulando, termo + razão.
        contador += 1 #contador vai acumulando a cada repetição até chegar ao 10 e perguntar se deseja mostrar mais termos ou finalizar.
    print('Pausa.')
    maistermos = str(input('Você deseja mostrar mais termos? [S/N]')).upper()
    if maistermos == 'S':
        termosextras = int(input('Quantos termos você quer mostrar a mais? '))
    else:
        print(f'Progressão finalizada com {total} termos apresentados.')
        break