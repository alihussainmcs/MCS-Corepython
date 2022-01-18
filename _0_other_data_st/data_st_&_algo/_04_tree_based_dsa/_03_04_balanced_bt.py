"""
Balanced Binary Tree

A balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the
height of the left and right subtree of any node differ by not more than 1.

Following are the conditions for a height-balanced binary tree:

difference between the left and the right subtree for any node is not more than one
the left subtree is balanced
the right subtree is balanced

                                 1  df = 1
                               /  \
                              /    \
                    df = 0   2      3  df = 0
                           /  \
                          /    \
                df = 0   4       5  df = 0

              Balanced Binary Tree with depth at each level



                                 1  df = 2
                               /  \
                              /    \
                    df = 1   2      3  df = 0
                           /  \
                          /    \
                df = 0   4       5  df = 1
                                /
                               /
                              6  df = 0

                Unbalanced Binary Tree with depth at each level

"""


# Checking if a binary tree is height balanced in Python


class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isHeightBalanced(root, height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l1 = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l1 and r

    return False


height1 = Height()

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

if isHeightBalanced(root1, height1):
    print('The tree is balanced')
else:
    print('The tree is not balanced')


"""
Balanced Binary Tree Applications
AVL tree
Balanced Binary Search Tree
"""