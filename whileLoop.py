# # i = 5
# # n = 50
# # while(i<=n):
# #     print(i)
# #     i+=1
# i = 1
# n = 100
# while(i<=n):
#     if(i==11):
#         i+=2
#         continue
#     print(i,end="")
#     i+=2
#     print()
#     print("Loop ended")

#Printing first digit:
n = int(input())
rem = 0
while(n>0):
    rem=n%10
    n=n//10
print(rem)

