class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if (self.head is None):
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

    def LLR(self,temp):
        if(temp is None):
            return 0
        return 1+ self.LLR(temp.next)

    def deletionAtEnd(self):
        if(self.head is None):
            return
        elif(self.head.next is None):
            self.head=None
        else:
            sl = self.head
            while(sl.next.next is not None):
                sl = sl.next

            sl.tail = sl
            sl.next=None

    def deletionAtBeginning(self):
        if(self.head is None):
            return
        else:
            self.head = self.head.next

    def deletionatIthPosition(self,i):
        n = self.LLR(self.head)
        if(self.head is not None or i>n-1):
            return
        if(i==0):
            self.deletionAtBeginning()
            return
        if(i==n-1):
            self.deletionAtEnd()
            return

        count=0
        temp = self.head
        while(temp is not None and count is not (i-1)):
            count+=1
            temp = temp.next
        temp.next=temp.next.next

    def printSinglyLinkedList(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=' ')
            # print(temp, end=' ')
            # print(temp.next)
            temp = temp.next


def main():
    singlyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.insertAtEnd(arr[i])

    singlyLinkedList.deletionatIthPosition()
    singlyLinkedList.printSinglyLinkedList()


if __name__ == '__main__':
    main()
