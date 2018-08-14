def getCharFromIndex(index):
    if(index == 0):
        return 'a';
    elif(index == 1):
        return 'b';
    elif(index == 2):
        return 'c';
    elif(index == 3):
        return 'd';
    elif(index == 4):
        return 'e';
    elif(index == 5):
        return 'f';
    elif(index == 6):
        return 'g';
    elif(index == 7):
        return 'h';
    elif(index == 8):
        return 'i';
    elif(index == 9):
        return 'j';
    elif(index == 10):
        return 'k';
    elif(index == 11):
        return 'l';
    elif(index == 12):
        return 'm';
    elif(index == 13):
        return 'n';
    elif(index == 14):
        return 'o';
    elif(index == 15):
        return 'p';
    elif(index == 16):
        return 'q';
    elif(index == 17):
        return 'r';
    elif(index == 18):
        return 's';
    elif(index == 19):
        return 't';
    elif(index == 20):
        return 'u';
    elif(index == 21):
        return 'v';
    elif(index == 22):
        return 'w';
    elif(index == 23):
        return 'x';
    elif(index == 24):
        return 'y';
    elif(index == 25):
        return 'z';
    else:
        return '';
    

##############a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z###########
dictionary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
while(True):
    try:
        var = input();
        arr = list(var);
        i=0;
        while(i<len(arr)):
            if(arr[i] == 'a'):
                dictionary[0] = 1;
            elif(arr[i] == 'b'):
                dictionary[1] = 1;
            elif(arr[i] == 'c'):
                dictionary[2] = 1;
            elif(arr[i] == 'd'):
                dictionary[3] = 1;
            elif(arr[i] == 'e'):
                dictionary[4] = 1;
            elif(arr[i] == 'f'):
                dictionary[5] = 1;
            elif(arr[i] == 'g'):
                dictionary[6] = 1;
            elif(arr[i] == 'h'):
                dictionary[7] = 1;
            elif(arr[i] == 'i'):
                dictionary[8] = 1;
            elif(arr[i] == 'j'):
                dictionary[9] = 1;
            elif(arr[i] == 'k'):
                dictionary[10] = 1;
            elif(arr[i] == 'l'):
                dictionary[11] = 1;
            elif(arr[i] == 'm'):
                dictionary[12] = 1;
            elif(arr[i] == 'n'):
                dictionary[13] = 1;
            elif(arr[i] == 'o'):
                dictionary[14] = 1;
            elif(arr[i] == 'p'):
                dictionary[15] = 1;
            elif(arr[i] == 'q'):
                dictionary[16] = 1;
            elif(arr[i] == 'r'):
                dictionary[17] = 1;
            elif(arr[i] == 's'):
                dictionary[18] = 1;
            elif(arr[i] == 't'):
                dictionary[19] = 1;
            elif(arr[i] == 'u'):
                dictionary[20] = 1;
            elif(arr[i] == 'v'):
                dictionary[21] = 1;
            elif(arr[i] == 'w'):
                dictionary[22] = 1;
            elif(arr[i] == 'x'):
                dictionary[23] = 1;
            elif(arr[i] == 'y'):
                dictionary[24] = 1;
            elif(arr[i] == 'z'):
                dictionary[25] = 1;
            i+=1;
        i=0;
        ini = '';
        fim = '';
        cc = 0;
        result = [];
        while(i<len(dictionary)):
            if(dictionary[i] == 1 and cc == 0):
                ini = getCharFromIndex(i);
                cc+=1;
            elif(dictionary[i] == 1 and cc != 0):
                fim = getCharFromIndex(i);
                cc+=1;
            else:
                cc = 0;
                if(fim == ''):
                    fim = ini;
                if(ini != '' and fim != ''):
                    result.append(ini + ":" + fim);
                ini = '';
                fim = '';
            i+=1;
        if(ini != '' and fim != ''):
            result.append(ini + ":" + fim);
        if(dictionary[24]==0 and dictionary[25]==1):
            result.append("z:z");
        i=0;
        resultString = "";
        while(i<len(result)):
            if(len(result)==0):
                resultString = " ";
            elif(len(result)==i+1):
                resultString += result[i]
            else:
                resultString += result[i] + ", "
            i+=1;
        print(resultString);
        result = [];
        dictionary = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    except EOFError:
        break;
