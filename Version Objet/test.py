from Program_Ski_Libraries import SkiProgram as SkiProgram
from Program_Ski_Libraries import LogsService as LogsService
from Program_Ski_Libraries import mockers as mockers
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
	
#Creating and initialising graph with files data
graph = SkiProgram.load_all_graph_input_data('./Input_Or_Generated_Files/data_arcs.txt', "./Input_Or_Generated_Files/current_flows.txt", "Main Graph", False)


#Index Nodes and Edges for next steps

index_nodes_name_to_key = SkiProgram.index_nodes_by_name (graph, False)
index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (graph, False)

#Displaying final graph
#SkiProgram.display_graph_console(graph)



#S/T
source = 7
target = 1

#User choices
filter = True
needs_max_flows = True
needs_shortest_path = True
filter_list = [ "N", "R"]

#filter (if needed)
if filter:
	filtered_graph = SkiProgram.get_filtered_graph_on_edge_type(graph,filter_list , False)

	#Index Nodes and Edges for next steps
	filtered_index_nodes_name_to_key = SkiProgram.index_nodes_by_name (filtered_graph, False)
	filtered_index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (filtered_graph, False)

	used_index_nodes_name_to_key = filtered_index_nodes_name_to_key
	used_index_edges_2dkey_to_object = filtered_index_edges_2dkey_to_object
	used_graph = filtered_graph
else:
	used_index_nodes_name_to_key = index_nodes_name_to_key
	used_index_edges_2dkey_to_object = index_edges_2dkey_to_object
	used_graph = graph

#if want to execute a shortest path algorithm
if needs_shortest_path:
	res_Dijkstra = SkiProgram.Dijkstra (used_graph, source, target, "normal_weight", used_index_nodes_name_to_key, used_index_edges_2dkey_to_object, False)


#if want to execute a max flow algorithm
if needs_max_flows:
	flows_graph = SkiProgram.transform_multidigraph_to_digraph(used_graph, used_index_edges_2dkey_to_object, False)
	result_Max_Flow = SkiProgram.Max_Flow (flows_graph, source, target, used_index_nodes_name_to_key, used_index_edges_2dkey_to_object, False)






print ("Test Program stopped without problem ! :)")
logger.info ("Test Program stopped without problem ! :)")


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


	
	
	
	
	