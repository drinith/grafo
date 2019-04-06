class Node:
    def __init__(self, name):
        self.name = name
        self.adj  = list()
        self.visited = False
        self.checked = False

class Edge:
    def __init__(self, endNode, weight):
        self.endNode = endNode
        self.weight = weight

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
                                node.adj.append(Edge(node2, int(edge[2])))
        fileObj.close()

def pre_order(n:Node):
    global time
	print(n.name)
	n.visited = True
	for a in n.adj:
		if not a.endNode.visited:
			pre_order(a.endNode)
            time += a.endNode.weight

def post_order(n:Node):
    global time
	n.visited = True
	for a in n.adj:
		if not a.endNode.visited:
			post_order(a.endNode)
            time += a.endNode.weight
	print(n.name)

time = 0

graph = Graph()
graph.load_graph("/home/vinicius/Documentos/CEFET/Grafos/grafo/carga.txt")

#pre_order(graph.nodeList[0])
post_order(graph.nodeList[0])