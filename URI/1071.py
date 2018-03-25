a=int(input())
b=int(input())
if a>b:
    c=a
    a=b
    b=c
i=a+1
soma=0
while i<b:
    if i%2!=0:
        soma=soma+i;
    i+=1
print(soma)
