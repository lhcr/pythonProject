lanche = ('Hambúrguer','Batata Frita','Heineken','Açai')
print(lanche[-1])
print(lanche[2:])
print(lanche[1:3])
print(lanche[:2])
for comida in lanche:
    print(f'Eu comi {comida}')
for count in range(0,len(lanche)):
    print(f'Eu comi {lanche[count]}')
for pos, comida in enumerate(lanche):
    print(f'Eu como {comida} na posição {pos} ')
print(sorted(lanche)) #sorted ordena em lista sua tupla
a= (1,2,5)
b= (6,7,4,5)
c=a+b #conctena tuplas
print(c.count(5)) # .count é método que conta o número de vezes que aparece determinado número
print(c.index(2)) # .index é método que mostra posição de um valor

pessoa = ('Luis', 35, 'M', 72.0) # TAD
print(pessoa)