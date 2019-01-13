import CGraph
import ReadData
import time

#Allows to show the way, with the name of the piks :
def Show_the_way(name_piks, shortest_path):
    print('Your shortest path is : ')
    for index in range(len(shortest_path)):
        print(name_piks[shortest_path[index]])

# Start to count the execution time
start_time = time.time()

#To save the name of the piks
name_piks = []

#To check the data inside the file, and create the matrix with the right size
graph = ReadData.Create_Adjacency_Matrix(name_piks)

print(name_piks)

#To fill the matrix with our ski data
ReadData.Fill_Adjacency_Matrix(graph)

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

# If you want display the execution time :
#print("Execution time : %s secondes ---" % (time.time() - start_time))

#If you want display the graph :
#print (graph)

#If you want show the way, with the name of the piks :
Show_the_way(name_piks, shortest_path)