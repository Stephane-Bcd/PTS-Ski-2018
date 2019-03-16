import os
import sys

from django.shortcuts import render
# import of our form of choice, concerning the data to be entered by the user to operate our Ski library
from .forms import userChoiceGraphForm
# Import which allows to be sure that our libraries will be found
from .ImportSolution import *

# gathering all project paths informations
PROJECT_ROOT_FOLDER_NAME = "PTS-Ski-2018"
PROJECT_ROOT_FOLDER_ABSOLUTE_PATH = get_absolute_path_of_current_project(PROJECT_ROOT_FOLDER_NAME)
PATHS_TO_ADD_IN_PYTHONPATH = get_recursive_directories_paths(PROJECT_ROOT_FOLDER_ABSOLUTE_PATH, IGNORED_FOLDERS)

# adding project paths to PYTHONPATH
add_list_paths_in_python_path(PATHS_TO_ADD_IN_PYTHONPATH)

# allows to import our SkiProgram
from Program_Ski_Libraries import SkiProgram
   
def graph(request):

    # Build the form, either with the data posted, empty if the user first accesses the page.
    form = userChoiceGraphForm(request.POST or None)
    
    # We verify that the data sent is valid. This method returns False if there are no data in the form or it contains errors.
    if form.is_valid(): 
        # Here we can process the form data
        
        # Retrieving the values transmitted by the form
        starting_point = form.cleaned_data['startingPoint']
        arrival_point = form.cleaned_data['arrivalPoint']
        kind_path = form.cleaned_data['kindPath']
        filter_difficulty = form.cleaned_data['filterDifficulty']
        
        ############ INTEGRATION OF THE DIJKSTRA PROGRAM #########################################
             
        # Path to graph data file
        graph_file_path = './Version Objet/Input_Or_Generated_Files/data_arcs.txt'
        flows_file_path = "./Version Objet/Input_Or_Generated_Files/current_flows.txt"
    
	    # It allows to create our graph
        graph = SkiProgram.load_all_graph_input_data(graph_file_path, flows_file_path, "Main Graph", False, False, 100)
        
        #Index Nodes and Edges for next steps
        index_nodes_name_to_key = SkiProgram.index_nodes_by_name (graph, False)
        index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (graph, False)
        
        #Executing Dijkstra Algorithm
        res_Dijkstra = SkiProgram.Dijkstra (graph, starting_point, arrival_point, kind_path, index_nodes_name_to_key, index_edges_2dkey_to_object, filter_difficulty, False)
        # allows to have a display of the shortest path easy to understand by a user
        Dijkstra_text_result = SkiProgram.shortest_path_result_into_text(res_Dijkstra).replace('\n','<br />')
        ############ END OF THE INTEGRATION OF THE DIJKSTRA PROGRAM  ################################
 
 
        sent = True
        
    # Whatever happens, we display the page of the form.
    return render(request, 'interface_ski/printGraphCalculation.html', locals())
    
