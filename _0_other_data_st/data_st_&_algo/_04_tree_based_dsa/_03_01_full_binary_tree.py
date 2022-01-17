"""
Full Binary Tree

A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no
children.

It is also known as a proper binary tree.

                                 1
                               /  \
                              /    \
                            2      3
                           /  \
                          /    \
                        4       5
                              /  \
                             /    \
                            6     7

                            Full Binary Tree


Full Binary Tree Theorems
Let, i = the number of internal nodes
       n = be the total number of nodes
       l = number of leaves
      λ = number of levels


The number of leaves is i + 1.
The total number of nodes is 2i + 1.
The number of internal nodes is (n – 1) / 2.
The number of leaves is (n + 1) / 2.
The total number of nodes is 2l – 1.
The number of internal nodes is l – 1.
The number of leaves is at most 2λ - 1.


"""

# Checking if a binary tree is a full binary tree in Python


# Creating a node
class Node:

    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None


# Checking full binary tree
def isFullTree(root1):

    # Tree empty case
    if root1 is None:
        return True

    # Checking whether child is present
    if root1.leftChild is None and root1.rightChild is None:
        return True

    if root1.leftChild is not None and root1.rightChild is not None:
        return isFullTree(root1.leftChild) and isFullTree(root1.rightChild)

    return False


root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2)

root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(7)

if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")
