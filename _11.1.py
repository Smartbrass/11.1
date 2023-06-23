N = int(input())


def fact(N):
    Nf = 1
    Nff = 1
    Nfs = []
    for i in range(1, N+1):
        Nf *= i
    print(Nf)
    for x in range(1, Nf+1):
        Nff *= x
        Nfs.insert(0, Nff)
    print(Nfs)

    
fact(N)



