from tokenize import String

from random import randint
n = s =0
while True:
    n = int(input('Digite um número: '))
    escolha = str(input('Par(P) ou Impar(I): '))
    n2 = int(randint)
    res = (n+n2) % 2
    if  res == 0 and escolha != 'P':
        break
    elif res !=0 and escolha != 'I':
        break
    print('Você ganhou')
    s+=1
print(f'Você venceu {s} vezes antes de perder. ')