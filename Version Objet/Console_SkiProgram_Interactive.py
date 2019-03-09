import Program_Ski_Libraries.SkiProgram as SkiProgram
import Program_Ski_Libraries.LogsService as LogsService
import Program_Ski_Libraries.mockers as mockers
import Program_Ski_Libraries.ConsoleService as cs
import json
import networkx as nx
import os



	
	

# Displaying header
logger = LogsService.initialise_logs("Ski Program Interactive (Console): TEST", "./Input_Or_Generated_Files/Logs.txt")

logger.info ("Console interactive program started ...")
print ("Console interactive program started ...")

header_message = "===========================================================================\n"
header_message += " CONSOLE INTERACTIVE SKI PROGRAM\n"
header_message += " Copyright 2019 Stephane BOUCAUD, Pierrick PUJOL, Simon GILBERT\n\n"
header_message += " This is an interactive program. Use your keyboard to select options.\n"
header_message += "===========================================================================\n\n"

logger.info (header_message)
print (header_message)



# Boolean variable used to exit the program
bool_exit = False

# Path to graph data file
graph_file_path = './Input_Or_Generated_Files/data_arcs.txt'
flows_file_path = "./Input_Or_Generated_Files/current_flows.txt"

try:
	if not os.path.exists(flows_file_path):
		print (flows_file_path + " file doesn't exist !")
		quit()
	
	#Creating and initialising graph with files data
	graph = SkiProgram.load_all_graph_input_data(graph_file_path, flows_file_path, "Main Graph")
	
	#Index Nodes and Edges for next steps
	index_nodes_name_to_key = SkiProgram.index_nodes_by_name (graph)
	index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (graph)
	
	#Start of the interactive program
	while not bool_exit:
		
		#Select the from ant to stations
		selection_introduction_msg = "----------------------------------\n"
		selection_introduction_msg += "In order to calculate a path, you will have to select a departure and a destination site.\n\n"
		print (selection_introduction_msg)
		
		_from = cs.ask_which_station_choose(graph, "Select one of the following departure site")
		_to = cs.ask_which_station_choose(graph, "Select one of the following destination site")
		
		#popose to filter on difficulty
		want_filter_difficulty = cs.ask_yes_no_question("Do you want to filter on Difficulty ? (Example: N,R)")
		filter_difficulty = []
		if want_filter_difficulty:
			filter_difficulty = cs.ask_for_list("Write the difficulties that you don't want (possible values: N for Black, R for Red, B for Blue)")
		
		#Desired path to go from point A or B (Shortest, Fun, Not overcrowded)
		list_choices_desired_path = [
			"1. Shortest path (fast and furious!)",
			"2. Favorising descents (more fun!)",
			"3. Favorising less congested path (less waiting!)",
			"4. Favorising less congested path and favorising descents"
		]
		
		choice_desired_path = cs.ask_option_from_choice_list(list_choices_desired_path, "What kind of path would you prefer to go through?")
		
		list_corresponding_weights = [
			"normal_weight",
			"most_interesting_path_weight",
			"less_congested_path_weight",
			"most_interesting_and_less_congested_path_weight"
		]
		
		#Depending on the choice of the user we will use the corresponding weight
		if choice_desired_path == 1:
			selected_weight = list_corresponding_weights[0]
		elif choice_desired_path == 2:
			selected_weight = list_corresponding_weights[1]
		elif choice_desired_path == 3:
			selected_weight = list_corresponding_weights[2]
		elif choice_desired_path == 4:
			selected_weight = list_corresponding_weights[3]
		else:
			selected_weight = list_corresponding_weights[0]
		
		
		#Executing Dijkstra Algorithm
		
		res_Dijkstra = SkiProgram.Dijkstra (graph, _from, _to, selected_weight, index_nodes_name_to_key, index_edges_2dkey_to_object, filter_difficulty)
		print(SkiProgram.shortest_path_result_into_text(res_Dijkstra))
		
		
		#Ask if want to quit (because if not we can retry)
		bool_exit = cs.ask_yes_no_question("Exit program?")
	

	print ("Console interactive program stopped without problem ! :)")
	logger.info ("Console interactive program stopped without problem ! :)")
	
except Exception as e:
	print(e)
	logger.info (e)
