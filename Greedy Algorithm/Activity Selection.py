class Time:
    def __init__(self,st,end):
        self.start = st
        self.finish = end


def main():
    t = int(input())
    while(t != 0):
        n  =int(input())
        start = list(map(int, input().split()))
        finish = list(map(int, input().split()))
        arr = []
        for i in range(n):
            arr.append(Time(start[i],finish[i]))

        arr.sort(key=lambda item:(item.finish))
        selected = []
        i = 0
        selected.append(i)
        for j in range(1,n):
            if(arr[j].start >= arr[i].finish):
                selected.append(j)
                i = j
        for ele in selected:
            print(ele, end=" ")
        print()

        t = t-1

if __name__ == '__main__':
    main()
