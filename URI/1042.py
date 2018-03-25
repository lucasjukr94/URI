a,b,c=map(int,input().split())
vec=[a,b,c]
vec1=[]
if a>b and a>c:
    vec1.append(a)
    if b>c:
        vec1.append(b)
        vec1.append(c)
    else:
        vec1.append(c)
        vec1.append(b)
elif b>a and b>c:
    vec1.append(b)
    if a>c:
        vec1.append(a)
        vec1.append(c)
    else:
        vec1.append(c)
        vec1.append(a)
else:
    vec1.append(c)
    if a>b:
        vec1.append(a)
        vec1.append(b)
    else:
        vec1.append(b)
        vec1.append(a)
print(vec1[2])
print(vec1[1])
print(vec1[0])
print("")
print(vec[0])
print(vec[1])
print(vec[2])
