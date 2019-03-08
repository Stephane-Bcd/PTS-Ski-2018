'''
	to use networkx package, do the following:
		pip install networkx==2.2
	print
	if pip not installed, do the following:
		sudo apt update
		sudo apt install python3-pip
	
	networkx package documentation: https://networkx.github.io/documentation/stable/_downloads/networkx_reference.pdf
	methods list: https://networkx.github.io/documentation/stable/reference/algorithms/shortest_paths.html
	download page: https://pypi.org/project/networkx/2.2/
	FreeBSD licence
'''

import networkx as nx
import json
import LogsService
import WeightCalculationTools
import time
import random
import os


'''
	GENERAL SHARED ATTRIBUTES
'''

#Path for logs
logs_file_path = "./Logs.txt"



def parse_nodes (file_path, verbose = False):
	'''
	===========================================================================
	FUNCTION TO PARSE NODES DATA FROM INPUT FILE 
	RETURNS CONVERTED NODES INTO LIST OF JSONS
	file_path: path to the input file containing edges and nodes
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".parse_nodes", logs_file_path)
	print('Nodes parsing into List of JSONs started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Nodes parsing into List of JSONs started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	
	# supposed and observed counts of nodes
	input_data_supposed_nodes_count = 0
	input_data_observed_nodes_count = 0
	
	# 1 for nodes 2 for Edges
	input_data_type_index = 0 
	
	#Final output List of JSONs
	JSONs_list = []
	
	# Reading the input file containing edges and nodes :
	fp = open(file_path, 'r')
	lines = fp.readlines()
	
	for line in lines:
		line = line.strip().replace("\n", "").split("\t")

		# if current line is supposed count of edges or a nodes
		if line.__len__() == 1:

			input_data_type_index += 1

			if input_data_type_index == 1:  # for nodes
				input_data_supposed_nodes_count = int(line[0])
			else:
				break

		# If current line is an edge or a node
		else:
			if input_data_type_index == 1:  # for nodes
				if verbose: logger.info("Node: " + str(line))
				input_data_observed_nodes_count += 1
				
				new_object = {}
				
				#actual node id
				new_object["node_id"] = int(line[0])
				#actual node name
				new_object["node_name"] = line[1]
				#actual node altitude
				new_object["node_altitude"] = int(line[2])
				
				#adding to the result list
				JSONs_list.append(new_object)
				
	fp.close()
	
	#If the observed and supposed of nodes are not the same
	if (input_data_supposed_nodes_count != input_data_observed_nodes_count):
		#Error message
		print("Nodes parsing into List of JSONs error: Not same supposed and observed nodes")
		logger.info("Nodes parsing into List of JSONs error: Not same supposed and observed nodes")
		
		raise ValueError("Nodes parsing into List of JSONs error: Not same supposed and observed nodes")
	
	else:
		if verbose: print("List of Nodes: \n" + json.dumps(JSONs_list, indent=4, sort_keys=True))
		if verbose: logger.info("List of Nodes: \n" + json.dumps(JSONs_list, indent=4, sort_keys=True))
		
		#End message
		print("Nodes parsing into List of JSONs finished successfully")
		logger.info("Nodes parsing into List of JSONs finished successfully")
					
	return JSONs_list


def parse_edges (file_path, verbose = False):
	'''
	===========================================================================
	FUNCTION TO PARSE EDGES DATA FROM INPUT FILE 
	RETURNS CONVERTED EDGES INTO LIST OF JSONS
	file_path: path to the input file containing edges and nodes
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".parse_edges", logs_file_path)
	print('Edges parsing into List of JSONs started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Edges parsing into List of JSONs started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	
	# supposed and observed counts of edges
	input_data_supposed_edges_count = 0
	input_data_observed_edges_count = 0
	
	# 1 for nodes 2 for Edges
	input_data_type_index = 0 
	
	#Final output List of JSONs
	JSONs_list = []
	
	# Reading the input file containing edges and nodes :
	fp = open(file_path, 'r')
	lines = fp.readlines()
	
	for line in lines:
		line = line.strip().replace("\n", "").split("\t")

		# if current line is supposed count of edges or a nodes
		if line.__len__() == 1:

			input_data_type_index += 1

			if input_data_type_index == 2:  # for edges
				input_data_supposed_edges_count = int(line[0])
			elif input_data_type_index != 1:
					break

		# If current line is an edge or a node
		else:
			if input_data_type_index == 2:  # for edges
				if verbose: logger.info("Edge: " + str(line))
				input_data_observed_edges_count += 1
				
				new_object = {}
				
				#actual edge id
				new_object["edge_id"] = int(line[0])
				#actual edge name
				new_object["edge_name"] = line[1]
				#actual edge type
				new_object["edge_type"] = line[2]
				#actual nodes ids
				new_object["node1_id"] = int(line[3])
				new_object["node2_id"] = int(line[4])
				
				JSONs_list.append(new_object)
				
	fp.close()
	
	#If the observed and supposed of nodes are not the same
	if (input_data_supposed_edges_count != input_data_observed_edges_count):
		#Error message
		print("Edges parsing into List of JSONs error: Not same supposed and observed nodes")
		logger.info("Edges parsing into List of JSONs error: Not same supposed and observed nodes")
		
		raise ValueError("Edges parsing into List of JSONs error: Not same supposed and observed nodes")
	
	else:
		if verbose: print("List of Edges: \n" + json.dumps(JSONs_list, indent=4, sort_keys=True))
		if verbose: logger.info("List of Edges: \n" + json.dumps(JSONs_list, indent=4, sort_keys=True))
		
		#Ending message
		print("Edges parsing into List of JSONs finished successfully")
		logger.info("Edges parsing into List of JSONs finished successfully")
					
	return JSONs_list


def create_new_graph(graph_type, graph_name = "graph", verbose = False):
	'''
	===========================================================================
	FUNCTION THAT CREATES A NEW GRAPH AND RETURNS IT
	Takes in parameters:
	graph_type: a string to specify the type of graph. Here is the list:
		- "multidirected" => Not simple directed graph
	===========================================================================
	'''
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".create_new_graph", logs_file_path)
	print('Graph creation started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Graph creation started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	
	graph = None
	
	if graph_type == "multidirected":
		graph = nx.MultiDiGraph(name = graph_name)
	else:
		#Error message
		print("Graph creation error: graph type not supported")
		if verbose: logger.info("Graph creation error: graph type not supported")
		
		return graph
		
	if verbose: print("Created Graph: " + graph_type + " named " + graph_name)
	logger.info("Created Graph: " + graph_type + " named " + graph_name)
		
	#Ending message
	print("Graph \'" + graph.graph["name"] + "\' created successfully")
	logger.info("Graph \'" + graph.graph["name"] + "\' created successfully")
	
	return graph


def clear_graph(graph, verbose = False):
	'''
	===========================================================================
	FUNCTION CLEARS THE GRAPH
	Takes in parameters:
	graph: a reference to a graph that has to be cleared
	===========================================================================
	'''
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".clear_graph", logs_file_path)
	print('Graph clearing started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Graph clearing started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	
	#Graph name will be saved
	graph_name = graph.graph["name"]
	
	graph.clear()
	
	graph.graph["name"] = graph_name
		
	#Ending message
	print("Graph \'" + graph.graph["name"] + "\' cleared successfully")
	logger.info("Graph \'" + graph.graph["name"] + "\' cleared successfully")
	

def get_filtered_graph_on_edge_type(graph, filter_list, verbose = False):
	'''
	===========================================================================
	FUNCTION TO GET A SUBGRAPH WITH FILTERED EDGES TYPES
	graph: graph to be filtered
	filter_list: list of edges types values to be filtered
	verbose: True if you want all informations in the log file
	returns a new graph with filtered edges on edges types
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".get_filtered_graph_on_edge_type", logs_file_path)
	print("Edges filtering started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Edges filtering started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	edges = graph.edges(data=True, keys=True)
	filtered_edges = []
	
	for edge in edges:
		if edge[3]["edge_type"] not in filter_list:
			filtered_edges.append((edge[0], edge[1], edge[2]))
	
		
	#Ending message
	print("Edges filtering finished successfully")
	logger.info("Edges filtering finished successfully")
	
	
	return graph.edge_subgraph(filtered_edges)


def insert_nodes_and_edges(graph, nodes, edges, verbose = False):
	'''
	===========================================================================
	FUNCTION TO INSERT NODES AND EDGES INTO A GRAPH
	graph: graph to be filled
	nodes: List of Nodes Objects (JSONs)
	edges: List of Edges Objects (JSONs)
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".insert_nodes_and_edges", logs_file_path)
	print("Nodes and Edges insertion into \'" + graph.graph["name"] + "\' graph started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Nodes and Edges insertion into \'" + graph.graph["name"] + "\' graph started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	for node in nodes:
		graph.add_node(node["node_id"],
		
			object_type = "node",
			node_id = node["node_id"],
			node_name = node["node_name"],
			node_altitude = node["node_altitude"]
		)
				
	for edge in edges:
		#is this edge a descent?
		is_descent = WeightCalculationTools.is_descent(edge["edge_type"])
		#actual maximal flow
		max_flow = WeightCalculationTools.compute_maxflow(edge["edge_type"])
		
		graph.add_edge(edge["node1_id"], edge["node2_id"], 
		
			object_type = "edge",
			node1_id = edge["node1_id"],
			node2_id = edge["node2_id"],
			edge_id = edge["edge_id"], 
			edge_name = edge["edge_name"], 
			edge_type = edge["edge_type"],
			is_descent = is_descent,
			max_flow = max_flow
		)
	
	#printing details about inserted data
	if verbose: print("Nodes inserted:\n" + json.dumps(list(graph.nodes(data=True)), indent=4, sort_keys=True))
	if verbose: logger.info("Nodes inserted:\n" + json.dumps(list(graph.nodes(data=True)), indent=4, sort_keys=True))
	if verbose: print("Edges inserted:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
	if verbose: logger.info("Edges inserted:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
		
	#Ending message
	print("Nodes and Edges insertion finished successfully")
	logger.info("Nodes and Edges insertion finished successfully")
	

def index_nodes_by_name (graph, verbose = False):
	'''
	===========================================================================
	FUNCTION TO INDEX NODES BY NAMES
	graph: graph which the nodes need to be indexed
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".index_nodes_by_name", logs_file_path)
	print("Nodes index by names started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Nodes index by names started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	in_out_index = {}
	
	for element in graph.nodes(data=True):
		in_out_index[element[1]["node_name"]] = element[0]
	
	if verbose: print("Nodes by name index:\n" + str(in_out_index))
	logger.info("Nodes by name index:\n" + str(in_out_index))
	
	#Ending message
	print("Nodes index by names finished successfully")
	logger.info("Nodes index by names finished successfully")
	
	return in_out_index
	
	
def index_edges_by_2D_key (graph, verbose = False):
	'''
	===========================================================================
	FUNCTION TO INDEX EDGES BY 2D KEYS
	graph: graph which the edges need to be indexed
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".index_edges_by_2D_key", logs_file_path)
	print("Edges index by 2D keys started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Edges index by 2D keys started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	in_out_index = {}
	
	for element in graph.edges(data=True, keys=True):
		key = str(element[0])+'-'+str(element[1])
		
		if key in in_out_index:
			if not isinstance(in_out_index[key], list):
				in_out_index[key] = []
		else:
			in_out_index[key] = []
			
		in_out_index[key].append([element[0],element[1],element[2]])
	
	if verbose: print("Edges by 2D keys index:\n" + str(in_out_index))
	logger.info("Edges by 2D keys index:\n" + str(in_out_index))
	
	#Ending message
	print("Edges index by 2D keys finished successfully")
	logger.info("Edges index by 2D keys finished successfully")
	
	return in_out_index
	

def get_node_by_id (graph, node_id):
	'''
	===========================================================================
	FUNCTION TO GET NODE DATA IN JSON FORMAT
	graph: graph in which we have to look for the node
	node_id: (integer) ID of a node
	returns: the JSON data concerning the node
	===========================================================================
	'''
	
	return graph.nodes[node_id]


def get_node_by_name (graph, index_nodes_by_name, node_name):
	'''
	===========================================================================
	FUNCTION TO GET NODE DATA IN JSON FORMAT
	graph: graph in which we have to look for the node
	index_nodes_by_name: index containing Name(Node) => Id(Node) (it has to be a JSON {})
	node_name: (string) name of a node
	returns: the JSON data concerning the node
	===========================================================================
	'''
	
	return get_node_by_id(graph, index_nodes_by_name[node_name])
	
	
def get_edge_by_3D_id (graph, edge_3d_id):
	'''
	===========================================================================
	FUNCTION TO GET EDGE DATA IN JSON FORMAT
	graph: graph in which we have to look for the edge
	edge_3d_id: (list of integers) ID of an edge (source, target, parallel edge id)
	returns: the JSON data concerning the edge
	===========================================================================
	'''
	
	return graph.edges[edge_3d_id[0], edge_3d_id[1], edge_3d_id[2]]
	
		
def get_edges_by_2D_id (graph, index_edges_by_2D_key, edge_2d_id):
	'''
	===========================================================================
	FUNCTION TO GET EDGE DATA IN JSON FORMAT
	graph: graph in which we have to look for the edge
	index_edges_by_2D_key: index containing 2D Id(Edge) => 3D ids(Edge) (it has to be a JSON {})
	edge_2d_id: (list of integers) ID of an edge (source, target)
	returns: the JSON data concerning the edge
	===========================================================================
	'''
	
	id_str = str(edge_2d_id[0])+'-'+str(edge_2d_id[1])
	
	edges_list = []
	
	for _3d_id in index_edges_by_2D_key[id_str]:
		edges_list.append(get_edge_by_3D_id(graph, _3d_id))
	
	return edges_list


def get_shortest_edge_between_two_nodes(graph, node1_id, node2_id, index_edges_by_2D_key, weight, filter_edges, verbose = False):
	'''
	===========================================================================
	FUNCTION TO GET THE SHORTEST EDGE BETWEEN TWO NODES
	In fact, if there are several parallel edges; we need to know which edge is the shortest one
	graph: graph which the edges need to be indexed
	node1_id, node2_id: ids if the two nodes
	index_edges_by_2D_key: index containing 2D Id(Edge) => 3D ids(Edge)
	weight: the weight used in the graph to find the shortest edge
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#Get all the parallel edges between two nodes
	parallel_edges = get_edges_by_2D_id (graph, index_edges_by_2D_key, [node1_id, node2_id])
	
	#initialising to infinite the actual weight
	shortest_edge = {}
	shortest_edge[weight] = float("Inf")
	
	for edge in parallel_edges:
		if shortest_edge[weight] > edge[weight] and edge["edge_type"] not in filter_edges:
			shortest_edge = edge
	
	return shortest_edge


def compute_normal_weight (graph, verbose = False):
	'''
	===========================================================================
	FUNCTION TO COMPUTE THE NORMAL WEIGHTS DEPENDING ON THE TYPES OF EDGES
	graph: graph for which normal weights have to be computed
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".compute_normal_weight", logs_file_path)
	print("Normal weights computation started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Normal weights computation started in " + ("verbose" if verbose else "not verbose") + " mode." )

	for edge in graph.edges(data=True, keys=True):
		
		node1_id = edge[3]["node1_id"]
		node2_id = edge[3]["node2_id"]
		
		edge_type = edge[3]["edge_type"]
		
		node1_data = get_node_by_id (graph, node1_id)
		node2_data = get_node_by_id (graph, node2_id)
		
		node1_altitude = node1_data["node_altitude"]
		node2_altitude = node2_data["node_altitude"]
		node1_name = node1_data["node_name"]
		node2_name = node2_data["node_name"]
		
		#actual normal weight (normal because to calculate normal shortest path without taking in consideration the flow or the fun)
		normal_weight = WeightCalculationTools.compute_weight(edge_type, node1_altitude, node2_altitude, node1_name, node2_name)
		
		graph.edges[edge[0], edge[1], edge[2]]['normal_weight'] = normal_weight
		
	
	if verbose: print("Edges with normal weights:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
	if verbose: logger.info("Edges with normal weights:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
	
	#Ending message
	print("Normal weights computation finished successfully")
	logger.info("Normal weights computation finished successfully")
	
	
def search_coef_favorise_descents (graph, verbose = False):
	'''
	===========================================================================
	FUNCTION THAT LOOKS FOR A COEFFICIENT TO DEFAVORISE RISES AND FAVORISE DESCENTS
	This coefficient is used to multiply the rises weights so, it'll be greater than the descents ones
	graph: graph for which this coefficient has to be found
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".search_coef_favorise_descents", logs_file_path)
	print("Searching for coefficient to favorise descents started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Searching for coefficient to favorise descents started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	#These two variables will make possible the calculation of weight for a shortest path considering the most interesting path (descents favorised)
	maximum_val_weight_descent = 0.0
	minimum_val_weight_rise = float("Inf")

	#Multiplicator for most interesting shortest path (more descents !)
	multiplicator_interesting_shortest_path = 1.0
	
	for edge in graph.edges(data=True, keys=True):
		
		#Calculating max weight for descents and min weight for rises to make possible calculation of interesting shortest path
		is_descent = edge[3]["is_descent"]
		normal_weight = edge[3]["normal_weight"]
		
		if is_descent:
			if maximum_val_weight_descent < normal_weight:
				maximum_val_weight_descent = normal_weight
		else:
			if minimum_val_weight_rise > normal_weight:
				minimum_val_weight_rise = normal_weight
				
				
	# Calculating the multiplicator for rises weights by dividing max descents weight by min rises weight
	# Example: descent max = 500 ; rise min = 300 ; So 500/300 = 1.666666.... And 300 * 1.66666.... = 500 ! Bingo ! So; All rises weights will be multiplicated by 1.66666
	multiplicator_interesting_shortest_path = maximum_val_weight_descent / minimum_val_weight_rise
	logger.info("Multiplicator for most interesting shortest path found: " + str(multiplicator_interesting_shortest_path) + " Using descent max weight: " +str(maximum_val_weight_descent) + " And rises min weight: " + str(minimum_val_weight_rise))
	
	#Ending message
	print("Searching for coefficient to favorise descents finished successfully")
	logger.info("Searching for coefficient to favorise descents finished successfully")
	
	return multiplicator_interesting_shortest_path
	
	
def compute_interesting_path_weight (graph, verbose = False):
	'''
	===========================================================================
	FUNCTION THAT COMPUTES A WEIGHT USED TO FAVORISE DESCENDS USING A COEFFICIENT
	coef: This coefficient is calculated using search_coef_favorise_descents (graph, verbose = False) function
	graph: graph for which this weight has to be calculated
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".compute_interesting_path_weight", logs_file_path)
	print("Interesting paths weights computation started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Interesting paths weights computation started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	#search for needed coefficient
	coef = search_coef_favorise_descents (graph, verbose = False)
	
	#We will create a new Edge parameter to store a weight that favorises descents to rises by increasing rises normal weights
	for edge in graph.edges(data=True, keys=True): #keys=True is used to identify parallel edges
		
		#JSON object containing all informations calculated before (name, normal weight etc)
		actual_edge_json = edge[3]
		actual_edge_id = actual_edge_json["edge_id"]
		actual_edge_is_descent = actual_edge_json["is_descent"]
		actual_edge_normal_weight = actual_edge_json["normal_weight"]
		
		if actual_edge_is_descent: #if it is a descent (more interesting so normal weight)
			actual_edge_most_interesting_path_weight = actual_edge_normal_weight
		else: #if it is a rise (less interesting so bigger weight)
			actual_edge_most_interesting_path_weight = actual_edge_normal_weight * coef
		
		graph.edges[edge[0], edge[1], edge[2]]['most_interesting_path_weight'] = actual_edge_most_interesting_path_weight
	
	
	if verbose: print("Edges with interesting paths weights:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
	if verbose: logger.info("Edges with interesting paths weights:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
	
	#Ending message
	print("Interesting paths weights computation finished successfully")
	logger.info("Interesting paths weights computation finished successfully")


def compute_coef_for_flows(flow_value, max_flow, normal_weight):
	return normal_weight * (max_flow/flow_value)

	
def compute_less_flow_weight (graph, verbose = False):
	'''
	===========================================================================
	FUNCTION THAT COMPUTES A WEIGHT USED TO FAVORISE DESCENDS USING A COEFFICIENT
	coef: This coefficient is calculated using search_coef_favorise_descents (graph, verbose = False) function
	graph: graph for which this weight has to be calculated
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".compute_interesting_path_weight", logs_file_path)
	print("Interesting paths weights computation started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Interesting paths weights computation started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	
	
	#Ending message
	print("Interesting paths weights computation finished successfully")
	logger.info("Interesting paths weights computation finished successfully")
	

def parse_current_flows(file_path, verbose = False):
	'''
	===========================================================================
	FUNCTION TO PARSE THE DATA FROM FLOWS FILE
	file_path: path to the input file containing current flows for rises 
	verbose: True if you want all informations in the log file
	returns a dictionnary Key (Edge) => actual_flow
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".parse_current_flows", logs_file_path)
	print("Parsing current flows file started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Parsing current flows file started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	# Reading the input file containing current flows :
	fp = open(file_path, 'r')
	lines = fp.readlines()
	
	#Dictionnary containing all current flows for each edge
	current_flows = {}
	
	#First filling a dictionnary to have a sorted 'list' of current flows (better performance for next step)
	for line in lines:
		line = line.strip().replace("\n", "").split("\t")
		
		if(line.__len__() == 2):
			current_flows [int(line[0])] = float(line[1])
		
	fp.close()
	
	#Ending message
	print("Parsing current flows file finished successfully")
	logger.info("Parsing current flows file finished successfully")
	
	return current_flows


def generate_random_current_flows ( seed, graph, output_file_path, verbose = False):
	'''
	===========================================================
	FUNCTION TO GENERATE A CURRENT FLOWS FILE RANDOMLY
	It takes max flows and transformes it to a +/-30% new value: the current flow
	seed
	graph: graph is needed to generate the current_flows
	output_file_path: generated current flows file path
	verbose: True if you want to print all informations
	===========================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".generate_random_current_flows", logs_file_path)
	logger.info ("Starting to generate current flows file in " + ("verbose" if verbose else "not verbose") + " mode ...")
	print ("Starting to generate current flows file in " + ("verbose" if verbose else "not verbose") + " mode ...")
	
	
	if os.path.exists(output_file_path):
		os.remove(output_file_path)
	
	random.seed(seed)
	
	for edge in list(graph.edges(data=True)):
		edge_attributes = edge[2]
		max_flow = edge_attributes['max_flow']
		id = edge_attributes['edge_id']
		
		random_multiplier = float(random.randrange(70, 130))/100.0
		with open(output_file_path, 'a') as the_file:
			the_file.write(str(id) + '\t' + str(500 if max_flow == float("Inf") else int(max_flow * random_multiplier) ) + '\n')
		
		the_file.close()
		
	logger.info ("Current flows file generated !")
	print ("Current flows file generated !")


def insert_current_flows(graph, current_flows, verbose = False):
	'''
	===========================================================================
	FUNCTION TO INSERT THE DATA FROM ACTUAL FLOWS DICTIONNARY TO GRAPH
	graph: Graph in which we need to insert the actual flows
	current_flows: a dictionnary Key (Edge) => actual_flow
	verbose: True if you want all informations in the log file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".insert_current_flows", logs_file_path)
	print("Current Flows importation started in " + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info("Current Flows importation started in " + ("verbose" if verbose else "not verbose") + " mode." )
	
	
	#For each edge, put the corresponding current flow by matching using the ids from input files
	for edge in list(graph.edges(data=True, keys=True)):
		
		edge_attributes = edge[3]
		id = edge_attributes["edge_id"]
		
		graph.edges[edge[0], edge[1], edge[2]]['actual_flow'] = current_flows[id]
	
	if verbose :
		#log the result edges
		updated_edges = list(graph.edges(data=True))
		pretty_updated_edges = json.dumps(updated_edges, indent=4, sort_keys=True)
		
		logger.info ("UPDATED  EDGES:\n")
		logger.info (pretty_updated_edges)
	
	print("Current Flows importation finished successfully !")
	logger.info("Current Flows importation finished successfully !" )
	
	
def display_graph_console(graph):
	'''
	===========================================================================
	FUNCTION TO DISPLAY ALL GRAPH CONTENT IN CONSOLE
	graph: Graph which we need to display
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".display_graph_console", logs_file_path)
	print("\'"+graph.graph["name"]+"\' Graph display in console started.")
	logger.info("\'"+graph.graph["name"]+"\' Graph display in console started.")
	
	
	
	print("NODES:\n" + json.dumps(list(graph.nodes(data=True)), indent=4, sort_keys=True))
	logger.info("NODES:\n" + json.dumps(list(graph.nodes(data=True)), indent=4, sort_keys=True))
	
	print("EDGES:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
	logger.info("EDGES:\n" + json.dumps(list(graph.edges(data=True, keys=True)), indent=4, sort_keys=True))
	
	#Ending message
	print("\'"+graph.graph["name"]+"\' Graph display in console finished successfully")
	logger.info("\'"+graph.graph["name"]+"\' Graph display in console finished successfully")
	

def load_all_graph_input_data(edges_nodes_input_file, actual_flows_input_file, graph_name, verbose = False, generate_current_flows = False, seed = 100):
	'''
	===========================================================================
	FUNCTION TO LOAD ALL GRAPH FROM INPUT FILES
	edges_nodes_input_file: path to file containing edges and nodes
	actual_flows_input_file: path to file containing actual flows for each edge
	graph_name: Graph name
	verbose: True if you want to print everything
	generate_current_flows: True if you want to generate randomly the actual flows file
	seed: needed if you want to generate the current flows file
	===========================================================================
	'''
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".load_all_graph_input_data", logs_file_path)
	print("Loading all data into new graph process started.")
	logger.info("Loading all data into new graph process started.")
	
	
	#Parsing data
	nodes = parse_nodes (edges_nodes_input_file, verbose)
	edges = parse_edges (edges_nodes_input_file, verbose)
	
	#Creating graph
	graph = create_new_graph("multidirected", graph_name, verbose)
	clear_graph(graph, verbose)
	
	#Inserting data into graph
	insert_nodes_and_edges(graph, nodes, edges, verbose)
		
	#generating current flows if needed
	if generate_current_flows or not os.path.exists(actual_flows_input_file):
		generate_random_current_flows ( seed, graph, actual_flows_input_file, verbose)
		
	#Parsing and inserting current flows
	current_flows = parse_current_flows(actual_flows_input_file, verbose)
	insert_current_flows(graph, current_flows, verbose)
	
	#Compute graph weights
	compute_normal_weight (graph, verbose)
	
	#Compute interesting paths weights
	compute_interesting_path_weight (graph, verbose)
	
	#Ending message
	print("\'"+graph.graph["name"]+"\' Graph created and filled with input data successfully")
	logger.info("\'"+graph.graph["name"]+"\' Graph created and filled with input data successfully")
	
	return graph


def Dijkstra (graph, source, target, weight, index_nodes_name_to_key, index_edges_2dkey_to_object, filter_edges, verbose = False):
	'''
	===========================================================================
	FUNCTION TO EXECUTE DIJKSTRA ALGORITHM FOR SHORTEST PATH
	graph: graph on which the algorithm has to be executed
	source, target: source and target nodes
	weight: string that defines which weight has to be used to calculate shortest path
	index_nodes_name_to_key: index containing Name(Node) => Id(Node)
	index_edges_2dkey_to_object: index containing 2D Id(Edge) => 3D ids(Edge)
	filter_edges: filter on edges (a list such as ["N", "R"], let [] if none
	verbose: True if you want to print everything
	===========================================================================
	'''
	
	start = time.time()
	
	#initialising logs and Intro Message
	logger = LogsService.initialise_logs(__name__ + ".Dijkstra", logs_file_path)
	print('Dijkstra algorithm started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Dijkstra algorithm started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	
	#test if there is any filter
	is_filtered = len(filter_edges) > 0
	
	#if there are filters, we create a filtered graph
	if is_filtered:
		graph = get_filtered_graph_on_edge_type(graph, filter_edges, verbose)
		index_nodes_name_to_key = index_nodes_by_name (graph, verbose)
		index_edges_2dkey_to_object = index_edges_by_2D_key (graph, verbose)
	
	#Return JSON variable
	final_res = {
		"source": source,
		"target": target,
		"execution_mode": "Dijkstra",
		"used_weight": weight,
		"execution_time": 0.0,
		"nodes": [],
		"edges": [],
		"mixed": [],
		"path_time": 0.0,
		"filter_on": filter_edges
	}
	
	#Checking if source and target are Names or Ids
	
	if verbose: logger.info("Selected source: " + str(source))
	if verbose: print("Selected source: " + str(source))
		
		
	if verbose: logger.info("Selected target: " + str(target))
	if verbose: print("Selected target: " + str(target))
	
	
	#Dijkstra execution if path exists
	if nx.has_path(graph, source, target): 
		
		#Here are the two results of Networkx execution
		shortest_path = nx.dijkstra_path(graph, source, target, weight=weight)
		path_time = 0.0
		
		#Filling final result JSON with Edges and nodes
		precedent_node_id = None
		for node_id in shortest_path:
			
			#for edges
			if node_id and precedent_node_id:
				current_edge = get_shortest_edge_between_two_nodes(graph, precedent_node_id, node_id, index_edges_2dkey_to_object, weight, filter_edges, verbose)
				final_res["edges"].append(current_edge)
				final_res["mixed"].append(current_edge)
				path_time += current_edge["normal_weight"]
			
			#for nodes
			current_node = get_node_by_id (graph, node_id)
			final_res["nodes"].append(current_node)
			final_res["mixed"].append(current_node)
			
			precedent_node_id = node_id
			
		#Filling final result with shortest path time
		final_res["path_time"] = path_time
	
	#End message
	end = time.time()
	print("Execution time: " + str(end - start))
	logger.info("Execution time: " + str(end - start))
	
	#Setting execution time in final result
	final_res["execution_time"] = str(end - start)
	
	return final_res


def shortest_path_result_into_text (JSON):
	'''
	===========================================================================
	FUNCTION TO CONVERT A JSON RESULT FROM SHORTEST PATH ALGO INTO TEXT
	JSON: result generated by shortest path algorithm
	returns a string containing a description text of the shortest path
	===========================================================================
	'''
	
	result_text = ""
	
	result_text += "\n---------------------------------------------------\n"
	result_text += "Execution mode: "+JSON["execution_mode"]+" , Execution time: "+str(JSON["execution_time"])
	if len(JSON["filter_on"]) > 0:
		result_text +="\nFilter on:"
		for filtr in JSON["filter_on"]:
			result_text += " \'" + filtr + "\'"
	else:
		result_text +="\nNo filter"
	
	result_text += ", Type of search: "
	
	if JSON["used_weight"] == "normal_weight":
		result_text += "Shortest path"
	elif JSON["used_weight"] == "most_interesting_path_weight":
		result_text += "Shortest path fovorizing descents"
	else:
		result_text += "Unknown"
	
	result_text += "\n---------------------------------------------------\n\n"
	result_text += "Instructions to go from \'" + str(JSON["source"]) + "\' to \'" + str(JSON["target"]) + "\'\n\n"
	
	first_Node = True
	first_Edge = True
	for element in JSON["mixed"]:
		if element["object_type"] == "node":
			if first_Node:
				result_text += "You're actually located at \'" + element["node_name"] + "\' station, with a "+ str(element["node_altitude"]) + "m high altitude.\n"
			else:
				result_text += "Then you will arrive at \'" + element["node_name"] + "\' station, with a "+ str(element["node_altitude"]) + "m high altitude.\n"
			first_Node = False
		else:
			if first_Edge:
				result_text += "In order to go to your destination, go first through \'" + element["edge_name"] + "\' path of \'" + element["edge_type"] + "\' type.\n"
			result_text += "It will take you  " + str(element["normal_weight"]) + " seconds to go to the next station.\n\n"
	
	result_text += "Total travel duration: " + str(JSON["path_time"]) + " seconds ! Enjoy !\n"
	
	return result_text
