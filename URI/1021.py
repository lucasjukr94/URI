n=float(input())
if n>=0 and n<=1000000.00:
    vec=[100.00,50.00,20.00,10.00,5.00,2.00,1.00,0.50,0.25,0.10,0.05,0.01]
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
        if i==6:
            print("MOEDAS:")
        if i==0:
            print("NOTAS:")
        if i<6:
            print("%d nota(s) de R$ %.2f" %(int(vec1[i]),vec[i]))
        else:
            print("%d moeda(s) de R$ %.2f" %(int(vec1[i]),vec[i]))
        i+=1

    
