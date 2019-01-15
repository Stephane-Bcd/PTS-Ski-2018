#If you have an error with "import numpy as np", it is because you need to install this library
#If you use Pycharm there is a easy way : File -> Settings -> Project : 'name project' -> project interpreter -> '+' -> select the nyumpy library
import numpy as np
import CComputeData

# Class to represent a graph


# This function check the number of data int the file, and create a adjacency matrix with the right size for the graph
# name_piks : output parameter
# name_piks : output parameter
def Create_Adjacency_Matrix(name_peaks, name_paths):
    # This variable "paths_and_occurences" contains all the paths and their occurrences, we use it to know the size of the third dimension
    paths_and_occurences = []

    # index to know if actual data is point or path
    input_data_type_index = 0

    # count of points and paths that we are supposed to have (count got from the input file)
    input_data_supposed_points_count = 0
    input_data_supposed_paths_count = 0

    # count of points and paths that we observe using lines (count got from the input files lines)
    input_data_observed_points_count = 0
    input_data_observed_paths_count = 0

    # boolean to know if first element
    first_iteration_on_file = True

    try:
        # You can choose the path of your file here :
        fp = open('./data_arcs.txt', 'r')
        lines = fp.readlines()
        for line in lines:
            line = line.strip().replace("\n", "").split("\t")

            # if current line is count of following informations
            if line.__len__() == 1:

                if not first_iteration_on_file:
                    input_data_type_index += 1
                first_iteration_on_file = False

                if input_data_type_index == 0:  # for points
                    input_data_supposed_points_count = int(line[0])

                elif input_data_type_index == 1:  # for paths
                    input_data_supposed_paths_count = int(line[0])
                else:
                    break

            # If current line is normal data line
            else:

                if input_data_type_index == 0:  # for points
                    print("Point: " + str(line))
                    input_data_observed_points_count += 1
                    name_peaks.append(line[1])
                elif input_data_type_index == 1:  # for paths
                    print("Path: " + str(line))
                    value = line[3] + line[4]
                    paths_and_occurences.append(value)
                    name_paths[input_data_observed_paths_count] = (line[1], line[2], line[3], line[4])
                    input_data_observed_paths_count += 1

        print("Supposed points count: " + str(input_data_supposed_points_count))
        print("Observed points count: " + str(input_data_observed_points_count))
        print("Supposed paths count: " + str(input_data_supposed_paths_count))
        print("Observed paths count: " + str(input_data_observed_paths_count))
        fp.close()

        # we create the matrix only if the data are correct :
        if input_data_supposed_points_count == input_data_observed_points_count and input_data_supposed_paths_count == input_data_observed_paths_count:

            # Allows to know the size of the third dimension before to create it
            size_third_dimension = CComputeData.Find_the_biggest_occurence(paths_and_occurences, int(input_data_supposed_paths_count))

            # To create the matrix for our data, the matrix is initialized with 0
            graph = np.zeros(input_data_observed_points_count * input_data_observed_points_count * size_third_dimension)
            graph.resize((input_data_observed_points_count, input_data_observed_points_count, size_third_dimension))
            # We can return the matrix to the main
            return graph
        else:
            print('Error : The specified text file contains inaccurate information ')

    except FileNotFoundError as e:
        print(e)


# This function will fill a adjacency matrix with the data from a file
# graph : input parameter
def Fill_Adjacency_Matrix(graph):
    # This variable "peaks" contains all the peaks of our graph
    peaks = {}
    # index to know if actual data is point or path
    input_data_type_index = 0

    # count of points and paths that we observe using lines (count got from the input files lines)
    input_data_observed_points_count = 0
    input_data_observed_paths_count = 0

    # boolean to know if first element
    first_iteration_on_file = True

    try:
        # You can choose the path of your file here :
        fp = open('./data_arcs.txt', 'r')
        lines = fp.readlines()
        for line in lines:
            line = line.strip().replace("\n", "").split("\t")

            # if current line is count of following informations
            if line.__len__() == 1:

                if not first_iteration_on_file:
                    input_data_type_index += 1
                first_iteration_on_file = False

            # If current line is normal data line
            else:

                if input_data_type_index == 0:  # for points
                    input_data_observed_points_count += 1
                    # code to add to the dictionnary
                    peaks[input_data_observed_points_count] = (line[0], line[1], line[2])

                elif input_data_type_index == 1:  # for paths

                    # To get the line with the informations(like peak height) about the current peak, it is the peak source
                    lineFromPeakA = peaks[int(line[3])]
                    # To get the height in the line about the second the current peak, it is the peak source
                    weightPeakA = int(lineFromPeakA[2])
                    # To get the line with the informations(like peak height) about the current peak, it is the peak destination
                    lineFromPeakB = peaks[int(line[4])]
                    # To get the height in the line about the second  current peak, it is the peak destination
                    weightPeakB = int(lineFromPeakB[2])

                    # I initialized the variable 'condition' to true to simulate a loop 'Do while' instead a loop 'while'
                    condition = True
                    indice = 0

                    # this loop while allows to add the parallel paths,
                    while condition:

                        # If the value in the array is 0 -> there is no path, so we can put the value
                        if graph[int(line[3]) - 1][int(line[4]) - 1][indice] == 0:
                            # compute_weight() : function to compute the weight of the vertices and return it (in secondes)
                            graph[int(line[3]) - 1][int(line[4]) - 1][indice] = CComputeData.compute_weight(line[2], abs(
                                weightPeakA - weightPeakB), line[1])
                            condition = False
                        # If there is a path, we have to use the third dimension of the array, so we increment the value
                        else:
                            indice = indice + 1
        fp.close()

    except FileNotFoundError as e:
        print(e)

