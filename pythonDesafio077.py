tupla=('banaeiouna','pera','chocolate','abacaxi')
for c in tupla:
    print(f'A palavra {c} possui as vogais:')
    for c1 in c:
        if c1.lower() in 'aeiou':
            print(c1, end=' ')
    print('')