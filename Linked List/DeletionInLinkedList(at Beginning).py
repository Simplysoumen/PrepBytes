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

    def deletionAtBeginning(self):
        if(self.head is None):
            return
        else:
            self.head = self.head.next

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

    singlyLinkedList.deletionAtBeginning()
    singlyLinkedList.printSinglyLinkedList()


if __name__ == '__main__':
    main()
