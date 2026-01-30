x = int(input())
y = int(input())

# while x < y:
#     if x % 5 == 2 or x % 5 == 3:
#         print(x)
#     x += 1

if x > y:
    x, y = y, x
    
for n in range(x +1, y):
    if n % 5 == 2 or n % 5 == 3:
        print(n)