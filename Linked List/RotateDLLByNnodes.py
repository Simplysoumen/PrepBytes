class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail  =None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def rotateNnode(self,N):
        temp=self.head
        count=0
        while(temp is not None and count is not N-1):
            temp = temp.next
            count +=1

        temp2 = temp.next
        if(temp2 is None):
            return
        temp.next=None
        temp2.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.head = temp2
        self.tail = temp

    def printDoublyLinkedList(self):
        temp=self.head
        while(temp is not None):
            # print(temp.prev, end=' ')
            print(temp.data, end=' ')
            # print(temp, end=' ')
            # print(temp.next)
            temp = temp.next

def main():
    t =int(input())
    while(t>0):
        doublyLinkedList = DoublyLinkedList()
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))

        for i in range(len(arr)):
            doublyLinkedList.insertAtEnd(arr[i])

        doublyLinkedList.rotateNnode(k)
        doublyLinkedList.printDoublyLinkedList()
        t=t-1

if __name__=='__main__':
    main()
