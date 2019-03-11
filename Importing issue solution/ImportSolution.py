import os
import sys

def get_absolute_path_of_current_project(root_folder_name = "PTS-Ski-2018"):
	'''
		FUNCTION TO FIND THE ABSOLUTE PATH OF THE PROJETS ROOT FOLDER
		root_folder_name: name of the folder containing the project
		returns absolute path of the projects root folder 
	'''
	actual_path = os.path.abspath(__file__)
	substr_index = actual_path.rfind(root_folder_name)
	return actual_path[:substr_index+len(root_folder_name)]
	
def get_recursive_directories_paths(main_directory, folder_names_ignored):
	'''
		FUNCTION TO FIND RECURSIVELY ALL THE PATHS OF FOLDERS IN A SPECIFIED DIRECTORY
		main_directory: path of the directory in which we want to perform the search
		returns a list of paths to all the contained folders
	'''
	os.chdir(main_directory)
	list_current_files_and_directories = os.listdir(main_directory)
	list_current_current_folders_paths = []
	
	for elem in list_current_files_and_directories:
		elem_abs_path = os.path.abspath(elem)
		if os.path.isdir(elem) and elem not in folder_names_ignored:
			list_current_current_folders_paths.append(elem_abs_path)
			list_current_current_folders_paths += get_recursive_directories_paths(elem_abs_path, folder_names_ignored)
			os.chdir(main_directory)
	
	return list_current_current_folders_paths

def add_list_paths_in_python_path(list, verbose=False):
	'''
		FUNCTION TO ADD ABOLUTE PATHS IN PYTHONPATH LIST
		list: list of absolue paths to add
	'''
	
	if verbose: 
		print( "The following paths are added in python path:" )
		for elem in PATHS_TO_ADD_IN_PYTHONPATH:
			print (elem)
	
	for path in list:
		sys.path.append(path)
	
	if verbose:
		print("\nHere is the result python path:")
		for elem in sys.path:
			print (elem)


# list of folder names to ignore
IGNORED_FOLDERS = [
	".git",
	"__pycache__",
	"Dijkstra", 
	"poc",
	"Recherches",
	"Input_Or_Generated_Files",
	"Old"
]

# gathering all project paths informations
PROJECT_ROOT_FOLDER_NAME = "PTS-Ski-2018"
PROJECT_ROOT_FOLDER_ABSOLUTE_PATH = get_absolute_path_of_current_project(PROJECT_ROOT_FOLDER_NAME)
PATHS_TO_ADD_IN_PYTHONPATH = get_recursive_directories_paths(PROJECT_ROOT_FOLDER_ABSOLUTE_PATH, IGNORED_FOLDERS)

#adding project paths to PYTHONPATH
add_list_paths_in_python_path(PATHS_TO_ADD_IN_PYTHONPATH)

#import example
from Program_Ski_Libraries import SkiProgram
from Test_lib import sub

#If the prompt message is displayed, that means that the import is successful
sub.prompt_message()




