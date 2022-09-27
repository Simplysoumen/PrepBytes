M,N,K = map(int, input().split())

mat1 = []
for i in range(M):
    mat1.append(list(map(int, input().split())))


mat2 = []
for i in range(M):
    mat2.append([0] * N)

for i in range(M):
    for j in range(N):
        mat2[i][j]=mat1[i][j]*K

for i in range(M):
    for j in range(N):
        print(mat2[i][j],end=' ')
    print()
