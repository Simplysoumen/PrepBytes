class Product:
    def __init__(self,wt,profit,index):
        self.wt = wt
        self.profit = profit
        self.index = index
        self.pw = profit/wt

    def __lt__(self,other):
        return self.pw < other.pw

def fractionalKnapsack(wt,profit,cap):
    ratio = []
    flag = 0
    for i in range(len(wt)):
        ratio.append(Product(wt[i],profit[i],i))

    ratio.sort(reverse = True)

    totalProfit = 0
    i = 0
    for i in range(len(ratio)):
        currWt = int(ratio[i].wt)
        currPro = int(ratio[i].profit)
        if(cap>0 and currWt<=cap):
            cap = cap-currWt
            totalProfit += currPro
        else:
            flag = 1
            break
    if(flag == 1):
        totalProfit += ratio[i].profit*(cap/ratio[i].wt)

    print(int(totalProfit))

def main():
    n, cap = map(int, input().split())
    wt = list(map(int, input().split()))
    profit = list(map(int, input().split()))
    fractionalKnapsack(wt,profit,cap)

if __name__ == '__main__':
    main()
