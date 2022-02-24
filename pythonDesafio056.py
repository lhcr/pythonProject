md=0
idadeHVelho=0
mulheresIdade=0
for c in range(0,4):
    nome=str(input('nome: \n'))
    idade=int(input('idade: \n'))
    sexo=str(input('sexo: \n'))
    if sexo in'Mm' and idade>idadeHVelho:
            idadeHVelho=idade
            homemVelho=nome
    elif sexo in 'Ff' and idade<20:
            mulheresIdade+=1
    md+=idade
md=md/4
print(' média: {} \n Homem mais velho: {} \n Mulheres com menos de 20 anos: {} \n'.format(md,idadeHVelho,mulheresIdade))
