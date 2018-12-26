import Compute

def getDataFile(graph):

    #The function will return this variable "error", to know if it working properly :
    error = 1;
    # This variable "peaks" contains all the peaks of our graph
    peaks = {}
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
        #You can choose the path of your file here :
        fp = open('./data_arcs.txt', 'r')
        error = 1
        lines = fp.readlines()
        for line in lines:
            line = line.strip().replace("\n", "").split("\t")

            # if current line is count of following informations
            if line.__len__() == 1:
                print("---------------------------------")

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
                    # code to add to the dictionnary
                    peaks[input_data_observed_points_count] = (line[0], line[1], line[2])

                elif input_data_type_index == 1:  # for paths
                    print("Path: " + str(line))
                    input_data_observed_paths_count += 1
                    # new code to add
                    print(line[3])
                    print(line[4])

                    # To get the line with the informations(like peak height) about the current peak, it is the peak source
                    lineFromPeakA = peaks[int(line[3])]
                    # To get the height in the line about the second the current peak, it is the peak source
                    weightPeakA = int(lineFromPeakA[2])
                    # To get the line with the informations(like peak height) about the current peak, it is the peak destination
                    lineFromPeakB = peaks[int(line[4])]
                    # To get the height in the line about the second  current peak, it is the peak destination
                    weightPeakB = int(lineFromPeakB[2])

                    # compute_weight() : function to compute the weight of the vertices and return it (in secondes)
                    graph[int(line[3]) - 1][int(line[4]) - 1] = Compute.compute_weight(line[2], abs(weightPeakA - weightPeakB), line[1])
                    # To display our graph :
                    for i in range(37):
                        print(graph[i])

        print("Supposed points count: " + str(input_data_supposed_points_count))
        print("Observed points count: " + str(input_data_observed_points_count))
        print("Supposed paths count: " + str(input_data_supposed_paths_count))
        print("Observed paths count: " + str(input_data_observed_paths_count))
        fp.close()

    except FileNotFoundError as e:
        error = -1;
        print(e)

    return error