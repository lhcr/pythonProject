numeros = []
p =0
while True:
    temp =int(input('Digite um valor: '))

    if p==0:
        numeros.insert(p,temp)
        p+=1
    else:
        for i,v in enumerate(numeros):
            if temp<v:
                p = i
                break
        numeros.insert(p,temp)
        p += 1
        
    continuar = str(input('Deseja continuar?[S/N] '))
    if continuar in 'nN':
        break
print(numeros)