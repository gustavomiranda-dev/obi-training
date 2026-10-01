n = int(input())

palitos = [int(k) for k in input().split()]
menor = 0

for i in range(len(palitos) - 1):

    if i == 0:
        menor = palitos [1] - palitos[0]
    atual = palitos[i]
    proximo = palitos[i + 1]

    diferenca = proximo - atual

    

    if diferenca < menor:
        menor = diferenca


print(menor)