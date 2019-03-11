from django.db import models

# Create your models here.

class choice_to_filter_difficulty(models.Model):

    SET_OF_CHOICES = (
        ("N", "Black"),
        ("R", "Red"),
        ("B", "Blue"),
    )
	
class choice_kind_of_path(models.Model):

    SET_OF_CHOICES = (
        ('normal_weight', 'Shortest path (fast and furious!)'),
        ('most_interesting_path_weight', 'Favorising descents (more fun!)'),
        ('less_congested_path_weight', 'Favorising less congested path (less waiting!)'),
        ('most_interesting_and_less_congested_path_weight', 'Favorising less congested path and favorising descents'),
    )