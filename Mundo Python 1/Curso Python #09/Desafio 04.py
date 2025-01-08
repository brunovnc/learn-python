# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o seu nome: ')).upper()

if nome.find('SILVA') == -1:
    print("Você não possue SILVA em seu nome.")
else:
    print("Você possue o nome SILVA em seu nome.")