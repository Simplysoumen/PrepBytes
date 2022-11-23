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

class Graph:
    def __init__(self, n):
        self.vertex = n
        self.adjMat = []
        for i in range(self.vertex):
            self.adjMat.append([0]*self.vertex)

    def addEdge(self,u,v):
        self.adjMat[u][v] = 1
        self.adjMat[v][u] = 1

    def edgePresent(self,u,v):
        if(self.adjMat[u][v]==1):
            return True
        else:
            return False

    def removeEdge(self,u,v):
        if(self.edgePresent(u,v)):
            self.adjMat[u][v] = 0
            self.adjMat[v][u] = 0

    def isCyclicConnected(self,v,visited):
        qu = QueueUsingList()
        qu.enqueue(v)
        visited[v] = True
        parent = [-1]*self.vertex
        while(qu.isEmpty() is False):
            node = qu.dequeue()
            for i in range(self.vertex):
                if(self.adjMat[node][i]==1):
                    if(visited[i] == False):
                        qu.enqueue(i)
                        visited[i] = True
                        parent[i] = node

                    elif(parent[node] != i):
                        return True
        return False

    def printMat(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.adjMat[i][j],end=' ')
            print()

def main():
    n,e = map(int, input().split())
    graph = Graph(n)
    for i in range(e):
        u,v = map(int, input().split())
        graph.addEdge(u,v)

    visited = [False]*graph.vertex
    flag = 0
    for i in range(graph.vertex):
        if(visited[i] is False and graph.isCyclicConnected(i,visited)):
            flag = 1
            break
    if(flag == 1):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
