n = int(input())
count = 0
while(n>0):
    t,c = map(int, input().split())
    if(c-t >=2):
        count +=1
    n=n-1
print(count)
