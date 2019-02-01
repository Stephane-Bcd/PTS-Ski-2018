'''
	to use networkx package, do the following:
		pip install networkx==2.2
	
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

#Contains names to access directly to ids of nodes
DictionnaryNamesToKey = {}

#Contains ids to access to Edges directly
DictionnaryEdgesIdsToObjects = {}

#Directed weighted not simple graph
GraphMain = nx.MultiDiGraph()

#Path for logs
logs_file_path = "./Logs.txt"


'''
	===========================================================================
	FUNCTION TO READ THE DATA FROM INPUT FILE
	file_path: path to the input file containing edges and nodes
	verbose: True if you want all informations in the log file
	===========================================================================
'''

def import_nodes_and_edges(file_path, verbose = False):
	
	#initialising logs
	logger = LogsService.initialise_logs(__name__ + ".import_nodes_and_edges", logs_file_path)
	
	#Before starting anything, we clean the graph
	GraphMain.clear()
	
	# count of nodes and edges that we are supposed to have (count got from the input file)
	input_data_supposed_nodes_count = 0
	input_data_supposed_edges_count = 0

	# count of points and paths that we observe using lines (count got from the input files lines)
	input_data_observed_nodes_count = 0
	input_data_observed_edges_count = 0

	# boolean to know if first iteration
	first_iteration_on_file = True
	
	# index to know if actual data is point or path
	input_data_type_index = 0
	
	#These two variables will make possible the calculation of weight for a shortest path considering the most interesting path (descents favorised)
	maximum_val_weight_descent = 0.0
	minimum_val_weight_rise = float("Inf")

	#Multiplicator for most interesting shortest path (more descents !)
	multiplicator_interesting_shortest_path = 1.0

	# Reading the input file containing edges and nodes :
	fp = open(file_path, 'r')
	lines = fp.readlines()
	
	#Intro Message
	print('Nodes and Edges importation started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Nodes and Edges importation started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	if verbose: logger.info("Data from the input file:")
	
	for line in lines:
		line = line.strip().replace("\n", "").split("\t")

		# if current line is supposed count of edges or nodes
		if line.__len__() == 1:

			if not first_iteration_on_file:
				input_data_type_index += 1
			first_iteration_on_file = False

			if input_data_type_index == 0:  # for nodes
				input_data_supposed_nodes_count = int(line[0])

			elif input_data_type_index == 1:  # for edges
				input_data_supposed_edges_count = int(line[0])
			else:
				break

		# If current line is an edge or a node
		else:

			if input_data_type_index == 0:  # for nodes
				if verbose: logger.info("Node: " + str(line))
				input_data_observed_nodes_count += 1
				
				#actual node id
				node_id = int(line[0])
				#actual node name
				node_name = line[1]
				#actual node altitude
				node_altitude = int(line[2])
				
				#insert node with only the id
				GraphMain.add_node(node_id)
				#add id (just for information)
				GraphMain.nodes[node_id]['id'] = node_id
				#add name
				GraphMain.nodes[node_id]['name'] = node_name
				#add altitude
				GraphMain.nodes[node_id]['altitude'] = node_altitude
				
				#Fill dictionnary that contains for nodes Name -> Key
				DictionnaryNamesToKey[node_name] = node_id
				
					
				
			elif input_data_type_index == 1:  # for edges
				if verbose: logger.info("Edge: " + str(line))
				input_data_observed_edges_count += 1
				
				#actual edge id
				edge_id = int(line[0])
				#actual edge name
				edge_name = line[1]
				#actual edge type
				edge_type = line[2]
				#actual nodes ids
				node1_id = int(line[3])
				node2_id = int(line[4])
				#actual nodes altitudes
				node1_altitude = GraphMain.nodes[node1_id]['altitude']
				node2_altitude = GraphMain.nodes[node2_id]['altitude']
				#actual nodes names
				node1_name = GraphMain.nodes[node1_id]['name']
				node2_name = GraphMain.nodes[node2_id]['name']
				#actual normal weight (normal because to calculate normal shortest path without taking in consideration the flow or the fun)
				normal_weight = WeightCalculationTools.compute_weight(edge_type, node1_altitude, node2_altitude, node1_name, node2_name)
				#actual maximal flow
				max_flow = WeightCalculationTools.compute_maxflow(edge_type)
				
				
				#Calculating max weight for descents and min weight for rises to make possible calculation of interesting shortest path
				is_descent = WeightCalculationTools.is_descent(edge_type)
				if is_descent:
					if maximum_val_weight_descent < normal_weight:
						maximum_val_weight_descent = normal_weight
				else:
					if minimum_val_weight_rise > normal_weight:
						minimum_val_weight_rise = normal_weight
				
				#insert edge 
				GraphMain.add_edge(node1_id, node2_id, 
					id = edge_id, 
					name = edge_name, 
					type = edge_type,
					is_descent = is_descent,
					normal_weight = normal_weight,
					max_flow = max_flow
				)
				#InputEdgesList.append(value)

	'''
	print("Supposed points count: " + str(input_data_supposed_nodes_count))
	print("Observed points count: " + str(input_data_observed_nodes_count))
	print("Supposed paths count: " + str(input_data_supposed_edges_count))
	print("Observed paths count: " + str(input_data_observed_edges_count))
	'''
	
	fp.close()

	# If observed and supposed counts of nodes and edges aren't correct :
	if not(input_data_supposed_nodes_count == input_data_observed_nodes_count and input_data_supposed_edges_count == input_data_observed_edges_count) :
		logger.info("Data file contains incorrect informations (count of edges and nodes)" )
		raise ValueError("Data file contains incorrect informations (count of edges and nodes)")
	else:
		# Calculating the multiplicator for rises weights by dividing max descents weight by min rises weight
		# Example: descent max = 500 ; rise min = 300 ; So 500/300 = 1.666666.... And 300 * 1.66666.... = 500 ! Bingo ! So; All rises weights will be multiplicated by 1.66666
		multiplicator_interesting_shortest_path = maximum_val_weight_descent / minimum_val_weight_rise
		if verbose: logger.info("Multiplicator for most interesting shortest path found: " + str(multiplicator_interesting_shortest_path) + " Using descent max weight: " +str(maximum_val_weight_descent) + " And rises min weight: " + str(minimum_val_weight_rise))
		
		#We will create a new Edge parameter to store a weight that favorises descents to rises by increasing rises normal weights
		for edge in list(GraphMain.edges(data=True, keys=True)): #keys=True is used to identify parallel edges
			
			#JSON object containing all informations calculated before (name, normal weight etc)
			actual_edge_json = edge[3]
			actual_edge_id = actual_edge_json["id"]
			actual_edge_is_descent = actual_edge_json["is_descent"]
			actual_edge_normal_weight = actual_edge_json["normal_weight"]
			
			if actual_edge_is_descent: #if it is a descent (more interesting so normal weight)
				actual_edge_most_interesting_path_weight = actual_edge_normal_weight
			else: #if it is a rise (less interesting so bigger weight)
				actual_edge_most_interesting_path_weight = actual_edge_normal_weight * multiplicator_interesting_shortest_path
			
			GraphMain.edges[edge[0], edge[1], edge[2]]['most_interesting_path_weight'] = actual_edge_most_interesting_path_weight
			
			#Adding edges to a dictionnary to make search easier
			DictionnaryEdgesIdsToObjects[str(edge[0])+'-'+str(edge[1])+'-'+str(edge[2])] = edge
		

		if verbose :
		
			#log the result nodes
			inserted_nodes = list(GraphMain.nodes(data=True))
			pretty_inserted_nodes = json.dumps(inserted_nodes, indent=4, sort_keys=True)
			
			logger.info ("\n******************************************************\n                   INSERTED NODES                       \n******************************************************")
			logger.info (pretty_inserted_nodes)
			
			
			
			#log the result edges
			inserted_edges = list(GraphMain.edges(data=True))
			pretty_inserted_edges = json.dumps(inserted_edges, indent=4, sort_keys=True)
			
			logger.info ("\n******************************************************\n                   INSERTED EDGES                       \n******************************************************")
			logger.info (pretty_inserted_edges)
			
		
		print("Data insertion finished successfully !")
		logger.info("Data insertion finished successfully !" )
	

'''
	===========================================================================
	FUNCTION TO READ THE DATA FROM FLOWS FILE
	file_path: path to the input file containing current flows for rises 
	verbose: True if you want all informations in the log file
	===========================================================================
