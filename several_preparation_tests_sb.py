# Class to add element to dictionnary with unique keys


class UniqueDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            dict.__setitem__(self, key, value)
        else:
            raise KeyError("'" + key + "' Key already exists")


diction = UniqueDict()
#print(diction)
diction.__setitem__("1", "val")
#print(diction)
try:
    diction.__setitem__("1", "val2")
except KeyError as e:
    print(e)


# read and split input file python

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
    fp = open('./data_arcs.txt', 'r')
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
                # new code to add
            elif input_data_type_index == 1:  # for paths
                print("Path: " + str(line))
                input_data_observed_paths_count += 1
                # new code to add

    print("Supposed points count: " + str(input_data_supposed_points_count))
    print("Observed points count: " + str(input_data_observed_points_count))
    print("Supposed paths count: " + str(input_data_supposed_paths_count))
    print("Observed paths count: " + str(input_data_observed_paths_count))
    fp.close()
except FileNotFoundError as e:
    print(e)
