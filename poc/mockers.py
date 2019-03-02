from random import randint, choice
from time import time


def write_graph(vertex_count: int = 37, edge_count: int = 95, filename: str = './graph_{}_{}_{}.txt'):
    vertices, edges = generate_graph(vertex_count, edge_count)

    with open(filename.format(vertex_count, edge_count, int(time())), 'x') as gf:
        gf.write('{}\n'.format(vertex_count))

        for vertex in vertices.values():
            gf.write('{}\t{}\t{}\n'.format(vertex[0], vertex[1], vertex[2]))

        gf.write('{}\n'.format(edge_count))

        for edge in edges.values():
            gf.write('{}\t{}\t{}\t{}\t{}\n'.format(edge[0], edge[1], edge[2], edge[3], edge[4]))


def generate_graph(vertex_count: int, edge_count: int):
    vertices = {vertex_id: generate_vertex(vertex_id) for vertex_id in range(1, vertex_count + 1)}
    edges = {}

    for edge_id in range(1, edge_count + 1):
        while True:
            vertex_1_id = randint(1, vertex_count)
            vertex_2_id = randint(1, vertex_count)

            if vertex_1_id != vertex_2_id and vertices[vertex_1_id][2] != vertices[vertex_2_id][2]:
                break

        edges[edge_id] = generate_edge(edge_id, vertex_1_id, vertex_2_id,
                                       vertex_1_altitude=vertices[vertex_1_id][2],
                                       vertex_2_altitude=vertices[vertex_2_id][2])

    return vertices, edges


def generate_vertex(vertex_id: int):
    return vertex_id, 'vertex{}'.format(vertex_id), randint(0, 8848)


def generate_edge(edge_id: int, vertex_1_id: int, vertex_2_id: int, vertex_1_altitude: int, vertex_2_altitude: int):
    tracks = ['V', 'B', 'R', 'N', 'KL', 'SURF']
    lifts = ['TPH', 'TC', 'TSD', 'TS', 'TK']

    edge_type = choice(tracks) if vertex_1_altitude > vertex_2_altitude else choice(lifts)

    return edge_id, 'edge{}'.format(edge_id), edge_type, vertex_1_id, vertex_2_id
