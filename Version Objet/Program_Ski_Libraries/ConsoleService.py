
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
		line_new = '%50s  %50s  %50s' % (list_choices[iteration], list_choices[iteration+1], list_choices[iteration+2])
		print (line_new)
		iteration += 3
	if len(list_choices) % 3 != 0:
		difference = len(list_choices) - iteration
		line_new = '%50s  %50s  %50s' % (  
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
