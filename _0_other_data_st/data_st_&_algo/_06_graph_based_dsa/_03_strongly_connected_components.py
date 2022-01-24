"""
Strongly Connected Components

We can find all strongly connected components in O(V+E) time using Kosaraju’s algorithm. Following is detailed
    Kosaraju’s algorithm.

1) Create an empty stack ‘S’ and do DFS traversal of a graph. In DFS traversal, after calling recursive DFS for adjacent
    vertices of a vertex, push the vertex to stack. In the above graph, if we start DFS from vertex 0, we get vertices
    in stack as 1, 2, 4, 3, 0.

2) Reverse directions of all arcs to obtain the transpose graph.

3) One by one pop a vertex from S while S is not empty. Let the popped vertex be ‘v’. Take v as source and do DFS
    (call DFSUtil(v)). The DFS starting from v prints strongly connected component of v. In the above example, we
    process vertices in order 0, 3, 4, 2, 1 (One by one popped from stack).

How does this work?
The above algorithm is DFS based. It does DFS two times. DFS of a graph produces a single tree if all vertices are
    reachable from the DFS starting point. Otherwise DFS produces a forest. So DFS of a graph with only one SCC always
    produces a tree. The important point to note is DFS may produce a tree or a forest when there are more than one SCCs
    depending upon the chosen starting point. For example, in the above diagram, if we start DFS from vertices 0 or 1
    or 2, we get a tree as output. And if we start from 3 or 4, we get a forest. To find and print all SCCs, we would
    want to start DFS from vertex 4 (which is a sink vertex), then move to 3 which is sink in the remaining set
    (set excluding 4) and finally any of the remaining vertices (0, 1, 2). So how do we find this sequence of picking
    vertices as starting points of DFS? Unfortunately, there is no direct way for getting this sequence. However, if we
    do a DFS of graph and store vertices according to their finish times, we make sure that the finish time of a vertex
    that connects to other SCCs (other that its own SCC), will always be greater than finish time of vertices in the
    other SCC (See this for proof). For example, in DFS of above example graph, finish time of 0 is always greater than
    3 and 4 (irrespective of the sequence of vertices considered for DFS). And finish time of 3 is always greater than
    4. DFS does’t guarantee about other vertices, for example finish times of 1 and 2 may be smaller or greater than 3
    and 4 depending upon the sequence of vertices considered for DFS. So to use this property, we do DFS traversal of
    complete graph and push every finished vertex to a stack. In stack, 3 always appears after 4, and 0 appear after
    both 3 and 4.

In the next step, we reverse the graph. Consider the graph of SCCs. In the reversed graph, the edges that connect two
    components are reversed. So the SCC {0, 1, 2} becomes sink and the SCC {4} becomes source. As discussed above,
    in stack, we always have 0 before 3 and 4. So if we do a DFS of the reversed graph using sequence of vertices in
    stack, we process vertices from sink to source (in reversed graph).That is what we wanted to achieve and that is all
    needed to print SCCs one by one.

"""

# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict


class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g1 = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g1.add_edge(j, i)
        return g1

    # Print strongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * self.V

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * self.V

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()


"""
Kosaraju's Algorithm Complexity
Kosaraju's algorithm runs in linear time i.e. O(V+E).

Strongly Connected Components Applications
Vehicle routing applications
Maps
Model-checking in formal verification
"""