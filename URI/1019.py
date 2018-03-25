n=int(input())
hora=(n/60)/60
minuto=(hora-int(hora))*60
segundo=n%60
print("%d:%d:%d"%(int(hora),int(minuto),int(segundo)))

    
