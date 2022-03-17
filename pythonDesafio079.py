from tokenize import String


p=0
numeros = []
while True:
    i = 0
    temp = int(input('Digite um valor: '))
    if p==0:
        numeros.insert(p,temp)
        p += 1
    else:
        for t,v in enumerate(numeros):
            print(v)
            if v==temp:
                i += 1
        if i==0:
            numeros.insert(p,temp)
            p+=1
    continuar = str(input('Deseja continuar?[S/N] '))
    if continuar in 'nN':
        break
print(numeros)
