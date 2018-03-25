n=int(input())
i=0
vec=[]
while i<n:
    val=int(input())
    vec.append(val)
    i+=1
i=0
out=0
dentro=0
while i<len(vec):
    if vec[i]>=10 and vec[i]<=20:
        dentro+=1
    else:
        out+=1
    i+=1
print("%d in" %dentro)
print("%d out" %out)
