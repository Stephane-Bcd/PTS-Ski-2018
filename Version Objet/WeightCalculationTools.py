#Function that computes the maximum flow /hour of the edge
def compute_maxflow(edge_type):
	if edge_type == "TPH":
		return 1200
	elif edge_type == "TC":
		return 2200
	elif edge_type == "TSD":
		return 2500
	elif edge_type == "TS":
		return 1800
	elif edge_type == "TK":
		return 800
	elif edge_type == "BUS":
		return 300
	else:
		return float('inf')

#Function that checks if actual Edge type is a descent(True) or a rise(False) 
def is_descent (edge_type):
	return edge_type in ["V", "B", "R", "N", "KL", "SURF"]
	
	
# Function to know time of bus, because we have two paths
def compute_time_bus(travelName):
    if '1800' in travelName:
        weight_vertice = 30.0 * 60.0
    else:
        weight_vertice = 40.0 * 60.0
    return weight_vertice


# Function to compute the weight of an edge
def compute_weight(edge_type, node1_altitude, node2_altitude, node1_name, node2_name):

	#default weight value
	weight_vertice = float("Inf")

	#Difference in heights (denivele)
	diff_in_heights = float(abs(node1_altitude-node2_altitude))

	# part about descents
	if edge_type == "V":
		weight_vertice = (5.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "B":
		weight_vertice = (4.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "R":
		weight_vertice = (3.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "N":
		weight_vertice = (2.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "KL":
		weight_vertice = 10.0 * (diff_in_heights / 100.0)
	elif edge_type == "SURF":
		weight_vertice = (10.0 * 60.0) * (diff_in_heights / 100.0)
	# part about mount
	elif edge_type == "TPH":
		weight_vertice = 4.0 * 60.0 + (2.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "TC":
		weight_vertice = 2.0 * 60.0 + (3.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "TSD":
		weight_vertice = 1.0 * 60.0 + (3.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "TS":
		weight_vertice = 1.0 * 60.0 + (4.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "TK":
		weight_vertice = 1.0 * 60.0 + (4.0 * 60.0) * (diff_in_heights / 100.0)
	elif edge_type == "BUS":
		weight_vertice = compute_time_bus(node1_name + "-" + node2_name)

	return weight_vertice

