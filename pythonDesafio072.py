ex = ('zero','um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez')
n = int
while n not in range (0,10):
    n = int(input(f'Digite o número da tupla entre 0 e 10:  '))
print(ex[n])