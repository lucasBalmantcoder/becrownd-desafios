x = int(input())
y = int(input())

# garante que o menor valor fique em x e o maior em y

if x > y:
    x, y = y, x

if x > y:
    x, y = y, x
    
soma = 0
for num in range(x, y + 1):
    if num % 13 != 0:
        soma += num
print(soma)
    
    