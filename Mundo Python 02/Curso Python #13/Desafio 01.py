#Faça uma contagem regressiva para estouro dos fogos de artifícios, indo de 10 até 0 com uma pausa de 1 segundo entre eles:
import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('BUMMM!')