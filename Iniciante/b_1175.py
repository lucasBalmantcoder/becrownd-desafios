v = []

for _ in range(20):
    v.append(int(input()))
    
for i in range(10):
    v[i], v[19 - i] = v[19 - i], v[i]

for i in range(20):
    print(f"N[{i}] = {v[i]}")