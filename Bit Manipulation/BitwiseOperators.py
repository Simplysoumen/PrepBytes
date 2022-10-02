# a=5
# b=7
# print(a&b)
# print(a|b)
# print(~a)
# print(~b)
#
# print(~-4)
#
# print(a<<2)
# print(b>>2)

n,k = map(int,input().split())
#Set the Kth  bit:
n = n | (1<<k)
print(n)

#Unset the Kth bit:
n = n & ~(1<<k)
print(n)

#Toggle
n = n ^(1<<k)
print(n)

#To check whether the bit is set or not
if(n &(1<<k)!=0):
    print("Kth bit is set")
else:
    print("Kth bit is unset")
