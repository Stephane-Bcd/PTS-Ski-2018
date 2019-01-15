#Allows to show the way, with the name of the piks :
def Show_the_peaks_for_the_path(name_peaks, shortest_path):
    print('Your shortest path is : ')
    for index in range(len(shortest_path)):
        print(name_peaks[shortest_path[index]])

# This function allows to show the names fo the paths between the peaks
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