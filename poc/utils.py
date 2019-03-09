from random import random

from .classes import Flow

'''
Before anything, write comments for each function/class of following files:
 - utils.py
 - parsers.py
 - mockers.py
 - classes.py
'''

'''
	Already implemented in SkiProgram.py (search_coef_favorise_descents function)
	and doesn't need to be integrated
	min_lift_time/max_track_time - 1/float('inf')
	|___ Why -1 and why divide by infinite ??
'''
def get_longest_track_shortest_lift_coef(edges):
    max_track_time = 0.0
    min_lift_time = float('inf')

    for edge in edges.values():
        weight = edge.get_weight()

        if edge.is_lift():
            if weight < min_lift_time:
                min_lift_time = weight
            else:
                continue
        else:
            if weight > max_track_time:
                max_track_time = weight
            else:
                continue

    return min_lift_time/max_track_time - 1/float('inf')

'''
	Integrated in SkiProgram/compute_less_flow_weight function
'''
def get_mean_waiting_time(flow: Flow):
    departure_interval = 1 / flow
    arrival_interval = random() * departure_interval
    queue_length = arrival_interval / departure_interval

    return queue_length / (departure_interval * (1 - queue_length))
