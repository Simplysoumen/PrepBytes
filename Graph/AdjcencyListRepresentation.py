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

        newNode = Node(u)
        newNode.next = self.graph[v]
        self.graph[v] = newNode

    def edgePresent(self,u,v):
        temp = self.graph[u]
        while(temp is not None):
            if(temp.data == v):
                return True
            temp = temp.next
        return False

    def edgeRemove(self,u,v):
        if(self.edgePresent(u,v)):
            temp = self.graph[u]


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

    gr.printGraph()
    x,y = map(int, input().split())
    print(gr.edgePresent(x,y))

if __name__ == '__main__':
    main()

