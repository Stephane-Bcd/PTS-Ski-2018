import os
import sys

from django.shortcuts import render
from .forms import userChoiceGraphForm
from .ImportSolution import *

# gathering all project paths informations
PROJECT_ROOT_FOLDER_NAME = "PTS-Ski-2018"
PROJECT_ROOT_FOLDER_ABSOLUTE_PATH = get_absolute_path_of_current_project(PROJECT_ROOT_FOLDER_NAME)
PATHS_TO_ADD_IN_PYTHONPATH = get_recursive_directories_paths(PROJECT_ROOT_FOLDER_ABSOLUTE_PATH, IGNORED_FOLDERS)

#adding project paths to PYTHONPATH
add_list_paths_in_python_path(PATHS_TO_ADD_IN_PYTHONPATH)

from Program_Ski_Libraries import SkiProgram
   
def graph(request):

    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = userChoiceGraphForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        starting_point = form.cleaned_data['startingPoint']
        arrival_point = form.cleaned_data['arrivalPoint']
        kind_path = form.cleaned_data['kindPath']
        filter_difficulty = form.cleaned_data['filterDifficulty']
        ############ TEST INTEGRATION DIJKSTRA PROGRAM     ##################################
        
        # Path to graph data file
        graph_file_path = './Input_Or_Generated_Files/data_arcs.txt'
        flows_file_path = "./Input_Or_Generated_Files/current_flows.txt"

        graph = SkiProgram.load_all_graph_input_data(graph_file_path, flows_file_path, "Main Graph", False, False, 100)
        
        #Index Nodes and Edges for next steps
        index_nodes_name_to_key = SkiProgram.index_nodes_by_name (graph, False)
        index_edges_2dkey_to_object = SkiProgram.index_edges_by_2D_key (graph, False)
        
		#Executing Dijkstra Algorithm
        res_Dijkstra = SkiProgram.Dijkstra (graph, starting_point, arrival_point, kind_path, index_nodes_name_to_key, index_edges_2dkey_to_object, filter_difficulty, False)
        Dijkstra_text_result = SkiProgram.shortest_path_result_into_text(res_Dijkstra)
        
        ############ END TEST INTEGRATION DIJKSTRA PROGRAM  ##################################
 
 
        envoi = True
        
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'interface_ski/printGraphCalculation.html', locals())
    
