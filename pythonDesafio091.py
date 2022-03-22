from audioop import reverse
import random
dado = {}
for i in range(0,4):
    dado[f'jogador{i+1}'] = int(random.randint(1,6))
# dado.sort(reverse=True)

print(dado)