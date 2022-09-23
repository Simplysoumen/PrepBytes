arr = []
for ele in input().split():
    arr.append(int(ele))

for i in range(len(arr)):
    print(arr[i], end=' ')


arr1 = list(map(int, input().split()))
for i in range(len(arr)):
    print(arr[i],end=' ')
