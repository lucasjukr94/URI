a,b,c=map(float,input().split())
if b>a and b>c:
    i=a
    a=b
    b=i
elif c>a and c>b:
    i=a
    a=c
    c=i
if a>=b+c:
    print("Area = %.1f" %(((a+b)*c)/2))
else:
    print("Perimetro = %.1f" %(a+b+c))
