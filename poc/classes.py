from enum import IntEnum

'''
	Could be interesting to integrate but we prefer to continue other modifications

'''
class Timing:
    @staticmethod
    def v(height_delta: int):
        return 5*height_delta/100

    @staticmethod
    def b(height_delta: int):
        return 4*height_delta/100

    @staticmethod
    def r(height_delta: int):
        return 3*height_delta/100

    @staticmethod
    def n(height_delta: int):
        return 2*height_delta/100

    @staticmethod
    def kl(height_delta: int):
        return 10/60*height_delta/100

    @staticmethod
    def surf(height_delta: int):
        return 10*height_delta/100

    @staticmethod
    def tph(height_delta: int):
        return 4 + 2*height_delta/100

    @staticmethod
    def tc(height_delta: int):
        return 2 + 3*height_delta/100

    @staticmethod
    def tsd(height_delta: int):
        return 1 + 3*height_delta/100

    @staticmethod
    def ts(height_delta: int):
        return 1 + 4*height_delta/100

    @staticmethod
    def tk(height_delta: int):
        return 1 + 4*height_delta/100

    @staticmethod
    def bus(src: str, dest: str):
        if (src == 'arc2000' and dest == 'arc1600') or (src == 'arc1600' and dest == 'arc2000'):
            return 40
        elif (src == 'arc1600' and dest == 'arc1800') or (src == 'arc1800' and dest == 'arc1600'):
            return 30

'''
	Don't know how to use it efficiently in the project
'''

class Flow(IntEnum):
    TPH = 1200
    TC = 2200
    TSD = 2500
    TS = 1800
    TK = 800
    BUS = 300

'''
	All the following Classes are not useful because NetworkX alredy returns some JSON data
'''
class VertexRaw:
    def __init__(self, vertex_id: int, name: str, altitude: int):
        self.vertex_id = vertex_id
        self.name = name
        self.altitude = altitude

    def __repr__(self):
        return 'Vertex(vertex_id={!r}, name={!r}, altitude={!r})'\
            .format(self.vertex_id, self.name, self.altitude)


class EdgeRaw:
    def __init__(self, edge_id: int, name: str, edge_type: str, src: int, dest: int):
        self.edge_id = edge_id
        self.name = name
        self.edge_type = edge_type
        self.src = src
        self.dest = dest

    def __repr__(self):
        return 'Edge(edge_id={!r}, name={!r}, edge_type={!r}, src={!r}, dest={!r})'\
            .format(self.edge_id, self.name, self.edge_type, self.src, self.dest)


class Vertex:
    def __init__(self, vertex_id: int, name: str, altitude: int, predecessors, successors):
        self.vertex_id = vertex_id
        self.name = name
        self.altitude = altitude
        self.predecessors = predecessors
        self.successors = successors

    def __repr__(self):
        return 'Vertex(vertex_id={!r}, name={!r}, altitude={!r}, predecessors={!r}, successors={!r})'\
            .format(self.vertex_id, self.name, self.altitude, self.predecessors, self.successors)


class Edge:
    def __init__(self, edge_id: int, name: str, edge_type: str, src: Vertex, dest: Vertex):
        self.edge_id = edge_id
        self.name = name
        self.edge_type = edge_type
        self.src = src
        self.dest = dest

    def is_bus(self):
        return self.edge_type == 'BUS'

    def is_lift(self):
        return self.edge_type in ['TPH', 'TC', 'TSD', 'TS', 'TK', 'BUS']

    def get_weight(self):
        return (getattr(Timing, self.edge_type.lower())(self.src.name, self.dest.name) if self.is_bus() else
                getattr(Timing, self.edge_type.lower())(abs(self.src.altitude - self.dest.altitude)))

    def get_adjusted_weight(self, bias: float):
        return (self.get_weight() * bias if not self.is_lift() else
                self.get_weight() + bias)

    def __repr__(self):
        return 'Edge(edge_id={!r}, name={!r}, edge_type={!r}, src={!r}, dest={!r})'\
            .format(self.edge_id, self.name, self.edge_type, self.src, self.dest)
