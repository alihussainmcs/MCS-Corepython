"""
Perfect Binary Tree

A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf
nodes are at the same level.

                                  1
                               /    \
                              /      \
                            2         3
                           /  \      /  \
                          /    \    /    \
                        4       5  6      7

                        Perfect Binary Tree

All the internal nodes have a degree of 2.

Recursively, a perfect binary tree can be defined as:

If a single node has no children, it is a perfect binary tree of height h = 0,
If a node has h > 0, it is a perfect binary tree if both of its subtrees are of height h - 1 and are non-overlapping.



        tree : 1                     tree : 1               tree : 2

           ()                           ()                      ( )
                                       /  \                    /   \
                                     ()   ()                 ()    ()
                                                            /  \  /  \
                                                           ()  ()()  ()


                                    Perfect Binary Tree

The following code is for checking whether a tree is a perfect binary tree.

"""


# Checking if a binary tree is a perfect binary tree in Python


class NewNode:
    def __init__(self, k):
        self.key = k
        self.right = self.left = None


# Calculate the depth
def calculateDepth(node):
    d = 0
    while node is not None:
        d += 1
        node = node.left
    return d


# Check if the tree is perfect binary tree
def is_perfect(root, d, level=0):

    # Check if the tree is empty
    if root is None:
        return True

    # Check the presence of trees
    if root.left is None and root.right is None:
        return d == level + 1

    if root.left is None or root.right is None:
        return False

    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))


# root1 = None
root1 = NewNode(1)
root1.left = NewNode(2)
root1.right = NewNode(3)
root1.left.left = NewNode(4)
root1.left.right = NewNode(5)

if is_perfect(root1, calculateDepth(root1)):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")

print('---------------------------------------------------------------------------------------------')

# root1 = None
root1 = NewNode(10)
root1.left = NewNode(20)
root1.right = NewNode(30)

root1.left.left = NewNode(40)
root1.left.right = NewNode(50)
root1.right.left = NewNode(60)
root1.right.right = NewNode(70)

if is_perfect(root1, calculateDepth(root1)):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
"""
Perfect Binary Tree Theorems

A perfect binary tree of height h has 2h + 1 – 1 node.
A perfect binary tree with n nodes has height log(n + 1) – 1 = Θ(ln(n)).
A perfect binary tree of height h has 2h leaf nodes.
The average depth of a node in a perfect binary tree is Θ(ln(n)).
"""