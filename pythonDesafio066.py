n= s = cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n== 999:
        break
    s+=n
    cont+=1
print(f'Foram somados {cont} e o valor é {s}')