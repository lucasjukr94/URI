n=int(input())
i=0
am=[]
ti=[]
while i<n:
    amount,tipo=map(str,input().split())
    am.append(int(amount))
    ti.append(tipo)
    i+=1
i=0
cobaias=0
coelhos=0
ratos=0
sapos=0
while i<n:
    cobaias=cobaias+am[i]
    if ti[i]=='C':
        coelhos+=am[i]
    elif ti[i]=='R':
        ratos+=am[i]
    else:
        sapos+=am[i]
    i+=1

print("Total: %d cobaias" %cobaias)
print("Total de coelhos: %d" %coelhos)
print("Total de ratos: %d" %ratos)
print("Total de sapos: %d" %sapos)
print("Percentual de coelhos: %.2f %%"%((coelhos/cobaias)*100))
print("Percentual de ratos: %.2f %%"%((ratos/cobaias)*100))
print("Percentual de sapos: %.2f %%"%((sapos/cobaias)*100))

    
