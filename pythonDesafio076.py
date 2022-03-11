prod = ('Suco', 1.25,'Limão', 0.3,'Doritos 400g', 2.53)
print('='*30)
for c in range (0,len(prod),2):
    print(f'{prod[c]} - {prod[c+1]}')
print('='*30)