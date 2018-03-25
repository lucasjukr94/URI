vert=str(input())
mam=str(input())
oni=str(input())
if vert=="vertebrado":
    if mam=="ave":
        if oni=="carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if oni=="onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if mam=="inseto":
        if oni=="hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if oni=="hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
