from tokenize import String

from random import randint
n = s = res = 0
while True:
    n = int(input('Digite um número: '))
    escolha = str(input('Par(P) ou Impar(I): '))
    n2 = int(randint(0,100))
    res = (n+n2) % 2
    if  res == 0 and escolha != 'p':
        print(f'Você perdeu meu número é {n2} e você escolheu {escolha} o res foi {res}')
        break;
    elif res !=0 and escolha != 'i':
        print(f'Você perdeu meu número é {n2} e você escolheu {escolha} o res foi {res}')
        break;
    print('Você ganhou')
    s+=1
print(f'Você venceu {s} vezes antes de perder. ')