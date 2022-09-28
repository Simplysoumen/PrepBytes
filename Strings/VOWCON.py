# T = int(input())
# while(T!=0):
#     S = input()
#     vowel = 0
#     consonant = 0
#     for i in S:
#         if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             vowel=vowel+1
#         else:
#             consonant=consonant+1
#
#     print(vowel,consonant)
#     T=T-1


T = int(input())
while(T>0):
    n=int(input())
    S = input()
    for i in range(n):
        for j in range(i+1):
            print(S[j], end='')
        print()
    for i in range(n):
        n = n-1
        print(S[n])

    T = T-1
