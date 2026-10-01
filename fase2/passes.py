# ========================
# Compilador online da OBI
# ========================

# Digite seu código aqui, por exemplo:
# print("resposta")

n = int(input())
t1 = 0
t2 = 0
j = []
while len(j) < n:
    linha = input().split()
    for x in linha:
        if x != '':
            j.append(int(x))
            
for i in range(len(j) - 1):
    # Se ambos forem maior que zero (Time 1) se for diferente doq ele mesmo ou seja, nao é ele mesmo ou seja toque, conta mais um pro time 1
    if j[i] > 0 and j[i+1] > 0 and j[i] != j[i+1]:
        t1 +=1
    # Vejamos que, ao contrario do time 1, o time 2 é de -1 a -100 pois entao ele nunca vai ser maior que zero, entao basta repetir o que fizemos anteriormente mais menor doq 0
    elif j[i] < 0 and j[i+1] < 0 and j[i] != j[i+1]:
        t2 += 1
print(t1)
print(t2)