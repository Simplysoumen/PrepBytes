class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail  =None

    def insertAtBeginning(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            return

        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def insertAtGivenPosition(self,i,data):
        newNode = Node(data)
        n = self.lengthofLinkedList()
        if(i==0):
            self.insertAtBeginning(data)
            return
        if(i==n):
            self.insertAtEnd(data)
            return
        if(i>n):
            print("Invalid Position")
            return
        count=0
        temp=self.head
        while(temp.next is not None and count is not (i-1)):
            count+=1
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode

    def printDoublyLinkedList(self):
        temp = self.head
        while (temp is not None):
            # print(temp.prev, end=' ')
            print(temp.data, end=' ')
            # print(temp, end=' ')
            # print(temp.next)
            temp = temp.next

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
        doublyLinkedList.insertAtBeginning(arr[i])
    doublyLinkedList.insertAtGivenPosition(3,100)
    doublyLinkedList.printDoublyLinkedList()

if __name__=='__main__':
    main()
