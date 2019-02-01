import SkiProgram
import LogsService
import random
import os

logger = LogsService.initialise_logs("Test file", "./Logs.txt")
logger.info ("Test Program started ...")
print ("Test Program started ...")

'''
	===========================================================
	FUNCTION TO GENERATE A CURRENT FLOWS FILE
	It takes max flows and transformes it to a +/-30% new value: the current flow
	===========================================================
'''

def generate_random_current_flows ( seed, graph, output_file_path, verbose = False):
	logger.info ("Starting to generate current flows file in " + ("verbose" if verbose else "not verbose") + " mode ...")
	print ("Starting to generate current flows file in " + ("verbose" if verbose else "not verbose") + " mode ...")
	
	
	if os.path.exists(output_file_path):
		os.remove(output_file_path)
	
	random.seed(seed)
	
	for edge in list(graph.edges(data=True)):
		edge_attributes = edge[2]
		max_flow = edge_attributes['max_flow']
		id = edge_attributes['id']
		
		random_multiplier = float(random.randrange(70, 130))/100.0
		with open(output_file_path, 'a') as the_file:
			the_file.write(str(id) + '\t' + str(500 if max_flow == float("Inf") else (max_flow * random_multiplier) ) + '\n')
		
		the_file.close()
		
	logger.info ("Current flows file generated !")
	print ("Current flows file generated !")
	
'''
	===========================================================
	MAIN TEST EXECUTION SCRIPT

	===========================================================
'''

try:
	#We first insert all Nodes and Edges and calculate all attributes
	SkiProgram.import_nodes_and_edges('./data_arcs.txt', False)

	#Generating simulated current flows data file
	generate_random_current_flows (100, SkiProgram.GraphMain, "./current_flows.txt", False)

	#Importing current flows values
	SkiProgram.import_current_flows("./current_flows.txt", False)

	#Executing Dijkstra algorithm
	source = "arc2000"
	target = "villaroger"
	Dijkstra_result = SkiProgram.Dijkstra (source, target, "normal_weight", False)
	
	print("\n---------------------------------------------------")
	print("Instructions to go from " + source + " to " + target + "\n\n")
	
	first_Node = True
	first_Edge = True
	for element in Dijkstra_result["mixed"]:
		if element["object_type"] == "node":
			if first_Node:
				print("You're actually located at " + element["name"] + " station, with a "+ str(element["altitude"]) + "m high altitude.")
			else:
				print("Then you will arrive at " + element["name"] + " station, with a "+ str(element["altitude"]) + "m high altitude.")
			first_Node = False
		else:
			if first_Edge:
				print("In order to go to your destination, go first through " + element["name"] + " path of " + element["type"] + " type.")
			print("It will take you  " + str(element["normal_weight"]) + " seconds to go to the next station.\n")
	
	print ("Total travel duration: " + str(Dijkstra_result["path_length"]) + " seconds ! Enjoy !")

	logger.info ("Test Program stopped without problem ! :)")
	print ("Test Program stopped without problem ! :)")
	
except Exception as e:
	print(e)
	logger.info (e)
