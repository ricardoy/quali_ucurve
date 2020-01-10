from graph.graph import Node, Edge


def get_dot_node(node:Node):
    attributes = dict()

    attributes['shape'] = 'box'
    attributes['xlabel'] = node.cost
    attributes['label'] = node.label

    attributes['pos'] = '{},{}!'.format(node.x, node.y)

    if node.is_visiting():
        attributes['style'] = 'filled'
        attributes['fillcolor'] = 'yellow'

    if node.is_pruned():
        attributes['style'] = 'filled'
        attributes['fillcolor'] = 'red'

    if node.is_minimum_local():
        attributes['style'] = 'filled'
        attributes['fillcolor'] = 'orange'

    if node.is_unvisited() and node.is_minimum_global():
        attributes['style'] = 'filled'
        attributes['fillcolor'] = 'green'

    return '{} [{}]'.format(node.node_id, ','.join(['{}="{}"'.format(x, y) for x, y in attributes.items()]))


def get_dot_edge(edge:Edge):
    orig = edge.orig
    dest = edge.dest
    attributes = dict()

    attributes['splines'] = 'none'

    if edge.is_unvisited():
        attributes['color'] = 'gray'

    if edge.is_visited():
        attributes['color'] = 'gray'

    if edge.is_visiting():
        attributes['color'] = 'black'
        attributes['penwidth'] = 2

    # print(edge.direction)
    if edge.is_undirected():
        attributes['dir'] = 'none'
    elif edge.is_direction_down():
        pass
    elif edge.is_direction_up():
        attributes['dir'] = 'back'
    else:
        raise Exception('Bad direction')

    return '{} -> {} [{}]'.format(orig.node_id, dest.node_id, ','.join(['{}="{}"'.format(x, y) for x, y in attributes.items()]))


def generate_dot_file(graph):
    s = 'digraph D {\n'

    for n in graph.nodes:
        s += get_dot_node(n)
        s += '\n'

    for e in graph.get_edges():
        s += get_dot_edge(e)
        s += '\n'

    s += '}'

    return s