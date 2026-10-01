# ======================================
# Gustavo futuro engenheiro de Software
# ======================================

# RUMO A FASE # UHUUUUUUU

import heapq

n, f = map(int, input().split())

#pega os pesos
pesos = []
while len(pesos) < n:
    linha = input().split()
    for x in linha:
        if x != '':
            pesos.append(int(x))

#cria a fila de acordo cum o tanto indicado
filas = [[] for o in range(f)]

#cria a fila afim de nao da o erro de memoria excedida(Em uma aplicacao normal nao era necessario essa lib, mais como mexer com fila requer muita memoria,
# torna-se nescessario)
heap = [(0, i) for i in range(f)]
heapq.heapify(heap)

#para cada peso em pesos
for peso in pesos:

    peso_total, idx = heapq.heappop(heap)
    filas[idx].append(peso)
    heapq.heappush(heap, (peso_total + peso, idx))

for i in range(f):
    print(*(filas[i]))
