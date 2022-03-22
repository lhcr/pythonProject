pares = list()
impares = list()
valores = list()
for i in range(0,7):
    temp =int(input('Digite valor: '))
    if temp%2==0:
        pares.append(temp)
    else:
        impares.append(temp)
pares.sort()
impares.sort()
valores.append(pares[:])
valores.append(impares[:])
print(valores)