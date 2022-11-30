import heapq
import sys
class Node:
    def __init__(self,v,weight):
        self.data = v
        self.wt = weight
        self.next = None

class Graph:
    def __init__(self,n):
        self.vertex = n
        self.ans = 0
        self.graph = [None]*self.vertex

    def addEdge(self,u,v,w):
        newNode = Node(v,w)
        newNode.next = self.graph[u]
        self.graph[u] = newNode

        newNode = Node(u,w)
        newNode.next  =self.graph[v]
        self.graph[v] = newNode

    def lengthofLinkedList(self, head):
        temp = head
        count = 0
        while(temp is not None):
            count +=1
            temp = temp.next

        return count

    def printGraph(self):
        for i in range(self.vertex):
            temp = self.graph[i]
            while temp:
                print("Weifght of edge from {} to {} = {}".format(i.temp.data,temp.wt))
                temp = temp.next
            print()

    def dijkstra(self,u):
        vertices = self.vertex
        dist = [sys.maxsize]*vertices
        dist[u] = 0
        heap = [(0,u)]
        visited = [False]*vertices
        while(heap):
            wt,v = heapq.heappop(heap)
            if(visited[v] is True):
                continue
            else:
                visited[v] = True
                temp = self.graph[v]
                while(temp):
                    if(visited[temp.data] is True):
                        temp = temp.next
                        continue
                    if(dist[temp.data]>dist[v]+temp.wt):
                        dist[temp.data] = dist[v]+temp.wt
                        heapq.heappush(heap, (dist[v]+temp.wt, temp.data))
                    temp = temp.next
        for i in range(vertices):
            print("Shortest distance from {} to {} is {}".format(u,i,dist[i]))

def main():
    n,e = map(int, input().split())
    gr = Graph(n)
    for i in range(e):
        u,v,w = map(int, input().split())
        gr.addEdge(u,v,w)

    gr.dijkstra(0)

if __name__ == '__main__':
    main()
