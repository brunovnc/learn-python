primeirotermo = int(input('Digite o valor do termo aritmétrico: '))
razão = int(input('Digite o valor da razão aritmétrica: '))
termo = primeirotermo
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    contador += 1 #contador vai acumulando a cada repetição até chegar ao 10 e dar Break.
    termo += razão #termo vai somar a razão e vai acumulando, termo + razão.
print('Fim.')