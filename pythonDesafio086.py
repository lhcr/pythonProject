l = []
m = []
for i in range(0,9):
    l.append(int(input('Valor: ')))
l.sort() 
m.append(l[0:3])
m.append(l[3:6])
m.append(l[6:9])
print(f'[ {m[0][0]} ][ {m[0][1]} ][ {m[0][2]} ]\n[ {m[1][0]} ][ {m[1][1]} ][ {m[1][2]} ]\n[ {m[2][0]} ][ {m[2][1]} ][ {m[2][2]} ]')
# print(m)