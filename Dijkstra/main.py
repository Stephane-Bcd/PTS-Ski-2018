import CGraph
import ReadData
import time

# Start to count the execution time
start_time = time.time()

#To check the data inside the file, and create the matrix with the right size
graph = ReadData.Create_Adjacency_Matrix()

#To fill the matrix with our ski data
ReadData.Fill_Adjacency_Matrix(graph)

g = CGraph.Graph(graph)
# Print the solution of Dijkstra
g.dijkstra(0)

shortest_distance = g.get_shortest_distance(1)
print('shortest distance : ')
print(shortest_distance)

# we create a list "shortest_path"
shortest_path = []
# method to get the shortest path to a node
g.get_shortest_path(36, shortest_path)
print('shortest path : ')
# we display the list "shortest_path"
print(shortest_path)

# Display the execution time
print("Execution time : %s secondes ---" % (time.time() - start_time))

print (graph)