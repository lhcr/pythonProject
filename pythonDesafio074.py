import random
maior = 0
tupla = (random.randint(0,5), random.randint(0,15), random.randint(0,35), random.randint(0,25), random.randint(0,5))
for count in range(0,len(tupla)):
  
    if count == 0:
        menor = tupla[count]
    elif tupla[count]<menor:
        menor = tupla[count]
    elif tupla[count]>maior:
        maior = tupla[count]
    
print(f'o maior é {maior}\n o menor é {menor}\n da tupla:\n{tupla}')