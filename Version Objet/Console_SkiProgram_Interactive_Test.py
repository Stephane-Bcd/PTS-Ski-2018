import Program_Ski_Libraries.SkiProgram as SkiProgram
import Program_Ski_Libraries.LogsService as LogsService
import Program_Ski_Libraries.mockers as mockers
import json
import networkx as nx
import os


def format_yes_no_response(response):
	'''
	=========================================================
	FUNCTION TO TRANSFORM YES NO STRING RESPONSE TO BOOLEAN
	response: yes/no response (string)
	returns: boolean True for yes, False for no
	=========================================================
	'''

	if response == "y" or response == "yes" or response == "o" or response == "oui":
		return True
	elif response == "n" or response == "no" or response == "n" or response == "non":
		return False
	else:
		return False


def ask_yes_no_question(question):
	'''
	=========================================================
	FUNCTION TO ASK A YES NO QUESTION, RETURNING A BOOLEAN
	question: asked question on the console
	returns: boolean True for yes, False for no
	=========================================================
	'''
	
	print ("----------------------------------\n")
	response = input(question + "\n\nResponse?(y/n)\n")
	response = format_yes_no_response(response)
	return response


def ask_which_station_choose(graph, question):
	'''
	=========================================================
	FUNCTION TO ASK FOR A SITE SELECTION
	question: asked question on the console
	graph: graph used to list the sites on the console
	returns: integer entered by the user (networkx id of the station)
	=========================================================
	'''
	
	
	print ("----------------------------------\n")
	print (question + ":\n\n")
	
	iteration = 1
	last_choices_check = False
	current_3_choices_list = ['','','']
	
	for node in graph.nodes(data=True):
		
		current_3_choices_list[iteration-1] = str(node[0]) + ". " + node[1]["node_name"]
		
		if iteration % 3 == 0:
			current_3_choices_str = '%30s  %30s  %30s' % (current_3_choices_list[0], current_3_choices_list[1], current_3_choices_list[2])
			print (current_3_choices_str)
			iteration = 1
			last_choices_check = True
			current_3_choices_list = ['','','']
		else:
			iteration += 1
			last_choices_check = False
			
	if not last_choices_check:
		current_3_choices_str = '%30s  %30s  %30s' % (current_3_choices_list[0], current_3_choices_list[1], current_3_choices_list[2])
		print (current_3_choices_str)
		
	response = input("\nResponse? (number)\n")
	return int(response)
	

def ask_option_from_choice_list(list_choices, question):
	'''
	=========================================================
	FUNCTION TO ASK FOR AN OPTION USING A LIST OF OPTIONS
	list_choices: List describing the options that can be chosen
	question: Question describing the options
	returns: integer entered by the user corresponding to the question
	=========================================================
	'''
	
	
	print ("----------------------------------\n")
	print (question + ":\n\n")
	
	iteration = 0
	
	while iteration+2 < len(list_choices):
		line_new = '%40s  %40s  %40s' % (list_choices[iteration], list_choices[iteration+1], list_choices[iteration+2])
		print (line_new)
		iteration += 3
	if len(list_choices) % 3 != 0:
		difference = len(list_choices) - iteration
		line_new = '%40s  %40s  %40s' % (  
			list_choices[iteration] if difference >= 1 else '', 
			list_choices[iteration+1] if difference >= 2 else '', 
			''
		)
		print (line_new)
		
	response = input("\nResponse? (number)\n")
	return int(response)
			

def ask_for_integer(question):
	'''
	=========================================================
	FUNCTION TO ASK FOR AN INTEGER
	question: Question describing the asked integer
	returns: integer entered by the user corresponding to the question
	=========================================================
	'''
	
	print ("----------------------------------\n")
	print (question + ":\n\n")
	
	response = input("\nResponse? (number)\n")
	return int(response)
	

def ask_for_string(question):
	'''
	=========================================================
	FUNCTION TO ASK FOR A STRING
	question: Question describing the asked string
	returns: string entered by the user corresponding to the question
	=========================================================
	'''
	
	print ("----------------------------------\n")
	print (question + ":\n\n")
	
	response = input("\nResponse? (text)\n")
	return response
	

def ask_for_list(question):
	'''
	=========================================================
	FUNCTION TO ASK FOR A LIST OF THNGS
	question: Question describing the asked string
	returns: list of strings entered by the user corresponding to the different selected informations
	=========================================================
	'''
	
	print ("----------------------------------\n")
	print ("For this question, answer with a list of choices separated with comas.\n")
	print (question + ":\n\n")
	
	response = input("\nResponse? (choices separated with comas ',')\n")
	return response.split(",")
	
	

