n=int(input())
print(n)
vec=[100,50,20,10,5,2,1]
vec1=[]
i=0
while i<len(vec):
    if n>=vec[i]:
        vec1.append(int(n/vec[i]))
    else:
        vec1.append(0)
    n=n-(vec1[i]*vec[i])
    i+=1
i=0
while i<len(vec):
    print("%d nota(s) de R$ %d,00" %(vec1[i],vec[i]))
    i+=1
