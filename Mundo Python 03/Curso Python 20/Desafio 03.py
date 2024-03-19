import time

def contador(i, f, p):
    print(f'Contagem de {i} até {f} pulando {p} casas.')
    
    if i < f: #Se o inicio for menor que o fim:
        cont = i #Contador = valor de inicio
        while cont <= f: #Enquanto o contador for menor que o valor final, repetir...
            print(f'{cont}', end=' ', flush=True) #Flush serve pro Time Sleep não acumular tempo.
            time.sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            time.sleep(0.5)
            cont -= p
        print('FIM')
    print('=-' *20)

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
pular = int(input('Pular casas: '))
contador(inicio, fim, pular)