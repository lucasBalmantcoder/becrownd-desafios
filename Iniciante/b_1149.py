
v = list(map(int, input().split()))

a = v[0]
n = None

for num in v[1:]:
    if num > 0:    
        n = num
        break

if n is None:
    exit()
    
s = sum(a + i for i in range(n))

print(s)
