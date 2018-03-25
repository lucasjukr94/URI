n=int(input())
ano=n/365
mes=(n-int(ano)*365)/30
dia=n-int(ano)*365-int(mes)*30
print("%d ano(s)\n%d mes(es)\n%d dia(s)"%(int(ano),int(mes),int(dia)))
