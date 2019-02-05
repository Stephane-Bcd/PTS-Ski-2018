import SkiProgram
import LogsService
import json

logger = LogsService.initialise_logs("Test file", "./Logs.txt")
logger.info ("Test Program started ...")
print ("Test Program started ...")


'''
	===========================================================
	MAIN TEST EXECUTION SCRIPT

	===========================================================
'''

try:
	
	
	#Creating and initialising graph with files data
	graph = SkiProgram.load_all_graph_input_data('./data_arcs.txt', "./current_flows.txt", "Main Graph")
	
	#Index Nodes and Edges for next steps
	index_nodes_name_to_key = {}
	index_edges_2dkey_to_object = {}
	
	index_nodes_name_to_key = SkiProgram.index_nodes_by_name (index_nodes_name_to_key, graph, False)
	index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (index_edges_2dkey_to_object, graph, False)
	
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
	
	#Executing Dijkstra algorithm
	source = "arc2000"
	target = "villaroger"
	
	res_Dijkstra = SkiProgram.Dijkstra (graph, source, target, "normal_weight", index_nodes_name_to_key, index_edges_2dkey_to_object, False)
	#print(json.dumps(res_Dijkstra, indent=4, sort_keys=True))
	
	print(SkiProgram.shortest_path_result_into_text(res_Dijkstra))
	
	
	

	print ("Test Program stopped without problem ! :)")
	logger.info ("Test Program stopped without problem ! :)")
	
except Exception as e:
	print(e)
	logger.info (e)
