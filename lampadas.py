n = int(input())

vezes = list(map(int, input().split()))

a = 0
b = 0

for n in vezes:

    if n == 1 and a == 0:
        a = 1
    elif n == 1 and a == 1:
        a = 0


    elif n == 2 and a == 0 and b == 0:
        a = 1
        b = 1
    elif n == 2 and a == 1 and b == 1:
        a = 0
        b = 0
    elif n == 2 and a == 0 and b == 1:
        a = 1
        b = 0
    elif n == 2 and a == 1 and b == 0:
        a = 0
        b = 1

print(a)
print(b)
    