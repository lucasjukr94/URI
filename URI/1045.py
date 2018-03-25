a,b,c=map(float,input().split())
if b>c and b>a:
    i=a
    a=b
    b=i
elif c>b and c>a:
    i=a
    a=c
    c=i
if a>=(b+c):
    print("NAO FORMA TRIANGULO")
else:
    if (a*a)==((b*b)+(c*c)):
        print("TRIANGULO RETANGULO")
    if (a*a)>((b*b)+(c*c)):
        print("TRIANGULO OBTUSANGULO")
    if (a*a)<((b*b)+(c*c)):
        print("TRIANGULO ACUTANGULO")
    if a==b and a==c:
        print("TRIANGULO EQUILATERO")
    if (b==c and b!=a) or (a==c and a!=b) or (a==b and a!=c):
        print("TRIANGULO ISOSCELES")


