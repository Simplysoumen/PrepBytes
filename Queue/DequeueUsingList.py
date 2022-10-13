class Dequeue():
    def __init__(self):
        self._dq = []

    def isEmpty(self):
        return self._dq==[]

    def insertRear(self, data):
        self._dq.append(data)

    def insertFront(self,data):
        self._dq.insert(0,data)

    def deleteRear(self):
        self._dq.pop()

    def deleteFront(self):
        self._dq.pop(0)

    def size(self):
        return len(self._dq)

    def frontEle(self):
        return self._dq[-0]

    def rearEle(self):
        return self._dq[-1]

    def printDeueue(self):
        for ele in self._dq:
            print(ele,end=" ")
        print()

def main():
    deque = Dequeue()
    deque.insertFront(5)
    deque.printDeueue()
    deque.insertFront(10)
    deque.printDeueue()
    deque.insertRear(1)
    deque.printDeueue()
    deque.insertRear(12)
    deque.printDeueue()

    deque.deleteRear()
    deque.printDeueue()
    deque.deleteFront()
    deque.printDeueue()

    print(deque.frontEle())
    print(deque.rearEle())
    print(deque.size())
    print(deque.isEmpty())

if __name__=='__main__':
    main()
