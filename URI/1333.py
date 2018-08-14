while(True):
    try:
        f = int(input());
        if(f==0):
            break;
        arr=input();
        ci=list(map(int,arr.split(' ')));
        
    except EOFError:
        break;

