aa = int(input())
bb = int(input())


a_str = str(aa)
b_str = str(bb)

maior = max(len(a_str), len(b_str))

b = b_str.zfill(maior)
a = a_str.zfill(maior)

resultado_a = []
resultado_b = []

for i in range(len(a)-1 ,-1 ,-1):
    if a[i] < b[i]:
        resultado_b.append(b[i])
    elif a[i] > b[i]:
        resultado_a.append(a[i])
    elif a[i] == b[i]:
        resultado_b.append(b[i])
        resultado_a.append(a[i])

if not resultado_a:
    resultado_a.append("-1")

if not resultado_b:
    resultado_b.append("-1")


final_a = int("".join(resultado_a[::-1]))
final_b = int("".join(resultado_b[::-1]))

if final_a > final_b:
    print(final_b, final_a)
else:
    print(final_a, final_b)
