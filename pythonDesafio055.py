pma=0
pme=10000
for c in range(0,5):
    p=float(input('peso: '))
    if p<pme:
        pme=p
    if p>pma:
        pma=p
print('Pma: {} \n Pme: {} \n'.format(pma,pme))