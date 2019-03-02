from random import random

from .classes import Flow


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


def get_mean_waiting_time(flow: Flow):
    departure_interval = 1 / flow
    arrival_interval = random() * departure_interval
    queue_length = arrival_interval / departure_interval

    return queue_length / (departure_interval * (1 - queue_length))
