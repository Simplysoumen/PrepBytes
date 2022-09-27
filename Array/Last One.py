T = int(input())
while(T>0):
    N = int(input())
    A = list(map(int, input().split()))[:N]
    for i in range(N-1,-1,-1):
        last = A[0]
        if(A[i]==1):
            last = A[i]
            last +=1
            print(i)
        else:
            print("-1")

    T = T-1
