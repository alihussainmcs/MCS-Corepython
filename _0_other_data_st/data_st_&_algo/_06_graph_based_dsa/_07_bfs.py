"""
Breadth first search

Traversal means visiting all the nodes of a graph. Breadth First Traversal or Breadth First Search is a recursive
    algorithm for searching all the vertices of a graph or tree data structure.

BFS algorithm
A standard BFS implementation puts each vertex of the graph into one of two categories:

Visited
Not Visited
The purpose of the algorithm is to mark each vertex as visited while avoiding cycles.

The algorithm works as follows:

Start by putting any one of the graph's vertices at the back of a queue.
Take the front item of the queue and add it to the visited list.
Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the queue.
Keep repeating steps 2 and 3 until the queue is empty.
The graph might have two different disconnected parts so to make sure that we cover every vertex, we can also run the
    BFS algorithm on every node

BFS example
Let's see how the Breadth First Search algorithm works with an example. We use an undirected graph with 5 vertices.

                                   _ _ _ _ _
                      0----3      |_|_|_|_|_|  visited
                     | \
                     |  2          _ _ _ _ _
                     | /  \       |_|_|_|_|_|  Queue
                    1      4

                Undirected graph with 5 vertices


BFS pseudocode
create a queue Q
mark v as visited and put v into Q
while Q is non-empty
    remove the head u of Q
    mark and enqueue all (unvisited) neighbours of u


"""

# BFS algorithm in Python


import collections


# BFS algorithm
def bfs(graph1, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph1[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)


"""
BFS Algorithm Complexity
The time complexity of the BFS algorithm is represented in the form of O(V + E), where V is the number of nodes and E 
    is the number of edges.

The space complexity of the algorithm is O(V).

BFS Algorithm Applications
To build index by search index
For GPS navigation
Path finding algorithms
In Ford-Fulkerson algorithm to find maximum flow in a network
Cycle detection in an undirected graph
In minimum spanning tree

"""