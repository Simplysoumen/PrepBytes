t=int(input())
while(t>0):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = [0]*40
    for i in range(n):
        freq[arr[i]]+=1

    # for i in range(40):
    #     if(freq[i]>0):
    #         print(i,freq[i])

    flag=0
    for i in range(40):
        if (freq[i]>1):
            flag=1
            break

    if (flag==1):
        print("Elements are not Unique")
    else:
        print("Elements are unique")
    t=t-1
