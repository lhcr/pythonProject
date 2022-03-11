n=0
while True:
    n = int(input('Digite um número: '))
    if n<0:
        break
    for cont in range(0,10):
        print(f'{n} X {cont} = {n*cont}')