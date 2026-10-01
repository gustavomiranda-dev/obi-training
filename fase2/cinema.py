# ======================================
# Gustavo futuro engenheiro de Software
# ======================================

# n = numero de pessoas
# m = quantidade de sessao
# c = maximo de pessoas de cada sessao

n, m, c = map(int, input().split())

hora_compra = []
while len(hora_compra) < n:
    linha = input().split()
    for x in linha:
        if x != '':
            hora_compra.append(int(x))

hora_inicio = []
while len(hora_inicio) < m:
    linha = input().split()
    for x in linha:
        if x != '':
            hora_inicio.append(int(x))

# pessoa
p = 0

#explicacao:
# bom, para cada hora que temos na lista hora_inicio, a gente cria o contador e faz um while, enquanto p(A pessoa) for menor que o numero maximo de pessoas e
# a hora da compra dessa pessoa for menor ou igual a hora maxima da sessao que ela comprou e se o contador for menor do que C que é o maximo de pessoas de cada sessao.
# se for true, o contador que é a quantidade de pessoas que podem entrar na sessao aumenta mais 1 e pula para a proxima pessoa, refazendo o loop.
# como nao consegui imprimir o contador em uma unica linha (o que influenciou a resposta da questao) fiz uma lista de cada contador e no final imprime cada valor com
# ,end=" " para nao quuebrar a linha e bingo! questao resolvida e rumo a fase 3 !
resposta = []

for hora in hora_inicio:
    contador = 0 
    while p < n and hora_compra[p] <= hora and contador < c:
        contador += 1
        p += 1
    resposta.append(contador)

for i in resposta:
    print(i ,end=" ")