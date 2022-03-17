exp = str(input('Digite uma expressão: '))
pa = pf =0
for c,v in enumerate(exp):
    # print(v)
    if v=="(":
        pa+=1
    if v==")":
        pf+=1
if pa==pf:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
print(pa,pf)