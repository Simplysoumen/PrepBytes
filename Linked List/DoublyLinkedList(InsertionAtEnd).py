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

    def printDoublyLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.prev, end=' ')
            print(temp.data, end=' ')
            print(temp, end=' ')
            print(temp.next)
            temp = temp.next

def main():
    doublyLinkedList = DoublyLinkedList()
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        doublyLinkedList.insertAtEnd(arr[i])
    doublyLinkedList.printDoublyLinkedList()

if __name__=='__main__':
    main()
