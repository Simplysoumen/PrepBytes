class Job:
    def __init__(self,id,deadline,profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def jobSequencing(jobArr):
    jobArr = sorted(jobArr, key = lambda job:job.profit, reverse=True)
    n =len(jobArr)
    slot = [False]*n
    result = [-1]*n
    for i in range(n):
        for j in range(min(n-1, jobArr[i].deadline-1),-1,-1):
            if(slot[j] is False):
                slot[j] = True
                result[j]=i
                break
    totalprofit = 0
    for i in range(n):
        if(slot[i] is True):
            print(jobArr[result[i]].id, end = ' ')
            totalprofit +=jobArr[result[i]].profit

    print(totalprofit)

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        jobArr = []
        for i in range(n):
            id,deadline,profit = map(int, input().split())
            jobArr.append(Job(id,deadline,profit))

        jobSequencing(jobArr)

        t = t-1

if __name__ == '__main__':
    main()
