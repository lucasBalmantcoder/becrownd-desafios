contagem = {
     1 :0,
     2 :0,
     3 :0
}

while True:
    x = int(input())
    
    if x in contagem:
        contagem[x] += 1
    elif x == 4:
        break
    
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool: {}".format(contagem[1]))
print("Gasolina: {}".format(contagem[2]))
print("Diesel: {}".format(contagem[3]))
