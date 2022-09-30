def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())
        flag = 0
        for i in range(n):
            if(arr[i] == target):
                print("Target value is present at index",i)
                flag = 1
                break

        if(flag == 0):
            print("Target is not present")
        t = t-1

if __name__ == '__main__':
    main()
