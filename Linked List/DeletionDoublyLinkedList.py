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

    def deletionFromEnd(self):
        if(self.head is None):
            print("Linked List is Empty")
            return
        temp=self.tail.prev
        temp.next=None
        self.tail.prev = None
        self.tail=temp

    def deletionFromBeginning(self):
        if (self.head is None):
            print("Linked List is Empty")
            return
        temp = self.head.next
        if(temp is None):
            self.head=None
            return

        self.head.next = None
        temp.prev = None
        self.head = temp

    def deleteFromGivenPosition(self,i):
        n = self.lengthofLinkedList()
        if(i>=n):
            print("Invalid Position")
            return
        if(i==0):
            self.deletionFromBeginning()
            return
        if(i==n-1):
            self.deletionFromEnd()
            return
        count=0
        temp=self.head
        while(temp.next is not None and count is not i):
            count +=1
            temp = temp.next

        temp1 = temp.prev
        temp2 = temp.next
        temp.prev = None
        temp.next = None
        temp1.next = temp2
        temp2.prev = temp1

    def printDoublyLinkedList(self):
        temp=self.head
        while(temp is not None):
            # print(temp.prev, end=' ')
            print(temp.data, end=' ')
            # print(temp, end=' ')
            # print(temp.next)
            temp = temp.next
        print()

    def lengthofLinkedList(self):
        temp=self.head
        count=0
        while(temp is not None):
            count +=1
            temp=temp.next

        return count

def main():
    doublyLinkedList = DoublyLinkedList()
    arr = list(map(int, input().split()))

    for i in range(len(arr)):
        doublyLinkedList.insertAtEnd(arr[i])

    doublyLinkedList.deleteFromGivenPosition(3)
    doublyLinkedList.printDoublyLinkedList()
    doublyLinkedList.deleteFromGivenPosition(0)
    doublyLinkedList.printDoublyLinkedList()
    doublyLinkedList.deleteFromGivenPosition(doublyLinkedList.lengthofLinkedList()-1)
    doublyLinkedList.printDoublyLinkedList()
    # doublyLinkedList.deletionFromBeginning()
    # doublyLinkedList.printDoublyLinkedList()

if __name__=='__main__':
    main()
