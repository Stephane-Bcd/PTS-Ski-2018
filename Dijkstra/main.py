import CGraph
import ReadData
import time

#Allows to show the way, with the name of the piks :
def Show_the_peaks_for_the_path(name_peaks, shortest_path):
    print('Your shortest path is : ')
    for index in range(len(shortest_path)):
        print(name_peaks[shortest_path[index]])

# This fucntion allows to show the names fo the paths between the peaks
def Show_the_paths_between_the_peaks(array_paths, shortest_path, graph):

    print('Your have to use this paths : ')

    for index in range(len(shortest_path)):

        if((index + 1) < len(shortest_path)):

            # We need to incremente this 2 variables because there is a gap between our shortest path from Dijkstra and our file
            valueIncremente1 = int(shortest_path[index]) + 1
            valueIncremente2 = int(shortest_path[index + 1]) + 1

            # Then I use str() to convert into string
            path_between_peaks_from_shortest_path = str(valueIncremente1) + str(valueIncremente2)

            for index2 in range(len(array_paths)):

               line = array_paths[index2]

               # Then I use str() to convert into string
               path_between_peaks_from_array_file = str(line[2]) + str(line[3])

               if(path_between_peaks_from_shortest_path == path_between_peaks_from_array_file) :
                      print("Take this path : ", line[0], ", with this traject : ", line[1])

# Start to count the execution time
start_time = time.time()

#To save the name of the piks, [] for lists
name_peaks = []
#To save the data of the paths, {} for dictionnarys
name_paths = {}

#To check the data inside the file, and create the matrix with the right size
graph = ReadData.Create_Adjacency_Matrix(name_peaks, name_paths)

print(name_paths)

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

#If you want display the graph :
#print (graph)

#If you want show the way, with the name of the peaks :
Show_the_peaks_for_the_path(name_peaks, shortest_path)

#If you want show the name of the path between the peaks :
Show_the_paths_between_the_peaks(name_paths, shortest_path, graph)

# If you want display the execution time :
print("Execution time : %s secondes ---" % (time.time() - start_time))