"""
            BFS for Graphs - Using Dictionary
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,source,neighbor):
        self.graph[source].append(neighbor)


    def BFS(self,source):

        visited = set()
        queue = []

        queue.append(source)
        visited.add(source)

        while queue:

            node = queue.pop(0)
            print(node)

            for vertice in self.graph[node]:
                if vertice not in visited:
                    queue.append(vertice)
                    visited.add(vertice)





    def __str__(self):
        string = ""
        for node,vertices in self.graph.items():
            string += " " + str(node) + " : " + str(vertices) + "\n"

        return string


g = Graph()
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(1,2)
g.addEdge(3,3)
g.addEdge(0,2)
g.addEdge(0,1)
# print(g)
g.BFS(2)