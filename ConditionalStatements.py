# a=5
# b=6
# if(a>b):
#     print(a,"is greater than",b)
# elif(b>a):
#     print(b,"is greater than",a)
# else:
#     print(a,"is equals to",b)
#a,b,c = map(int,input().split())
a = 1
b = 2
c = 3
if(a>b and a>c):
    print(a,"is the largest")
elif(b>a and b>c):
    print(b,"is the largest")
else:
    print(c,"is the largest")

X,Y = map(int, input().split())
if(X<Y):
  print(X, "is smaller than", Y)
elif(X>Y):
  print(X, "is greater than", Y)
else:
  print(X, "is equal to", Y)
