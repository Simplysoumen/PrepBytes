class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head=newNode

        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=newNode
    def printSinglyLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.data, end=' ')
            print(temp, end=' ')
            print(temp.next)
            temp=temp.next
    def lengthofLinkedList(self):
        temp=self.head
        count=0
        while(temp is not None):
            count +=1
            temp=temp.next
        return count

def main():
    singlyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.insertAtEnd(arr[i])

    print(singlyLinkedList.lengthofLinkedList())
    singlyLinkedList.printSinglyLinkedList()

if __name__ == '__main__':
    main()
