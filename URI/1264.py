n = int(input());
i=0;
while(i<n):
    val = input();
    arrVal = list(val);
    p=0;
    switch = True;
    arrA = [];
    arrB = [];
    while(p<len(arrVal)):
        if(arrVal[p]==' '):
            switch = False;
        else:
            if(switch):
                arrA.append(arrVal[p]);
            else:
                arrB.append(arrVal[p]);
        p+=1;
    if(len(arrB) > len(arrA)):
        print("nao encaixa");
    else:
        encaixa = True;
        j=len(arrA)-len(arrB);
        k=0;
        while(k<len(arrB)):
            if(arrA[j+k] != arrB[k]):
                encaixa = False;
            k+=1;
        if(encaixa):
            print("encaixa");
        else:
            print("nao encaixa");
    i+=1;
