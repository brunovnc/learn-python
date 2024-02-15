while True:
    n = int(input('Digite um número para mostrar a tabuada: '))
    if n < 0:
        print('Programa encerrado. Volte sempre!')
        break
    for c in range(1, 11):
        resultado = n*c
        print(f'{n} x {c} = {resultado}')