'''

def import_current_flows(file_path, verbose = False):
	
	#initialising logs
	logger = LogsService.initialise_logs(__name__ + ".import_current_flows", logs_file_path)
	
	#Intro Message
	print('Current Flows importation started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Current Flows importation started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	
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
	
	#For each edge, put the corresponding current flow by matching using the ids from input files
	for edge in list(GraphMain.edges(data=True, keys=True)):
		
		edge_attributes = edge[3]
		id = edge_attributes["id"]
		
		GraphMain.edges[edge[0], edge[1], edge[2]]['actual_flow'] = current_flows[id]
	
	if verbose :
		#log the result edges
		updated_edges = list(GraphMain.edges(data=True))
		pretty_updated_edges = json.dumps(updated_edges, indent=4, sort_keys=True)
		
		logger.info ("\n******************************************************\n                   UPDATED  EDGES                       \n******************************************************")
		logger.info (pretty_updated_edges)
	
	print("Current Flows importation finished successfully !")
	logger.info("Current Flows importation successfully !" )
	
def Dijkstra (source, target, weight, verbose = False):
	start = time.time()
	
	#initialising logs
	logger = LogsService.initialise_logs(__name__ + ".Dijkstra", logs_file_path)
	
	#Intro Message
	print('Dijkstra algorithm started in ' + ("verbose" if verbose else "not verbose") + " mode.")
	logger.info('Dijkstra algorithm started in ' + ("verbose" if verbose else "not verbose") + " mode." )
	
	#Return JSON variable
	final_res = {
		"nodes": [],
		"edges": [],
		"mixed": [],
		"path_length": 0.0
	}
	
	#Checking if source and target are Names or Ids
	
	if verbose: logger.info("Selected source: " + str(source))
	if verbose: print("Selected source: " + str(source))
	
	if isinstance(source, str): #if string entered, we check in names dictionnary to know the key
		source = DictionnaryNamesToKey[source]
		if verbose: logger.info("Selected source corresponds to id: " + str(source))
		if verbose: print("Selected source corresponds to id: " + str(source))
		
		
	if verbose: logger.info("Selected target: " + str(target))
	if verbose: print("Selected target: " + str(target))
	
	if isinstance(target, str): 
		target = DictionnaryNamesToKey[target]
		if verbose: logger.info("Selected target corresponds to id: " + str(target))
		if verbose: print("Selected target corresponds to id: " + str(target))
	
	
	#Dijkstra execution if path exists
	if nx.has_path(GraphMain, source, target): 
		
		res = nx.dijkstra_path(GraphMain, source, target, weight="normal_weight")
		
		res2 = nx.dijkstra_path_length(GraphMain, source, target, weight="normal_weight")
		
		
		#Calculating result var using res (we want edges and full nodes informations)
		
		precedent_node_key = None
		for node_key in res: #for each node
			
			#searching for best weight edge for two consecutive nodes
			actual_edge = None
			actual_edge_min_weight = float("Inf")
			
			
			if node_key and precedent_node_key: #if we have two consecutive nodes
				for key,value in DictionnaryEdgesIdsToObjects.items(): 
					if (str(precedent_node_key)+'-'+str(node_key)+'-') in key: #and we find their corresponding edges
						if value[3][weight] < actual_edge_min_weight: #it helps us choose the better weighted edge
							actual_edge = value[3]
							actual_edge_min_weight = value[3][weight]
							
				#we insert the best parallel edge into mixed and edges
				actual_edge["object_type"] = "edge"
				final_res["edges"].append(actual_edge)
				final_res["mixed"].append(actual_edge)
			
			precedent_node_key = node_key
			
			#inserting the node in nodes and mixed
			actual_node = GraphMain.nodes[node_key]
			actual_node["object_type"] = "node"
			final_res["nodes"].append(actual_node)
			final_res["mixed"].append(actual_node)
		
		#for finish, we put into the result var the total path length
		final_res["path_length"] = res2
		
		if verbose: pretty_final_res = json.dumps(final_res, indent=4, sort_keys=True)
		if verbose: logger.info("Dijkstra result: \n" + pretty_final_res)
		if verbose: print("Dijkstra result: \n" + pretty_final_res)
	
	
	end = time.time()
	print("Execution time: " + str(end - start))
	logger.info("Execution time: " + str(end - start))
	
	return final_res
