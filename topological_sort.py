# Python program to print topological sorting of a DAG
from collections import defaultdict
 
# Class to represent a graph
 
 
class Graph:
    # def __init__(self, vertices):
    #     self.graph = defaultdict(list)  # dictionary containing adjacency List
    #     self.V = vertices  # No. of vertices

    def __init__(self):
        self.graph =  {'1': ['10'], '2': ['16'], '3': ['10', '11'], '6': ['11'], '7': ['19'], '22': [], '23': [], '10': ['22'], '11': ['16', '19'], '16': ['22', '23'], '19': ['23']}

        self.visited = {} 
        for i in self.graph.keys():
          self.visited[i] = False
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
 
        # Mark the current node as visited.
        visited[v] = True
        # print(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)
 
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        vis = self.visited
        for i in self.graph.keys():
            if vis[i] == False:
                self.topologicalSortUtil(i, vis, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
    def pri_g(self):
      print(self.graph)
      print(self.V)
 
# Driver Code
if __name__ == '__main__':
    g = Graph()
    # g.addEdge(5, 2)
    # g.addEdge(5, 0)
    # g.addEdge(4, 0)
    # g.addEdge(4, 1)
    # g.addEdge(2, 3)
    # g.addEdge(3, 1)
 
    print("Following is a Topological Sort of the given graph")
 
    # Function Call
    
    g.topologicalSort()
   



