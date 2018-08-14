def BinaryToDecimal(arrVal):
    length = len(arrVal);
    i=0;
    soma=0;
    while(i<length):
        if(arrVal[i]=="#"):
            break;
        soma += int(arrVal[i]) * pow(2,length-i);
        i+=1;
    print(soma/2);
    return soma;

while(True):
    try:
        val = input();
        arrVal = list(val);
        decimalVal = BinaryToDecimal(arrVal);
        if(decimalVal%131071==0):
            print("YES");
        else:
            print("NO");
    except EOFError:
        break;
