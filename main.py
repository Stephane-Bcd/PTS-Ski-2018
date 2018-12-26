import CGraph
import ReadData

#We can define here the size of the graph (number of peaks)
numberRows = 37
numberColumns = 37

#To create the matrix for our data :
# Here I initialize the matrix with 0
graph = [0] * numberRows
for i in range(numberRows):
    graph[i] = [0] * numberColumns

#To read the data and fill our matrix
error = ReadData.getDataFile(graph)

if(error == -1):
    print("Error : impossible to read the data in the file ! ")

else:
    g = CGraph.Graph()
    # Print the solution of Dijkstra
    g.dijkstra(graph, 0)
