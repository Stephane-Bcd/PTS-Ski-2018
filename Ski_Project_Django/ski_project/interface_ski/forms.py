# to solve the problem of tabulation and space in python: :
# notepad++ -> Edition -> traitement des espacements -> transformer les tabulations en espaces


from django import forms
#to import our classes that allow users to make their choice
from .models import choice_to_filter_difficulty
from .models import choice_kind_of_path

# class that generates a form
class userChoiceGraphForm(forms.Form):

    # part of the form that allows the user to choose his point of departure
    startingPoint = forms.IntegerField(min_value=0, label="Enter your starting point:")
	# part of the form that allows the user to choose his point of arrival
    arrivalPoint = forms.IntegerField(min_value=0, label="Enter your point of arrival:")
	# part of the form that allows the user to choose his type of path
    kindPath = forms.ChoiceField(choices=choice_kind_of_path.SET_OF_CHOICES, label="What kind of path would you prefer to go through?")
	# part of the form that allows the user to choose the difficulties he wants to filter
    filterDifficulty = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False, choices=choice_to_filter_difficulty.SET_OF_CHOICES, label="Do you want to filter on Difficulty ? Tick the difficulties that you don't want")
    
	# Exemple to add a radio button :
	#choiceSourceGraph = forms.ChoiceField(choices=choice_source_graph.SET_OF_CHOICES, widget=forms.RadioSelect, label="Do you want to import a graph file or generate one automatically?")
