from tokenize import String


homem = maIdade = muVinte = 0
while True:
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Informe o sexo: [M/F] '))
    if idade>18:
        maIdade+=1
    if sexo in 'fF':
        if idade<20:
            muVinte+=1
    else:
        homem+=1       
        
    pergunta = str(input("Deseja continuar? [S/N] "))
    if pergunta in 'nN':
        break
print(f'Foram cadastrados:\n{homem} homens\n{maIdade} pessoas maiores de 18 anos\n{muVinte} mulheres com menos de 20 anos. ')


