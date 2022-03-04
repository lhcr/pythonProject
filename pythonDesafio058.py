import random
acertou = 'N'
palpite = 0
n = int
while acertou == 'N':
    n = int(input('Digite um número entre 0 e 10: '))
    nc = random.randint(0,10)
    if n>nc:
        print('Você ganho, eu escolhi o número {} !'.format(nc))
        acertou = 'S'
    elif n==nc:
        print('Empate, eu escolhi o número {} !'.format(nc))
    else:
        print('Você perdeu, eu escolhi o número {} !'.format(nc))
    palpite+=1
print('Você precisou de {} tentativas para me ganhar.'.format(palpite))
print('Fim')