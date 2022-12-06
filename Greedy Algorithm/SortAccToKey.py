class Items:
    def __init__(self,fv,sv):
        self.first = fv
        self.second = sv
        self.total = fv + sv

    def __lt__(self,other):
        return self.total < other.total

def main():
    n = int(input())
    itemArr = []
    for i in range(n):
        fv,sv = map(int,input().split())
        itemArr.append(Items(fv,sv))
    itemArr.sort()
    # itemArr = sorted(itemArr, key = lambda item:item.total)
    for i in range(n):
        print("{} + {} = {}".format(itemArr[i].second,itemArr[i].total))

if __name__ == '__main__':
    main()
