def getReverse(num):
    res = 0
    while num:
        remainder = num%10
        num = num//10
        res = res*10 + remainder

    return res

print(getReverse(int(input())))
