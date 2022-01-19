"""
An AVL tree is a self-balancing binary search tree.
It was the first such data structure to be invented.
In an AVL tree, the heights of the two child subtrees of
any node differ by at most one; if at any time they differ
by more than one, rebalancing is done to restore this property
-- in this implementation duplicates are not allowed.
"""


class AVLNode:
    # node class
    def __init__(self, value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.height = 1


# wrapper Tree class
class AVLTree:
    def __init__(self, avl_node=None):
        self.root = avl_node

    def _find(self, node, val):
        if node is None:
            return False
        elif node.value == val:
            return True
        elif val < node.value:
            if node.leftchild is not None:
                if val == node.leftchild.value:
                    return True
                else:
                    return self._find(node.leftchild, val)
            else:
                return False
        elif val > node.value:
            if node.rightchild is not None:
                if val == node.rightchild.value:
                    return True
                else:
                    return self._find(node.rightchild, val)
            else:
                return False

    def find(self, val):
        return self._find(self.root, val)

    def _preOrderTraverse(self, node):
        if not node:
            return
        else:
            print(node.value, end=' ')
            self._preOrderTraverse(node.leftchild)
            self._preOrderTraverse(node.rightchild)

    def preOrderTraverse(self):
        self._preOrderTraverse(self.root)

    def _inOrderTraverse(self, node):
        if not node:
            return
        else:
            self._inOrderTraverse(node.leftchild)
            print(node.value, end=' ')
            self._inOrderTraverse(node.rightchild)

    def inOrderTraverse(self):
        self._inOrderTraverse(self.root)

    def _postOrderTraverse(self, node):
        if not node:
            return
        else:
            self._postOrderTraverse(node.leftchild)
            self._postOrderTraverse(node.rightchild)
            print(node.value, end=' ')

    def postOrderTraverse(self):
        self._postOrderTraverse(self.root)

    def _levelOrderTraverse(self, node):
        if node is None:
            return
        else:
            queue = [node]
            while queue:
                temp = queue.pop(0)
                print(temp.value, end=' ')
                if temp.leftchild:
                    queue.append(temp.leftchild)
                if temp.rightchild:
                    queue.append(temp.rightchild)

    def levelOrderTraverse(self):
        self._levelOrderTraverse(self.root)

    def _getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getHeight(self):
        # height of entire tree
        return self._getHeight(self.root) - 1

    def _updateHeight(self, node):
        node.height = 1 + max(self._getHeight(node.leftchild), self._getHeight(node.rightchild))

    def _rightRotate(self, disbalanced):
        new_node = disbalanced.leftchild
        disbalanced.leftchild = disbalanced.leftchild.rightchild
        new_node.rightchild = disbalanced
        self._updateHeight(new_node)
        self._updateHeight(disbalanced)
        return new_node

    def _leftRotate(self, disbalanced):
        new_node = disbalanced.rightchild
        disbalanced.rightchild = disbalanced.rightchild.leftchild
        new_node.leftchild = disbalanced
        self._updateHeight(disbalanced)
        self._updateHeight(new_node)
        return new_node

    def _getBalance(self, node):
        if not node:
            return 0
        else:
            return self._getHeight(node.leftchild) - self._getHeight(node.rightchild)

    def getBalance(self):
        return self._getBalance(self.root)

    def _insert(self, node, value):

        if node is None:
            return AVLNode(value)
        # elif value == node.value:
        #     node.leftchild = self._insert(node.leftchild,value)
        elif value < node.value:
            node.leftchild = self._insert(node.leftchild, value)
        else:
            node.rightchild = self._insert(node.rightchild, value)

        # self._updateHeight(node)
        node.height = 1 + max(self._getHeight(node.leftchild), self._getHeight(node.rightchild))
        balance = self._getBalance(node)

        if balance > 1 and value < node.leftchild.value:
            # LL condition
            return self._rightRotate(node)

        if balance > 1 and value > node.leftchild.value:
            # LR condition
            # left rotate leftchild
            # right rotate node
            node.leftchild = self._leftRotate(node.leftchild)
            return self._rightRotate(node)

        if balance < -1 and value > node.rightchild.value:
            # RR condition
            return self._leftRotate(node)

        if balance < -1 and value < node.rightchild.value:
            # RL condition
            # right rotate right child
            # left rotate node
            node.rightchild = self._rightRotate(node.rightchild)
            return self._leftRotate(node)

        # return balanced node
        return node

    def insert(self, value):
        # if self.root is None:
        #     self.root = AVLNode(value)
        # else:
        #     self.root = self._insert(self.root,value)
        if self._find(self.root, value):
            return False, {'error message': 'duplicates not allowed'}
        else:
            self.root = self._insert(self.root, value)

    def _getMinNode(self, node):
        min_node = node
        while min_node.leftchild is not None:
            min_node = min_node.leftchild
        return min_node

    def _deleteNode(self, node, value):
        if node is None:
            return node
        else:
            if value < node.value:
                node.leftchild = self._deleteNode(node.leftchild, value)
            elif value > node.value:
                node.rightchild = self._deleteNode(node.rightchild, value)

            # not one of above case, i.e. value = node.value
            else:
                if node.leftchild is None:
                    right_subtree = node.rightchild
                    node = None
                    return right_subtree
                if node.rightchild is None:
                    left_subtree = node.leftchild
                    node = None
                    return left_subtree

                # node has both children present
                # find min node in right subtree, replace with it, delete that node

                temp = self._getMinNode(node.rightchild)
                node.value = temp.value
                node.rightchild = self._deleteNode(node.rightchild, temp.value)

                node.height = 1 + max(self._getHeight(node.leftchild), self._getHeight(node.rightchild))
                balance = self._getBalance(node)

                if balance > 1 and value < node.leftchild.value:
                    # LL condition
                    return self._rightRotate(node)

                if balance > 1 and value > node.leftchild.value:
                    # LR condition
                    # left rotate leftchild
                    # right rotate node
                    node.leftchild = self._leftRotate(node.leftchild)
                    return self._rightRotate(node)

                if balance < -1 and value > node.rightchild.value:
                    # RR condition
                    return self._leftRotate(node)

                if balance < -1 and value < node.rightchild.value:
                    # RL condition
                    # right rotate right child
                    # left rotate node
                    node.rightchild = self._rightRotate(node.rightchild)
                    return self._leftRotate(node)

            return node

    def delete(self, value):
        self.root = self._deleteNode(self.root, value)

    # delete entire tree
    def dropTree(self):
        self.root = None
        return self.root


tree = AVLTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(8)
tree.insert(9)
tree.insert(10)
print(tree.insert(10))

tree.insert(5)
# tree.insert(5) # dup value
# tree.insert(5)# dup value

tree.insert(4)
tree.insert(7)
tree.insert(12)
tree.insert(0)
tree.insert(13)
tree.insert(14)
tree.insert(15)

tree.inOrderTraverse()
print('\n')
tree.levelOrderTraverse()

tree.delete(4)
print('\nafter delete\n')
tree.levelOrderTraverse()

print("\n", "height:", tree.getHeight())
print("\n", "balance:", tree.getBalance())
tree.insert(4)
tree.levelOrderTraverse()
print("\n", "height:", tree.getHeight())
print("\n", "balance:", tree.getBalance())
tree.delete(5)
tree.delete(5)
tree.levelOrderTraverse()
print("\n", "height:", tree.getHeight())
print("\n", "balance:", tree.getBalance())
# tree.insert(4)
# tree.insert(5)
# tree.levelOrderTraverse()
# print("\n","height:",tree.getHeight())
# print("\n","balance:",tree.getBalance())
# print(tree.find(100))

print(tree.dropTree())
tree.levelOrderTraverse()
