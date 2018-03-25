a=[]
b=[]
i=0
n=int(input())
while i<n:
    ab,ba=map(int,input().split())
    a.append(ab)
    b.append(ba)
    i+=1
i=0
while i<n:
    mini=a[i]
    maxi=b[i]
    if mini>maxi:
        k=mini
        mini=maxi
        maxi=k
    j=1
    while j<=mini/2:
        if maxi%j==0 and mini%j==0:
            mdc=j
        j+=1
    print(mdc)
    i+=1
