T = int(input())
while(T>0):
    N = int(input())
    A = list(map(int, input().split()))
    max_dif = A[1]-A[0]
    index_dif=0
    for i in range(N):
        for j in range(i+1,N):
            if(A[j]-A[i]>max_dif and A[j]>A[i] and j > i):
                max_dif = A[j]-A[i]
                index_dif=j-i
    if(max_dif == 0):
        print("-1")
    else:
        print(index_dif)
    T=T-1
