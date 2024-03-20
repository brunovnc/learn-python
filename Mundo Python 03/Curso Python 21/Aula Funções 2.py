#help() Para tirar dúvidas sobre comandos internos do Python.
help(input)
print(input.__doc__)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem.
    :param f: Fim da contagem.
    :param p: Passo da contagem.
    :return: Sem retorno.
    Função criada por Bruno Venâncio.
    """
    c = i
    while c <=f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

help(contador)