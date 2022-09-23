def getLeapYear(year):
    if year % 4==0:
        if year % 100==0:
            if year % 400==0:
                print("Yes")
            else:
                print("No")
        else:
             print("Yes")

    else:
        print("No")

# for _ in range(int(input())):
#     getLeapYear(int(input()))

T = int(input())
while (T > 0):
    getLeapYear(int(input()))
    T = T - 1
