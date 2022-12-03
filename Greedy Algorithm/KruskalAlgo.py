class Edge:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self,other):
        return self.w < other.w

class Graph:
    def __init__(self,n):
        self.vertex = n
        self.edgeList = []

    def addEdge(self,u,v,w):
        self.edgeList.append(Edge(u,v,w))

    def getSet(self,node,vertexList):
        if(node==vertexList[node]):
            return node
        return self.getSet(vertexList[node],vertexList)
    def kruskalAlgo(self):
        vertexSet = [-1]*self.vertex
        for i in range(self.vertex):
            vertexSet[i] = i

        self.edgeList.sort()
        count = 0
        i = 0
        result = []
        while(count<self.vertex-1):
            currEd = self.edgeList[i]
            uset = self.getSet(currEd.u, vertexSet)
            vset = self.getSet(currEd.v, vertexSet)
            if(uset != vset):
                result.append(currEd)
                count +=1
                vertexSet[vset] = uset
            i +=1
        for i in range(len(result)):
            print("{} {}".format(result[i].u,result[i].v))


def main():
    n,e = map(int, input().split())
    graph = Graph(n)
    for i in range(e):
        u,v,w = map(int, input().split())
        graph.addEdge(u,v,w)
    graph.kruskalAlgo()

if __name__ == '__main__':
    main()