# Displaying header
logger = LogsService.initialise_logs("Ski Program Interactive (Console): TEST", "./Input_Or_Generated_Files/Logs.txt")

logger.info ("Console interactive test program started ...")
print ("Console interactive test program started ...")

header_message = "===========================================================================\n"
header_message += " CONSOLE INTERACTIVE SKI TEST PROGRAM\n"
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

#verbose defines if we want or not to prompt all data on terminal and in logs file
verbose = False

try:
	
	#Ask if we need a verbose mode for this test
	verbose = ask_yes_no_question("Do you need a verbose mode for this test?")
	
	#Ask if want to generate a new graph
	choices_list = ["1.Use existing graph",
		"2. Generate new random graph"
	]
	choice_graph = ask_option_from_choice_list(choices_list, "Which kind of graph would you like to use?")
	
	#If we want to use existing graph
	if choice_graph == 1:
		choices_list_graph_path = ["1.Use default graph file path: "+graph_file_path,
			"2. Use custom graph file path"
		]
		choice_graph = ask_option_from_choice_list(choices_list_graph_path, "Which kind of graph would you like to use?")
		
		#If we want to use a custom graph file (type the path)
		if choice_graph == 2:
			graph_file_path = ask_for_string("Enter the path to the file containing graph data")
			
			
	#If we want to generate a graph
	else:
		graph_file_path = './Input_Or_Generated_Files/data_arcs_generated.txt'
		_vertex_nb = 50
		_edges_nb = 200
		
		_vertex_nb = ask_for_integer("Enter a number of vertex")
		_edges_nb = ask_for_integer("Enter a number of edges")

		mockers.write_graph(_vertex_nb,_edges_nb, graph_file_path)
	
	want_gen_flows = ask_yes_no_question("Do you want to generate a random Flows file ?")
	if not want_gen_flows and not os.path.exists(flows_file_path):
		print (flows_file_path + " file doesn't exist !")
		quit()
	
	#Creating and initialising graph with files data
	graph = SkiProgram.load_all_graph_input_data(graph_file_path, flows_file_path, "Main Graph", verbose, want_gen_flows, 100)
	
	#Index Nodes and Edges for next steps
	index_nodes_name_to_key = SkiProgram.index_nodes_by_name (graph, verbose)
	index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (graph, verbose)
	
	#Start of the interactive program
	while not bool_exit:
		
		#Select the from ant to stations
		selection_introduction_msg = "----------------------------------\n"
		selection_introduction_msg += "In order to calculate a path, you will have to select a departure and a destination site.\n\n"
		print (selection_introduction_msg)
		
		_from = ask_which_station_choose(graph, "Select one of the following departure site")
		_to = ask_which_station_choose(graph, "Select one of the following destination site")
		
		#popose to filter on difficulty
		want_filter_difficulty = ask_yes_no_question("Do you want to filter on Difficulty ? (Example: N,R)")
		filter_difficulty = []
		if want_filter_difficulty:
			filter_difficulty = ask_for_list("Write the difficulties that you don't want (possible values: N for Black, R for Red, B for Blue)")
		
		#Desired path to go from point A or B (Shortest, Fun, Not overcrowded)
		list_choices_desired_path = [
			"1. Shortest path (fast and furious!)",
			"2. Favorising descents (more fun!)",
			"3. Favorising less congested path (less waiting!)"
		]
		
		choice_desired_path = ask_option_from_choice_list(list_choices_desired_path, "What kind of path would you prefer to go through?")
		
		list_corresponding_weights = [
			"normal_weight",
			"most_interesting_path_weight",
			"less_congested_path_weight"
		]
		
		#Depending on the choice of the user we will use the corresponding weight
		if choice_desired_path == 1:
			selected_weight = list_corresponding_weights[0]
		elif choice_desired_path == 2:
			selected_weight = list_corresponding_weights[1]
		elif choice_desired_path == 3:
			selected_weight = list_corresponding_weights[2]
		else:
			selected_weight = list_corresponding_weights[0]
		
		
		#Executing Dijkstra Algorithm
		
		res_Dijkstra = SkiProgram.Dijkstra (graph, _from, _to, selected_weight, index_nodes_name_to_key, index_edges_2dkey_to_object, filter_difficulty, verbose)
		print(SkiProgram.shortest_path_result_into_text(res_Dijkstra))
		
		
		#Ask if want to quit (because if not we can retry)
		bool_exit = ask_yes_no_question("Exit program?")
	

	print ("Console interactive test program stopped without problem ! :)")
	logger.info ("Console interactive test program stopped without problem ! :)")
	
except Exception as e:
	print(e)
	logger.info (e)
