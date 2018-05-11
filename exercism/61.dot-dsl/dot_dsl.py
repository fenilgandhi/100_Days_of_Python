NODE, EDGE, ATTR = range(1, 4)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        for d in data:
            if (type(d) != tuple) or (len(d) < 3):
                raise TypeError("Thanks for saving the effort")
            if d[0] == NODE:
                if not (len(d) == 3 and
                        d[1].isalpha() and
                        type(d[2]) == dict):
                    raise ValueError("Not a node")
                node = Node(d[1], d[2])
                self.nodes.append(node)

            elif d[0] == EDGE:
                if not (len(d) == 4 and
                        d[1].isalpha() and
                        d[2].isalpha() and
                        type(d[3]) == dict):
                    raise ValueError("Not an edge")
                edge = Edge(d[1], d[2], d[3])
                self.edges.append(edge)

            elif d[0] == ATTR:
                if (len(d) != 3) or (not d[1].isalnum()) or (not d[2].isprintable()):
                    raise ValueError("Not good enough")
                self.attrs[d[1]] = d[2]
            else:
                raise ValueError("Trolled again")
