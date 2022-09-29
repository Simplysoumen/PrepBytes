def removeAdjDup(str):
    if(len(str)==1):
        return str
    if(str[0]==str[1]):
        return removeAdjDup(str[1:])
    return str[0] + removeAdjDup(str[1:])

str = input()
print(removeAdjDup(str))
