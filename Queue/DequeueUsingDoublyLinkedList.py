class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DequeueUsingDLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtFront(self,data):
        self.size+=1
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insertAtRear(self,data):
        newNode = Node(data)
        self.size+=1
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def deleteAtFront(self):
        if(self.head is None):
            return

        self.size-=1
        if(self.head.next is None):
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev.next = None
        self.head.prev = None

    def deleteAtEnd(self):
        if (self.head is None):
            return

        self.size -= 1
        if (self.head.next is None):
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next.prev = None
        self.tail.next = None

    def printDoublyLinkedList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp = temp.next
        print()

def main():
    dq = DequeueUsingDLL()
    dq.insertAtFront(5)
    dq.printDoublyLinkedList()
    dq.insertAtFront(10)
    dq.printDoublyLinkedList()
    dq.insertAtRear(1)
    dq.printDoublyLinkedList()
    dq.insertAtRear(12)
    dq.printDoublyLinkedList()
    dq.deleteAtEnd()
    dq.printDoublyLinkedList()
    dq.deleteAtFront()
    dq.printDoublyLinkedList()

if __name__ == '__main__':
    main()
