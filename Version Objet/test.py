import Program_Ski_Libraries.SkiProgram as SkiProgram
import Program_Ski_Libraries.LogsService as LogsService
import Program_Ski_Libraries.mockers as mockers
import json
import networkx as nx

logger = LogsService.initialise_logs("Test file", "./Input_Or_Generated_Files/Logs.txt")
logger.info ("Test Program started ...")
print ("Test Program started ...")


'''
	===========================================================
	MAIN TEST EXECUTION SCRIPT

	===========================================================
'''

try:
	
	
	
	#Creating and initialising graph with files data
	graph = SkiProgram.load_all_graph_input_data('./Input_Or_Generated_Files/data_arcs.txt', "./Input_Or_Generated_Files/current_flows.txt", "Main Graph", True)
	
	#Index Nodes and Edges for next steps
	
	index_nodes_name_to_key = SkiProgram.index_nodes_by_name (graph, False)
	index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (graph, False)
	
	#Displaying final graph
	SkiProgram.display_graph_console(graph)
	
	'''
	#Test Get data
	#Get node by id
	print("Get node by id (2) result:\n"+ str(SkiProgram.get_node_by_id (graph, 2)))
	#Get node by name
	print("Get node by name (\'arc2000\') result:\n"+ str(SkiProgram.get_node_by_name (graph, index_nodes_name_to_key, "arc2000")))
	#Get edge by 3D ID
	print("Get edge by 3d id ([2,1,2]) result:\n"+str(SkiProgram.get_edge_by_3D_id (graph, [2, 1, 2])))
	print("Get edge by 3d id ([2,1,0]) result:\n"+str(SkiProgram.get_edge_by_3D_id (graph, [2, 1, 0])))
	#Get edge(s) by 2D ID
	print("Get edge by 2d id ([2-1]) result:\n"+str(SkiProgram.get_edges_by_2D_id (graph, index_edges_2dkey_to_object, [2,1])))
	'''
	
	'''#Executing Dijkstra algorithm
	source = 7
	target = 1
	
	#dijkstra with filter
	res_Dijkstra = SkiProgram.Dijkstra (graph, source, target, "normal_weight", index_nodes_name_to_key, index_edges_2dkey_to_object, [ "N", "R"], False)
	print(SkiProgram.shortest_path_result_into_text(res_Dijkstra))
	
	#dijkstra without filter
	res_Dijkstra = SkiProgram.Dijkstra (graph, source, target, "normal_weight", index_nodes_name_to_key, index_edges_2dkey_to_object, [], False)
	print(SkiProgram.shortest_path_result_into_text(res_Dijkstra))
	
	#dijkstra with filter and with most interesting path
	source = 1
	target = 37
	res_Dijkstra = SkiProgram.Dijkstra (graph, source, target, "most_interesting_path_weight", index_nodes_name_to_key, index_edges_2dkey_to_object, [ ], False)
	print(SkiProgram.shortest_path_result_into_text(res_Dijkstra))'''
	
	
	
	
	

	print ("Test Program stopped without problem ! :)")
	logger.info ("Test Program stopped without problem ! :)")
	
except Exception as e:
	print(e)
	logger.info (e)
