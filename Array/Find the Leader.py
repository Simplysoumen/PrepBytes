T = int(input())
while(T>0):
    N = int(input())
    A = list(map(int,input().split()))[:N]
    leader = A[N-1]
    for i in range(N-1, -1, -1):
        if(A[i]==leader or A[i]>leader):
            leader = A[i]
            print(leader, end=' ')
    print()
    T = T-1

