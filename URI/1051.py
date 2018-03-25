n=float(input())
if n<=2000:
    print("Isento")
else:
    val2=0
    val4=0
    if n>=3000:
        val=(n-2000)-(n%3000)
        if n<=4500:
            val2=(n%3000)
        else:
            val2=(n-3000)-(n%4500)
            val4=n-4500
    else:
        val=n-2000
    val1=val*0.08
    val3=val2*0.18
    val5=val4*0.28
    print("R$ %.2f" %(val1+val3+val5))

    
