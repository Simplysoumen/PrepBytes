class QueueUsingList:
    def __init__(self):
        self.que = []
        self.size = 0
        self.front = 0

    def enqueue(self,data):
        self.que.append(data)
        self.size+=1

    def isEmpty(self):
        return self.size==0

    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return

        temp = self.que[self.front]
        self.front +=1
        self.size -=1
        return temp

    def frontele(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return
        return self.que[self.front]

    def printQueue(self):
        if (self.isEmpty()):
            print("Queue is Empty")
            return

        for i in range(self.size):
            print(self.que[self.front + i],end=" ")
        print()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self,n):
        self.vertex = n
        self.graph = [None]*self.vertex

    def addEdge(self,u,v):
        newNode = Node(v)
        newNode.next = self.graph[u]
        self.graph[u] = newNode

    def edgePresent(self,u,v):
        temp = self.graph[u]
        while(temp is not None):
            if(temp.data == v):
                return True
            temp = temp.next
        return False

    def isPath(self,src,dest):
        visited =[False]*self.vertex
        qu = QueueUsingList()
        qu.enqueue(src)
        visited[src] = True
        while(qu.isEmpty() is False):
            node = qu.dequeue()
            if(node == dest):
                return True
            temp = self.graph[node]
            while temp:
                if(visited[temp.data]==False):
                    qu.enqueue(temp.data)
                    visited[temp.data] = True
                temp = temp.next
        return False

    def printGraph(self):
        for i in range(self.vertex):
            print("Adjacency list of vertex {} is = ".format(i),end='')
            temp = self.graph[i]
            while temp:
                print("->",temp.data, end = '')
                temp = temp.next
            print()

def main():
    n,e = map(int, input().split())
    gr = Graph(n)
    for i in range(e):
        u, v = map(int, input().split())
        gr.addEdge(u,v)

    src,dest = map(int, input().split())
    print(gr.isPath(src,dest))

if __name__ == '__main__':
    main()
