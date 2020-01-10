from enum import Enum


class DirectionEnum(Enum):
    UP = 0
    DOWN = 1
    UNDIRECTED = 2


class NodeStatus(Enum):
    UNVISITED = 0
    VISITING = 1
    PRUNED = 2
    MINIMUM_LOCAL = 3


class EdgeStatus(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class Node:
    def __init__(self, node_id, label, cost, x, y, minimum=False):
        self.node_id = node_id
        self.label = label
        self.cost = cost
        self.minimum = minimum
        self.visit_status:NodeStatus = NodeStatus.UNVISITED
        self.x = x
        self.y = y

    def set_unvisited(self):
        self.visit_status = NodeStatus.UNVISITED

    def set_visiting(self):
        self.visit_status = NodeStatus.VISITING

    def set_pruned(self):
        self.visit_status = NodeStatus.PRUNED

    def set_minimum_local(self):
        self.visit_status = NodeStatus.MINIMUM_LOCAL

    def is_unvisited(self):
        return self.visit_status == NodeStatus.UNVISITED

    def is_visiting(self):
        return self.visit_status == NodeStatus.VISITING

    def is_pruned(self):
        return self.visit_status == NodeStatus.PRUNED

    def is_minimum_local(self):
        return self.visit_status == NodeStatus.MINIMUM_LOCAL

    def is_minimum_global(self):
        return self.minimum


class Edge:
    def __init__(self, orig, dest, visit_status:EdgeStatus=EdgeStatus.UNVISITED):
        self.orig = orig
        self.dest = dest
        self.direction = DirectionEnum.UNDIRECTED
        self.visit_status = visit_status

    def set_unvisited(self):
        self.visit_status = EdgeStatus.UNVISITED

    def set_visiting(self):
        self.visit_status = EdgeStatus.VISITING

    def set_visited(self):
        self.visit_status = EdgeStatus.VISITED

    def is_unvisited(self):
        return self.visit_status == EdgeStatus.UNVISITED

    def is_visiting(self):
        return self.visit_status == EdgeStatus.VISITING

    def is_visited(self):
        return self.visit_status == EdgeStatus.VISITED

    def set_direction_up(self):
        self.direction = DirectionEnum.UP

    def set_direction_down(self):
        self.direction = DirectionEnum.DOWN

    def set_undirected(self):
        self.direction = DirectionEnum.UNDIRECTED

    def is_direction_up(self):
        return self.direction == DirectionEnum.UP

    def is_direction_down(self):
        return self.direction == DirectionEnum.DOWN

    def is_undirected(self):
        return self.direction == DirectionEnum.UNDIRECTED


class Graph:
    def __init__(self):
        self.nodes = list()
        self.edges = dict() # par de tuplas

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, orig, dest):
        if (orig, dest) not in self.edges:
            self.edges[(orig, dest)] = Edge(orig, dest)

    def reset(self):
        for n in self.nodes:
            if n.is_visiting() or n.is_minimum_local():
                n.set_pruned()

        for e in self.edges.values():
            if e.is_visiting():
                e.set_visited()
                e.set_undirected()

    def get_edge(self, orig:Node, dest:Node):
        k = (orig, dest)
        if k in self.edges:
            return self.edges[k]
        k = (dest, orig)
        if k in self.edges:
            return self.edges[k]
        raise Exception('Edge not found')

    def get_edges(self):
        return self.edges.values()