from datetime import datetime
from django.shortcuts import render
from .forms import ContactForm

def date_actuelle(request):
    return render(request, 'interface_ski/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'interface_ski/addition.html', locals())
	
	
def graph(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        point_depart = form.cleaned_data['pointDepart']
        point_arrive = form.cleaned_data['pointArrive']
 
        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'interface_ski/printGraph.html', locals())