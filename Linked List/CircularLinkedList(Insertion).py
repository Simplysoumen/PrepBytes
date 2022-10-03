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

    def insertAtBeginning(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            return
        newNode.next = self.head
        self.head = newNode
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
    circularLinkedList2 = CircularLinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        circularLinkedList.insertAtEnd(arr[i])
        circularLinkedList2.insertAtBeginning(arr[i])
    circularLinkedList.printLL()
    print()
    circularLinkedList2.printLL()

if __name__ == '__main__':
    main()
