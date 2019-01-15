import CGraph
import CReadData
import time
import CDisplayData


# Start to count the execution time
start_time = time.time()

#To save the name of the piks, [] for lists
name_peaks = []
#To save the data of the paths, {} for dictionnarys
name_paths = {}

#To check the data inside the file, and create the matrix with the right size
graph = CReadData.Create_Adjacency_Matrix(name_peaks, name_paths)

print(name_paths)

#To fill the matrix with our ski data
CReadData.Fill_Adjacency_Matrix(graph)

g = CGraph.Graph(graph)

# the value for the Dijkstra function below is the strating point
g.dijkstra(0)

shortest_distance = g.get_shortest_distance(36)
print('shortest distance : ')
print(shortest_distance)

# we create a list "shortest_path"
shortest_path = []
# method to get the shortest path to a node
g.get_shortest_path(36, shortest_path)
print('shortest path : ')
# we display the list "shortest_path"
print(shortest_path)

#If you want display the graph :
#print (graph)

#If you want show the way, with the name of the peaks :
CDisplayData.Show_the_peaks_for_the_path(name_peaks, shortest_path)

#If you want show the name of the path between the peaks :
CDisplayData.Show_the_paths_between_the_peaks(name_paths, shortest_path, graph)

# If you want display the execution time :
print("Execution time : %s secondes ---" % (time.time() - start_time))