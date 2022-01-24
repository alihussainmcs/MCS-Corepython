"""
Depth First Search (DFS)

Depth first Search or Depth first traversal is a recursive algorithm for searching all the vertices of a graph or tree
    data structure. Traversal means visiting all the nodes of a graph.

Depth First Search Algorithm
A standard DFS implementation puts each vertex of the graph into one of two categories:

Visited
Not Visited
The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

The DFS algorithm works as follows:

Start by putting any one of the graph's vertices on top of a stack.
Take the top item of the stack and add it to the visited list.
Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the top of the stack.
Keep repeating steps 2 and 3 until the stack is empty.
Depth First Search Example
Let's see how the Depth First Search algorithm works with an example. We use an undirected graph with 5 vertices.

                      0----3
                     | \
                     |  2
                     | /  \
                    1      4

DFS Pseudocode (recursive implementation)
The pseudocode for DFS is shown below. In the init() function, notice that we run the DFS function on every node. This
    is because the graph might have two different disconnected parts so to make sure that we cover every vertex, we can
    also run the DFS algorithm on every node.

DFS(G, u)
    u.visited = true
    for each v ∈ G.Adj[u]
        if v.visited == false
            DFS(G,v)

init() {
    For each u ∈ G
        u.visited = false
     For each u ∈ G
       DFS(G, u)
}

"""


# DFS algorithm in Python


# DFS algorithm
def dfs(graph1, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next1 in graph1[start] - visited:
        dfs(graph1, next1, visited)
    return visited


graph = {'0': {'1', '2'},
         '1': {'0', '3', '4'},
         '2': {'0'},
         '3': {'1'},
         '4': {'2', '3'}}

dfs(graph, '0')


"""
Complexity of Depth First Search
The time complexity of the DFS algorithm is represented in the form of O(V + E), where V is the number of nodes and E is 
    the number of edges.

The space complexity of the algorithm is O(V).

Application of DFS Algorithm
For finding the path
To test if the graph is bipartite
For finding the strongly connected components of a graph
For detecting cycles in a graph
"""