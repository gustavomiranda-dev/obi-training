"""
Problema: Maior sequência crescente
Dada uma lista de N números inteiros, você deve descobrir qual é o tamanho da maior sequência de números consecutivos que está em ordem estritamente crescente.
Uma sequência crescente é aquela em que cada número é maior que o anterior.
Entrada
A primeira linha contém um inteiro N.
A segunda linha contém N números inteiros.
Saída
Imprima um único inteiro: o tamanho da maior sequência crescente encontrada.
"""

n = int(input())

anterior = int(input())

maior = 1
cont = 1

for i in range(n - 1):
    atual = int(input())

    if atual > anterior:
        cont += 1
    else:
        cont = 1

    if cont > maior:
        maior = cont

    anterior = atual
print(maior)
