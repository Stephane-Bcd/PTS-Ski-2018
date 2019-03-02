from .classes import VertexRaw, EdgeRaw, Vertex, Edge


def parse_vertex_file(filename: str):
    vertices = {}

    with open(filename) as vf:
        for line in vf:
            vertex = line.rstrip('\n').split(',')

            vertices[vertex[0]] = VertexRaw(int(vertex[0]), vertex[1], int(vertex[2]))

    return vertices


def parse_edge_file(filename: str):
    edges = {}

    with open(filename) as ef:
        for line in ef:
            edge = line.rstrip('\n').split(',')

            edges[edge[0]] = EdgeRaw(int(edge[0]), edge[1], edge[2], int(edge[3]), int(edge[4]))

    return edges


def get_vertices_and_edges(vertex_filename: str = './vertices.txt', edge_filename: str = './edges.txt'):
    vertices_raw = parse_vertex_file(vertex_filename)
    edges_raw = parse_edge_file(edge_filename)

    vertices = {vertex_raw.vertex_id: Vertex(vertex_raw.vertex_id, vertex_raw.name, vertex_raw.altitude, {}, {})
                for vertex_raw in vertices_raw.values()}
    edges = {edge_raw.edge_id: Edge(edge_raw.edge_id, edge_raw.name, edge_raw.edge_type,
                                    vertices[edge_raw.src], vertices[edge_raw.dest]) for edge_raw in edges_raw.values()}

    predecessors_dict, successors_dict = get_vertices_dictionaries(edges_raw)

    for vertex_id, predecessors in predecessors_dict.items():
        vertices[vertex_id].predecessors = predecessors

    for vertex_id, successors in successors_dict.items():
        vertices[vertex_id].successors = successors

    return vertices, edges


def get_vertices_dictionaries(edges_raw):
    predecessors = {}
    successors = {}

    for edge_raw in edges_raw.values():
        if edge_raw.dest not in predecessors:
            predecessors[edge_raw.dest] = {}

        if edge_raw.src not in successors:
            successors[edge_raw.src] = {}

        if edge_raw.src not in predecessors[edge_raw.dest]:
            predecessors[edge_raw.dest][edge_raw.src] = {}

        if edge_raw.dest not in successors[edge_raw.src]:
            successors[edge_raw.src][edge_raw.dest] = {}

        if edge_raw.edge_type not in predecessors[edge_raw.dest][edge_raw.src]:
            predecessors[edge_raw.dest][edge_raw.src][edge_raw.edge_type] = set()

        if edge_raw.edge_type not in successors[edge_raw.src][edge_raw.dest]:
            successors[edge_raw.src][edge_raw.dest][edge_raw.edge_type] = set()

        predecessors[edge_raw.dest][edge_raw.src][edge_raw.edge_type].add(edge_raw.edge_id)

        successors[edge_raw.src][edge_raw.dest][edge_raw.edge_type].add(edge_raw.edge_id)

    return predecessors, successors
