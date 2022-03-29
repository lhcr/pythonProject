class mercadoria: #TAD = classe
    cod = 0
    nome = ' '
    pc = 1.0
    pv = 1.0


def NovaMercadoria():
    mc = mercadoria()#instancia o Obj
    mc.cod = int(input('Digite o código: '))
    return mc

def LucroMercadoria(mc):
    lucro = (mc.pv - mc.pc)*100.0/mc.pc
    return lucro