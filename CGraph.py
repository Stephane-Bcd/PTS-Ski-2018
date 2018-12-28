
# Python program for Dijkstra's single source shortest path algorithm.
# The program is for adjacency matrix representation of the graph

# Class to represent a graph
from typing import List, Any


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)
        self.col = len(graph[0])

    # A utility function to find the
    # vertex with minimum dist value, from
    # the set of vertices still in queue
    def minDistance(self, queue):
        # Initialize min value and min_index as -1
        minimum = float("Inf")
        min_index = -1

        # from the dist array,pick one which
        # has min value and is till in queue
        for i in range(len(self.dist)):
            if self.dist[i] < minimum and i in queue:
                minimum = self.dist[i]
                min_index = i
        return min_index

        # Function to print shortest path

    # from source to j
    # using parent array
    def printPath(self, j):

        # Base Case : If j is source
        if self.parent[j] == -1:
            print (j),
            return
        self.printPath(self.parent[j])
        print (j),

        # A utility function to print

    # the constructed distance
    # array
    def printSolution(self, src):
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(self.dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, self.dist[i])),
            self.printPath(i)

    '''Function that implements Dijkstra's single source shortest path 
    algorithm for a graph represented using adjacency matrix 
    representation'''

    def dijkstra(self, src):

        # The output array. dist[i] will hold
        # the shortest distance from src to i
        # Initialize all distances as INFINITE
        self.dist = [float("Inf")] * self.row

        # Parent array to store
        # shortest path tree
        self.parent = [-1] * self.row

        # Distance of source vertex
        # from itself is always 0
        self.dist[src] = 0

        # Add all vertices in queue
        queue = []
        for i in range(self.row):
            queue.append(i)

            # Find shortest path for all vertices
        while queue:

            # Pick the minimum dist vertex
            # from the set of vertices
            # still in queue
            u = self.minDistance(queue)

            # remove min element
            queue.remove(u)

            # Update dist value and parent
            # index of the adjacent vertices of
            # the picked vertex. Consider only
            # those vertices which are still in
            # queue
            for i in range(self.col):
                '''Update dist[i] only if it is in queue, there is 
                an edge from u to i, and total weight of path from 
                src to i through u is smaller than current value of 
                dist[i]'''
                if self.graph[u][i] and i in queue:
                    if self.dist[u] + self.graph[u][i] < self.dist[i]:
                        self.dist[i] = self.dist[u] + self.graph[u][i]
                        self.parent[i] = u

                        # print the constructed distance array
        self.printSolution(src)

    def get_shortest_path(self, goal):
        # Base Case : If j is source
        path = []
        if self.parent[goal] == -1:
            path.__add__(goal)
            return path
        self.get_shortest_path(self.parent[goal])
        path.__add__(goal)

    def get_shortest_distance(self, goal):
        return self.dist[goal]

