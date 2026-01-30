x = int(input())

while True:
    z = int(input())
    if z > x:
        break
    
soma = 0
contador = 0
valor_atual = x

while soma <= z:
    soma += valor_atual
    valor_atual += 1
    contador += 1

print(contador)


# lucas@15A