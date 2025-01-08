# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math

oposto = float(input("Digite o valor do cateto oposto: "))
adjacente = float(input("Digite o valor do cateto adjacente: "))

print(f"O valor da Hipotenusa é igual {math.hypot(oposto, adjacente)}.")

# OU

c = math.sqrt(oposto ** 2 + adjacente ** 2)
print(f"O valor da Hipotenusa é igual {math.hypot(oposto, adjacente)}.")