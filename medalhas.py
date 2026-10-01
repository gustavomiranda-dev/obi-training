t1 = int(input())
t2 = int(input())
t3 = int(input())

maior = 0
menor = 0 
meio = 0

if t1 > t2 and t1 > t3:
    maior = 1
elif t2 > t1 and t2 > t3:
    maior = 2
else:
    maior = 3

if t1 < t2 and t1 < t3:
    menor = 1
elif t2 < t1 and t2 < t3:
    menor = 2
else:
    menor = 3



if maior == 1:

    if t2 > t3:
        meio = 2
        menor = 3
    else:
        menor = 2
        meio = 3

elif maior == 2:

    if t1 > t3:
        meio = 1
        menor = 3
    else:
        menor = 1
        meio = 3

else:

    if t1 > t2:
        meio = 1
        menor = 2
    else:
        menor = 1
        meio = 2

print(menor)
print(meio)
print(maior)