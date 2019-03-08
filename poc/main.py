# from poc.mockers import write_graph
from parsers import get_vertices_and_edges
from utils import get_longest_track_shortest_lift_coef, get_mean_waiting_time
from classes import Flow


# write_graph()

vertices, edges = get_vertices_and_edges(vertex_filename='./poc/vertices.txt', edge_filename='./poc/edges.txt')

longest_track_shortest_lift_coef = get_longest_track_shortest_lift_coef(edges)

weights = {edge.edge_id: edge.get_weight() for edge in edges.values()}

adjusted_weights = {}

for edge in edges.values():
    bias = get_mean_waiting_time(Flow[edge.edge_type]) if edge.is_lift() else longest_track_shortest_lift_coef

    adjusted_weights[edge.edge_id] = edge.get_adjusted_weight(bias)

print('# Vertices #\n{}\n# Edges #\n{}'.format(vertices, edges))

print('# Weights #\n{}'.format(weights))

print('# Adjusted weights #\n{}'.format(adjusted_weights))
