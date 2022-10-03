class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtBeginning(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head=newNode

        else:
            newNode.next = self.head
            self.head = newNode

    def printSinglyLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.data, end=' ')
            print(temp, end=' ')
            print(temp.next)
            temp=temp.next


def main():
    singlyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.insertAtBeginning(arr[i])

    singlyLinkedList.printSinglyLinkedList()

if __name__ == '__main__':
    main()
