a,b=map(int,input().split())
if a>b:
    i=a
    a=b
    b=i
if b%a==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
