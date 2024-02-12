import math
#Digite um angulo e mostre o seno, cosseno e tangente do mesmo.
angulo = int(input('Digite o valor de um ângulo:'))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'Visto o angulo de {angulo}° o seu seno é {seno:.3f}, o seu cosseno é {cosseno:.3f} e o seu tangente é {tangente:.3f}.')
