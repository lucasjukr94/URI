n=int(input())
i=0
vec=[]
while i<n:
    val=int(input())
    vec.append(val)
    i+=1
i=0
while i<len(vec):
    if vec[i]%2==0 and vec[i]>0:
        print("EVEN POSITIVE")
    elif vec[i]%2==0 and vec[i]<0:
        print("EVEN NEGATIVE")
    elif vec[i]==0:
        print("NULL")
    elif vec[i]%2!=0 and vec[i]>0:
        print("ODD POSITIVE")
    else:
        print("ODD NEGATIVE")
    i+=1
