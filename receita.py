# ========================
# Compilador online da OBI
# ========================

# Digite seu código aqui, por exemplo:
# print("resposta")

#2 pao
# 4 ovos

p = int(input())
o = int(input())

cafe = 0

while p >= 2 and o >= 4:

    p -= 2
    o -= 4

    cafe += 1

print(cafe)