class Stack:
    def __init__(self):
        self.arr = []
        self.tos = -1

    def push(self,data):
        self.tos +=1
        self.arr.append(data)

    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        self.tos = self.tos-1
        self.arr.pop()

    def size(self):
        return self.tos+1

    def isEmpty(self):
        return self.tos==-1

    def top(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        return self.arr[self.tos]

class QueueUsingStack:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        self.size=0

    def enqueue(self,data):
        self.s1.push(data)
        self.size+=1

    def dequeue(self):
        if(self.s1.isEmpty() and self.s2.isEmpty()):
            print("Queue Underflow")

        if(self.s2.isEmpty()):
            while(self.s1.isEmpty() is False):
                self.s2.push(self.s1.top())
                self.s1.pop()

        data = self.s2.top()
        self.s2.pop()
        self.size -=1
        return data

    def isEmpty(self):
        return self.size==0


def main():
    que = QueueUsingStack()
    for ele in input().split():
        que.enqueue(int(ele))

    while(que.isEmpty() is False):
        print(que.dequeue(), end=" ")

if __name__ == '__main__':
    main()
