from graph.graph import Node, Graph
from plot.graphviz import generate_dot_file


contador = 0


def output_graph(graph):
    global contador
    filename = '/tmp/{:04d}.dot'.format(contador)
    contador += 1
    with open(filename, 'w') as fh:
        fh.write(generate_dot_file(graph))


def generate_node_and_add_to_graph(node_id, label, cost, x, y, graph):
    n = Node(node_id=node_id, label=label, cost=cost, x=x, y=y*1.6)
    graph.add_node(n)
    return n


def main():
    g = Graph()

    n0000 = generate_node_and_add_to_graph('0000', '0123', 15, 3, 3, g)

    n0110 = generate_node_and_add_to_graph('0110', '03|12', 9, 0, 2, g)
    n0111 = generate_node_and_add_to_graph('0111', '0|123', 7, 1, 2, g)
    n0010 = generate_node_and_add_to_graph('0010', '013|2', 8, 2, 2, g)
    n0101 = generate_node_and_add_to_graph('0101', '02|13', 13, 3, 2, g)
    n0001 = generate_node_and_add_to_graph('0001', '012|3', 9, 4, 2, g)
    n0100 = generate_node_and_add_to_graph('0100', '023|1', 12, 5, 2, g)
    n0011 = generate_node_and_add_to_graph('0011', '01|23', 11, 6, 2, g)

    n0112 = generate_node_and_add_to_graph('0112', '0|12|3', 6, 0.5, 1, g)
    n0120 = generate_node_and_add_to_graph('0120', '03|1|2', 4, 1.5, 1, g)
    n0121 = generate_node_and_add_to_graph('0121', '0|13|2', 6, 2.5, 1, g)
    n0102 = generate_node_and_add_to_graph('0102', '02|1|3', 8, 3.5, 1, g)
    n0012 = generate_node_and_add_to_graph('0012', '01|2|3', 7, 4.5, 1, g)
    n0122 = generate_node_and_add_to_graph('0122', '0|1|23', 3, 5.5, 1, g)

    n0123 = generate_node_and_add_to_graph('0123', '0|1|2|3', 13, 3, 0, g)

    g.add_edge(n0000, n0110)
    g.add_edge(n0000, n0111)
    g.add_edge(n0000, n0010)
    g.add_edge(n0000, n0101)
    g.add_edge(n0000, n0001)
    g.add_edge(n0000, n0100)
    g.add_edge(n0000, n0011)

    g.add_edge(n0110, n0112)
    g.add_edge(n0110, n0120)

    g.add_edge(n0111, n0112)
    g.add_edge(n0111, n0121)
    g.add_edge(n0111, n0122)

    g.add_edge(n0010, n0120)
    g.add_edge(n0010, n0121)
    g.add_edge(n0010, n0012)

    g.add_edge(n0101, n0121)
    g.add_edge(n0101, n0102)

    g.add_edge(n0001, n0112)
    g.add_edge(n0001, n0102)
    g.add_edge(n0001, n0012)

    g.add_edge(n0100, n0120)
    g.add_edge(n0100, n0102)
    g.add_edge(n0100, n0122)

    g.add_edge(n0011, n0012)
    g.add_edge(n0011, n0122)

    g.add_edge(n0112, n0123)
    g.add_edge(n0120, n0123)
    g.add_edge(n0121, n0123)
    g.add_edge(n0102, n0123)
    g.add_edge(n0012, n0123)
    g.add_edge(n0122, n0123)


    n0122.minimum = True

    ############################################

    output_graph(g)

    n0112.set_visiting()
    output_graph(g)

    g.get_edge(n0112, n0110).set_direction_up()
    g.get_edge(n0112, n0110).set_visiting()
    n0110.set_visiting()
    output_graph(g)

    g.get_edge(n0112, n0111).set_direction_up()
    g.get_edge(n0112, n0111).set_visiting()
    n0111.set_visiting()
    output_graph(g)

    g.get_edge(n0112, n0001).set_direction_up()
    g.get_edge(n0112, n0001).set_visiting()
    n0001.set_visiting()
    output_graph(g)

    g.get_edge(n0112, n0123).set_direction_down()
    g.get_edge(n0112, n0123).set_visiting()
    n0123.set_visiting()
    output_graph(g)

    n0112.set_minimum_local()
    output_graph(g)

    g.reset()
    n0000.set_pruned()
    output_graph(g)

    ############################################

    n0122.set_visiting()
    output_graph(g)

    g.get_edge(n0122, n0100).set_direction_up()
    g.get_edge(n0122, n0100).set_visiting()
    n0100.set_visiting()
    output_graph(g)

    g.get_edge(n0122, n0011).set_direction_up()
    g.get_edge(n0122, n0011).set_visiting()
    n0011.set_visiting()
    output_graph(g)

    n0122.set_minimum_local()
    output_graph(g)

    g.reset()
    output_graph(g)

    ############################################

    n0120.set_visiting()
    output_graph(g)

    g.get_edge(n0120, n0010).set_direction_up()
    g.get_edge(n0120, n0010).set_visiting()
    n0010.set_visiting()
    output_graph(g)

    n0120.set_minimum_local()
    output_graph(g)

    g.reset()
    output_graph(g)

    ############################################

    n0101.set_visiting()
    output_graph(g)

    g.get_edge(n0101, n0121).set_direction_down()
    g.get_edge(n0101, n0121).set_visiting()
    n0121.set_visiting()
    output_graph(g)

    g.reset()
    n0121.set_visiting()
    output_graph(g)

    n0121.set_minimum_local()
    output_graph(g)

    g.reset()
    output_graph(g)

    ############################################

    n0102.set_visiting()
    output_graph(g)

    n0102.set_minimum_local()
    output_graph(g)

    g.reset()
    output_graph(g)

    ############################################

    n0012.set_visiting()
    output_graph(g)

    n0012.set_minimum_local()
    output_graph(g)

    g.reset()
    output_graph(g)


if __name__ == '__main__':
    main()