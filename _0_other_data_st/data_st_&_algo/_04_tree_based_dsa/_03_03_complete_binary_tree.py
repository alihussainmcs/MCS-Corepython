"""
Complete Binary Tree

A complete binary tree is a binary tree in which all the levels are completely filled except possibly the lowest one,
which is filled from the left.

A complete binary tree is just like a full binary tree, but with two major differences

All the leaf elements must lean towards the left.
The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

                                  1
                               /    \
                              /      \
                            2         3
                           /  \      /
                          /    \    /
                        4       5  6

                        Complete Binary Tree

Full Binary Tree vs Complete Binary Tree
1)                                1
                               /    \
                              /      \
                            2         3
                           /  \        \
                          /    \        \
                        4       5        6


                         X  Full Binary Tree
                         X  Complete Binary Tree


2)
                                  1
                               /    \
                              /      \
                            2         3
                                    /  \
                                   /    \
                                  6      7

                         ✓  Full Binary Tree
                         x  Complete Binary Tree

3)
                                  1
                               /    \
                              /      \
                            2         3
                           /
                          /
                        4

                         x  Full Binary Tree
                         ✓  Complete Binary Tree

4)
                                  1
                               /    \
                              /      \
                            2         3
                           /  \
                          /    \
                        4       5


                         ✓  Full Binary Tree
                         ✓  Complete Binary Tree

How a Complete Binary Tree is Created?
Select the first element of the list to be the root node. (no. of elements on level-I: 1)

1.Select the first element as root
                    (1)                    1 12 9 5 6 10

2.Put the second element as a left child of the root node and the third element as the right child.
    (no. of elements on level-II: 2)

            (1)             1 12 9 5 6 10
           /  \
          12   9

          12 as a left child and 9 as a right child

3.Put the next two elements as children of the left node of the second level. Again, put the next two elements as
children of the right node of the second level (no. of elements on level-III: 4) elements).

4.Keep repeating until you reach the last element.

                        (1)                 1 12 9 5 6 10
                       /  \
                      12   9
                     /  \  |
                    5   6  10


"""


# Checking if a binary tree is a complete binary tree


class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


# Count the number of nodes
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Check if the tree is complete binary tree
def is_complete(root, index1, number_nodes):
    # Check if the tree is empty
    if root is None:
        return True

    if index1 >= number_nodes:
        return False

    return (is_complete(root.left, 2 * index1 + 1, number_nodes)
            and is_complete(root.right, 2 * index1 + 2, number_nodes))


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)

node_count = count_nodes(root1)
index = 0

if is_complete(root1, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")

"""
Relationship between array indexes and tree element
A complete binary tree has an interesting property that we can use to find the children and parents of any node.

Complete Binary Tree Applications
Heap-based data structures
Heap sort

"""
