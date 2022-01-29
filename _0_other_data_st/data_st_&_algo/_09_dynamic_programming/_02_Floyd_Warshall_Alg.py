"""
Floyd-Warshall Algorithm

Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted
    graph. This algorithm works for both the directed and undirected weighted graphs. But, it does not work for the
    graphs with negative cycles (where the sum of the edges in a cycle is negative).

A weighted graph is a graph in which each edge has a numerical value associated with it.

Floyd-Warshall algorithm is also called as Floyd's algorithm, Roy-Floyd algorithm, Roy-Warshall algorithm, or
    WFI algorithm.

This algorithm follows the dynamic programming approach to find the shortest paths.

How Floyd-Warshall Algorithm Works?
Let the given graph be:

                            5
                        1 --------> 4
                      ^   \        ^ |
                     |   3 |    /    |  2
                 2   \    /    /4    |
                      \  -    /      _
                        2 <--------  3
                             1

                             Initial graph


Follow the steps below to find the shortest path between all the pairs of vertices.

1. Create a matrix A0 of dimension n*n where n is the number of vertices. The row and the column are indexed as i and j
    respectively. i and j are the vertices of the graph.

Each cell A[i][j] is filled with the distance from the ith vertex to the jth vertex. If there is no path from ith vertex
    to jth vertex, the cell is left as infinity.


                        0   3  INF   5
                        2   0  INF   4


"""