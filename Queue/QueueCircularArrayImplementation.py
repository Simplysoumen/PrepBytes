class QueueUsingCircularArray:
    def __init__(self,capacity):
        self.que=[None]*capacity
        self.front = -1
        self.rear = -1
        self.size = 0
        self.cap = capacity

    def isEmpty(self):
        return self.front == -1

    def enqueue(self,data):
        #Queue full
        if((self.rear+1)%self.cap == self.front):
            print("Queue is Full")
            return

        #Queue Empty
        if(self.isEmpty()):
            self.front = self.rear = 0
            self.que[self.rear] = data
            self.size +=1
            return

        self.rear = (self.rear+1)%self.cap
        self.que[self.rear] = data
        self.size +=1

    def dequeue(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return -1

        # Que element in the queue
        if(self.rear==self.front):
            temp=self.que[self.front]
            self.front=self.rear = -1
            return temp

        temp=self.que[self.front]
        self.front = (self.front+1)%self.cap
        self.size-=1
        return temp

    def frontele(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return -1
        return self.que[self.front]

    def printQueue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return

        for i in range(self.size):
            print(self.que[(self.front+i)%self.cap], end=" ")
        print()


def main():
    cap = int(input())
    que = QueueUsingCircularArray(cap)
    for ele in input().split():
        que.enqueue(int(ele))

    que.printQueue()
    que.dequeue()
    que.printQueue()
    que.dequeue()
    que.printQueue()
    que.dequeue()
    que.enqueue(100)
    que.enqueue(200)
    que.printQueue()

if __name__ == '__main__':
    main()
