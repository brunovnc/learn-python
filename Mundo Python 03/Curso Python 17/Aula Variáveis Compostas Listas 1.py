#Diferente das Tuplas as Listas são mutavéis [].
num = [2, 5, 9, 1]
num[2] = 3 #Substituir valores
num.append(7) #Adicionar valores
num.sort(reverse=True) #Para inverter os valores em ordem
num.insert(2, 0) #Inserir o valor "0" na posição 2.
num.pop() #Excluir um valor. #Excluir um valor específico que aparecer primeiro.
print(num)
print(f'Essa lista tem {len(num)} elementos.')