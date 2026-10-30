# Undirected, Unweighted Graph
class Graph():
    def __init__(self):
        self.total_nodes = 0
        self.adjacency_list = dict()

    def addVertex(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
            self.total_nodes += 1

    def addEdge(self, node1, node2):
        # undirected
        if node2 not in self.adjacency_list[node1]:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)

    def showConnections(self):
        for item in self.adjacency_list.items():
            print(item)


