# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A";
# Em que posição ela aparace a primeira vez;
# Em que posição ela aparece a última vez.

n = str(input("Digite uma frase: ")).lower()

print(f'A letra A aparece {n.count('a')} vezes na frase.')

print(f'A primeira letra A apareceu na posição {n.find('a')+1}.') 

print(f'A última letra A apareceu na posição {n.rfind('a')+1}.')

