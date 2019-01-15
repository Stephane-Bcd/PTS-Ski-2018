
# This function allows to count the number of occurrences in a list
def countX(lst, x):
     count = 0
     for element in lst:
          if (element == x):
                count = count + 1
     return count

# This function allows to find the biggest occurrence in a list
def Find_the_biggest_occurence(array_occurence, size_array):

     valueMax = 0

     for index in range(size_array):
         value = countX(array_occurence, array_occurence[index])
         if (value > valueMax):
            valueMax = value

     return valueMax

# Function to know time of bus, because we have two paths
def compute_time_bus(travelName):
    if '1800' in travelName:
        weight_vertice = 30 * 60
    else:
        weight_vertice = 40 * 60
    return weight_vertice


# Function to compute the weight of each vertices, and return it (weight in secondes)
def compute_weight(type, distance, travelName):
    weight_vertice = 0
    # part about descents
    if type == "V":
        weight_vertice = (5 * 60) * (distance / 100)
    elif type == "B":
        weight_vertice = (4 * 60) * (distance / 100)
    elif type == "R":
        weight_vertice = (3 * 60) * (distance / 100)
    elif type == "N":
        weight_vertice = (2 * 60) * (distance / 100)
    elif type == "KL":
        weight_vertice = 10 * (distance / 100)
    elif type == "SURF":
        weight_vertice = (10 * 60) * (distance / 100)
    # part to mount
    elif type == "TPH":
        weight_vertice = 4 * 60 + (2 * 60) * (distance / 100)
    elif type == "TC":
        weight_vertice = 2 * 60 + (3 * 60) * (distance / 100)
    elif type == "TSD":
        weight_vertice = 1 * 60 + (3 * 60) * (distance / 100)
    elif type == "TS":
        weight_vertice = 1 * 60 + (4 * 60) * (distance / 100)
    elif type == "TK":
        weight_vertice = 1 * 60 + (4 * 60) * (distance / 100)
    elif type == "BUS":
        weight_vertice = compute_time_bus(travelName)
    # If we can not find the type :
    else:
        weight_vertice = -1
        print(" Function compute_weight : Error with the type ")

    return weight_vertice

