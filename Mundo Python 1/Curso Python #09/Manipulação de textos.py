frase = "Curso em Vídeo Python"

# FATIAMENTO:
print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[9:])
print(frase[:9])
print(frase[9::3])
# Quando o espaço tá vazio indica o início ou o fim.

# ANÁLISE:
print(len(frase)) 
# Lê a quantidade de letras de uma string.

print(frase.count('o')) 
# Conta a quantidade total do caracter escolhido.

print(frase.count('o', 0, 13)) 
# Conta a quantidade do caracter escolhido em determinada parte da string.

print(frase.find('deo')) 
# Procura por caracteres específicos.

print('Curso' in frase) 
# Procura por uma palavra específica.

# TRANSFORMAÇÃO:
print(frase.replace('Python', 'Java')) 
# Substituia em segundo plano uma palavra por outra palavra.

print(frase.upper()) 
# Transforma todas as letras em maiúsculas.

print(frase.lower()) 
# Transforma todas as letras em minúsculas.

print(frase.capitalize()) 
#Transforma a letra inicial da frase em maiúscula e o restante minúsculas.

print(frase.title()) 
# Transforma as letras iniciais de cada palavra em maiúsculas.

teste = '   Aprenda Python  '
print(teste.strip()) 
# Removedor de caracteres.

print(teste.rstrip()) 
# Removedor de caracteres no final da string (lado direito).

print(teste.lstrip()) 
# Removedor de caracteres no início da string (lado esquerdo).

# DIVISÃO:
print(frase.split())
# Separa cada palavra em strings diferentes.

print('-'.join(frase))
# Separa cada letra em um caractere específico de sua escolha.

# EXTRA:
print("""Olá! tudo bem?
Meu nome é bruno tenho 22 anos
Sou Nutricionista e atualmente estudo
Programação. Obrigado pela atenção!""")

# COMBINAÇÕES:
print(frase.upper().count('O'))