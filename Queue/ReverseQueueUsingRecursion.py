class QueueUsingList:
    def __init__(self):
        self.que = []
        self.size = 0
        self.front = 0

    def enqueue(self,data):
        self.que.append(data)
        self.size+=1

    def isEmpty(self):
        return self.size==0

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return

        temp = self.que[self.front]
        self.front +=1
        self.size -=1
        return temp

    def frontele(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return
        return self.que[self.front]

    def printQueue(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return

        for i in range(self.size):
            print(self.que[self.front + i],end=" ")
        print()



def reverse(que):

    if(que.isEmpty()):
        return

    temp = que.dequeue()

    reverse(que)

    que.enqueue(temp)

def main():
    que = QueueUsingList()

    for ele in input().split():
        que.enqueue(int(ele))

    reverse(que)
    que.printQueue()

if __name__ == '__main__':
    main()
