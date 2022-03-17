#numeros = [2,6,1,3,9]
numeros = []
ma = me = posMa = posMe = 0
for p in range(0,5):
    temp = int(input('Digite um valor: '))
    numeros.insert(p,temp)
    if p==0:
        me = numeros[p]
        ma=numeros[p]
    elif numeros[p]>ma:
        ma = numeros[p]
        posMa = p
    elif numeros[p]<me:
        me = numeros[p]
        posMe = p
print(f'A lista é {numeros}')
print(f'O maior número é {ma} e está na posição {posMa}\nO menor número é {me} e está na posição {posMe}.')
