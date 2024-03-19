#Agora ao invés de Tuplas vamos criar listas.
def dobra(list):
    pos = 0
    while pos < len(list): #Enquanto a posição for menor que a quantidade de elementos na lista...
        list[pos] *= 2 #Elemento da posição X será multiplicado por 2.
        pos += 1 #Posição será somada por +1.


# Programa Principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

#Outro teste...
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

# Programa Principal
soma(5, 2)
soma(2, 9, 4)