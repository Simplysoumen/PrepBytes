class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            return
        self.tail.next = newNode
        self.tail = newNode
        self.tail.next = self.head
    def deletionAtEnd(self):
        if(self.head is None):
            print("Linked Lst is empty")
            return
        if(self.head.next is self.head):
            self.head = None
            self.tail = None
            return

        temp = self.head
        while(temp.next is not self.tail):
            temp = temp.next

        self.tail.next = None
        self.tail = temp
        self.tail.next = self.head

    def deletionAtBeginning(self):
        if (self.head is None):
            print("Linked Lst is empty")
            return
        if (self.head.next is self.head):
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.tail.next = self.head

    def printLL(self):
        temp=self.head
        while(True):
            print(temp, end=' ')
            print(temp.data,end=' ')
            print(temp.next)
            temp = temp.next
            if(temp == self.head):
                break
        print()

def main():
    circularLinkedList = CircularLinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        circularLinkedList.insertAtEnd(arr[i])

    circularLinkedList.deletionAtEnd()
    circularLinkedList.printLL()
    circularLinkedList.deletionAtBeginning()
    circularLinkedList.printLL()

if __name__ == '__main__':
    main()
