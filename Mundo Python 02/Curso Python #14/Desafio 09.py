import time
média = 0
contador = 0
total = 0
continuar = 'S'
maior2 = 0
menor2 = 0

while continuar == 'S':
    n = int(input('Digite um número: '))
    contador += 1
    total += n
    média = total / contador
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Você deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        print('Encerrando...')
        time.sleep(1)
print(f'A média dos números digitados é {média:.2f}.\nO maior número entre eles foi {maior}.\nO menor número entre eles foi {menor}.')