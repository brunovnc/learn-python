# Crie um script que permita que o indivíduo digite qualquer coisa e identifique e mostre na tela qual o tipo primitivo do que foi digitado.
primitivo = input('Digite alguma coisa: ')

print(f"O tipo primitivo desse valor é {primitivo.__class__}")

print(f"É um alfabeto? {primitivo.isalpha()}")

print(f"É um número? {primitivo.isnumeric()}")

print(f"É um alfanumérico? {primitivo.isalnum()}")

print(f"Está em maiúsculas? {primitivo.isupper()}")

print(f"Está em minúsculas? {primitivo.islower()}")

print(f"Está capitalizada? {primitivo.istitle}")

print(f"Só tem espaços? {primitivo.isspace()}")