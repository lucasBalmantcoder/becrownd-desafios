
v = []

while True:
    x = int(input())
    if x == 0:
        break
    v.append(x)

for X in v:
    if X % 2 != 0:
        X += 1

    soma = 0
    for _ in range(5):
        soma += X
        X += 2

    print(soma)