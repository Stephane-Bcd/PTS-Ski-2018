# to solve the problem of tabulation and space in python: :
# notepad++ -> Edition -> traitement des espacements -> transformer les tabulations en espaces


from django import forms
from .models import choice_to_filter_difficulty
from .models import choice_kind_of_path

class userChoiceGraphForm(forms.Form):
   
    startingPoint = forms.IntegerField(min_value=0, label="Enter your starting point:")
    arrivalPoint = forms.IntegerField(min_value=0, label="Enter your point of arrival:")
    kindPath = forms.ChoiceField(choices=choice_kind_of_path.SET_OF_CHOICES, label="What kind of path would you prefer to go through?")
    filterDifficulty = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False, choices=choice_to_filter_difficulty.SET_OF_CHOICES, label="Do you want to filter on Difficulty ? Tick the difficulties that you don't want")
