# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = int(input("Digite o valor do ângulo: "))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O valor do SENO do ângulo de {angulo}° é {sen:.2f}.")
print(f"O valor do COSSENO do ângulo de {angulo}° é {cos:.2f}.")
print(f"O valor da TANGENTE do ângulo de {angulo}° é {tan:.2f}.")