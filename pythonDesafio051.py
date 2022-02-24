n=int(input('n: '))
r=int(input('R: '))
for c in range(n,10*r, r):
    print(n,c)
    n=n+c