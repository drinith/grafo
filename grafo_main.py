class Node:
    def __init__(self, name):
        self.name     = name
        self.edgeList = list()
        self.visited  = False
        self.checked  = False

class Edge:
    def __init__(self, endNode, weight):
        self.endNode = endNode
        self.weight  = weight

class Graph:
    def __init__(self):
        self.nodeList = list()

    def load_graph(self,path):
        fileObj  = open(path, 'r')
        text     = fileObj.readlines()
        readNode = False
        readEdge = False
        
        for line in text:
            if line == 'Vertices\n':
                readNode = True
                readEdge = False
                continue
            if line == 'Ligacoes\n':
                readNode = False
                readEdge = True
                continue

            if readNode:
                self.nodeList.append(Node(line.replace('\n','')))
            if readEdge:
                edge = line.replace('\n','').split(" ")
                for node in self.nodeList:
                    if edge[0] == node.name:
                        for node2 in self.nodeList:
                            if edge[1] == node2.name:
                                node.edgeList.append(Edge(node2, int(edge[2])))
        fileObj.close()

def pre_order(n:Node):
    global time
    print(n.name)
    n.visited = True
    for a in n.edgeList:
        if not a.endNode.visited:
            pre_order(a.endNode)
            time += a.weight

def post_order(n:Node):
    global time
    n.visited = True
    for a in n.edgeList:
        if not a.endNode.visited:
            post_order(a.endNode)
            time += a.weight
    print(n.name)

def breadth_first_search(q:list):
    global time
    while(q):
        node = q.pop(0)
        if not node.visited:
            print(node.name)
            node.visited = True
            for a in node.edgeList:
                if not a.endNode.checked:
                    q.append(a.endNode)
                    time             += a.weight
                    a.endNode.checked = True

def bellman_ford(graph:Graph, source:Node):
    dist = dict()
    prev = dict()

    for node in graph.nodeList:
        dist[node] = float("inf")
        prev[node] = None
    
    dist[source] = 0
    
    for i in range(0, len(graph.nodeList) - 1):
        node = graph.nodeList[i]
        for edge in node.edgeList:
            if (dist[edge.endNode] > dist[node] + edge.weight):
                dist[edge.endNode] = dist[node] + edge.weight
                prev[edge.endNode] = node
        
    for node in graph.nodeList:
        pass

'''def dijkstra(graph:Graph, source:Node):
    queue = list()
    dist     = dict()
    prev     = dict()

    for node in graph.nodeList:
        dist[node] = float("inf")
        prev[node] = None
        queue.append(node)

    dist[source] = 0

    while(queue):
        u = '''

time = 0

graph = Graph()
graph.load_graph("/home/vinicius/Documentos/CEFET/Grafos/grafo/carga.txt")

#pre_order(graph.nodeList[0])
#post_order(graph.nodeList[0])
#q = [graph.nodeList[0]]
#breadth_first_search(q)
bellman_ford(graph, graph.nodeList[0])

#print(time)