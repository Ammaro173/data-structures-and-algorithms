import inspect, re, collections


class Graph:
    """
    [method] - add_node(value): adds a new vertex to the graph, returns the added vertex
    [method] - add_edge(vertex1, vertex2, [weight]): adds new edge between two virtices, takes in two verticies, has ability to add weight
    [method] - get_nodes() - returns all of the vertices as a collection
    [method] - get_neighbors(vertex): returns a collection of vertices (with weights) connected to a vertex, takes in a vertex
    [method] - get_values(vertex): returns the value from a given vertex
    [method] - size() - returns number of vertices in Graph; integer
    [method] - breadth_first(vertex) - traverses the graph starting from the given vertex, returns a list of nodes visited during traversal
    """

    def __init__(self):
        self._adj_list = {}

        # stores reference to variable user assigned at init
        name = inspect.getframeinfo(inspect.currentframe().f_back)[3][0].split()[0]
        self.name = re.sub(r"[=]", "", name)

    def __repr__(self):
        return self.name

    def add_node(self, value):
        """
        Adds a new vertex to the graph.
        Parameters:
            [value] - value to be assigned to the vertex
        Returns:
            vertex - the vertex that was created
        """
        vertex = Vertex(value)
        try:
            self._adj_list[vertex].append([vertex])
        except:
            self._adj_list[vertex] = [[vertex]]

        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Adds an edge between two existing vertices in the Graph.
        Parameters:
            [start_vertex] - First vertex to start edge from
            [end_vertex] - Second vertex to point edge to
            [[weight]] - Adds a weight to the edge (default 0)
        No return
        """
        if start_vertex not in self._adj_list or end_vertex not in self._adj_list:
            raise KeyError(f"{start_vertex} is not in {self}")

        adj_list = self._adj_list[start_vertex]
        for i in range(len(adj_list)):
            adjacencies = adj_list[i]

            if adjacencies[0] == start_vertex:
                adjacencies += [(end_vertex, weight)]

    def size(self):
        """
        Returns: Total number of vertices in the graph
        """
        return len(self._adj_list)

    def get_values(self, vertex):
        """
        Gets a values from the graph at a given vertex
        Parameters:
            [vertex] - The vertex to get value from
        Return:
            values - values from the vertex
        """
        try:
            for vtx in self._adj_list[vertex]:
                if vtx[0] == vertex:
                    return vtx[0].value
            return None
        except:
            raise KeyError(f"{vertex} is not in {self}")

    def get_nodes(self):
        """Returns a list of the vertices in the Graph."""
        if self.size() == 0:
            return None
        return [vtx for vtx in self._adj_list]

    def get_neighbors(self, vertex):
        """
        Gets the neighboring vertices to a given vertex
        Parameters:
            [vertex] - vertex to get the neighbors of
        Return:
            [list] - list of vertices with weights
        """
        try:
            lst = [
                vtx[idx] for vtx in self._adj_list[vertex] for idx in range(1, len(vtx))
            ]
            if lst:
                return lst
            return []
        except:
            return []


class Vertex:
    """
    Instance of a vertex object
    Attributes:
        [value] - requires a value to init
    """

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value
