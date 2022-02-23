s=0
for c in range(0,6):
    n=int(input('n{}: '.format(c)))
    if n%2==0:
        s=s+n
print(s)   