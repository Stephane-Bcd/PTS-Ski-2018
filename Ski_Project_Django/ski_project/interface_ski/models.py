from django.db import models

# Create your models here.

#class that allows the user to filter the difficulties of the tracks
class choice_to_filter_difficulty(models.Model):

    # Black, Red, Blue are the choices offered to the user
	# N, R, B, are the values sent to the view
    SET_OF_CHOICES = (
        ("N", "Black"),
        ("R", "Red"),
        ("B", "Blue"), 
    )
	
#class that allows the user to choose the difficulties of the tracks to filter
class choice_kind_of_path(models.Model):

    # Shortest path..., Favorising descents..., are the choices offered to the user
	# normal_weight, most_interesting_path_weight..., are the values sent to the view
    SET_OF_CHOICES = (
        ('normal_weight', 'Shortest path (fast and furious!)'),
        ('most_interesting_path_weight', 'Favorising descents (more fun!)'),
        ('less_congested_path_weight', 'Favorising less congested path (less waiting!)'),
        ('most_interesting_and_less_congested_path_weight', 'Favorising less congested path and favorising descents'),
    )
