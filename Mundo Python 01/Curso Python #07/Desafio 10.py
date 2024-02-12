dias = float(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km rodados?'))

valordiario = dias * 60
valorkm = km * 0.15
valortotal = valordiario + valorkm

print(f'O valor total do aluguel é de R${valortotal} visto que foram gastos R${valordiario} da diária e R${valorkm} de km rodados.')