a,b,c,d=map(int,input().split())
if a>c:
    val1=(24-a)+c
    if d>b:
        val2=d-b
    else:
        val1-=1
        val2=60-(b-d)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(val1,val2))
elif a==c:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    val1=c-a
    if d>b:
        val2=d-b
    else:
        val1-=1
        val2=60-(b-d)
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(val1,val2))
