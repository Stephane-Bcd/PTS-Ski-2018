from django import forms

class ContactForm(forms.Form):
    pointDepart = forms.CharField(max_length=10,label="Saisissez votre point de départ (valeur numérique) :")
    pointArrive = forms.CharField(max_length=10,label="Saisissez votre point d'arrivée (valeur numérique) :")
    #envoyeur = forms.EmailField(label="Votre adresse e-mail")
    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)