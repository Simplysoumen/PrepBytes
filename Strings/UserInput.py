# str = input()
# print(str)
#
# for i in range(len(str)):
#     print(str[i])
#
# for ele in str:
#     print(ele)


T = int(input())
while(T>0):
  N = int(input())
  A = list(map(int, input().split()))[:N]
  K = int(input())
  for i in range(N-1):
    for j in range(i + 1, N):
      if A[i] + A[j] == K:
        print(i,j)
  T = T-1





