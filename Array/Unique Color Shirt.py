def getUnique(arr):
    resDict = {}
    for ele in arr:
        if ele in resDict:
            resDict[ele] +=1
        else:
            resDict[ele] = 1

    print(len([ele for ele in resDict if resDict[ele]==1]))

count = input()
arr = [int(ele) for ele in input().split(" ")]
getUnique(arr)
