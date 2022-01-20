"""
Insertion into a B-tree

Inserting an element on a B-tree consists of two events: searching the appropriate node to insert the element and
splitting the node if required.Insertion operation always takes place in the bottom-up approach.

Let us understand these events below.

Insertion Operation
If the tree is empty, allocate a root node and insert the key.
Update the allowed number of keys in the node.
Search the appropriate node for insertion.
If the node is full, follow the steps below.
Insert the elements in increasing order.
Now, there are elements greater than its limit. So, split at the median.
Push the median key upwards and make the left keys as a left child and the right keys as a right child.
If the node is not full, follow the steps below.
Insert the node in increasing order.
Insertion Example
Let us understand the insertion operation with the illustrations below.


The elements to be inserted are 8, 9, 10, 11, 15, 20, 17.


---8--> 8      ---9--> 8 9      --10-->   9        --11-->    9
                                        /   \               /   \
                                       8     10            8    10 11

--15-->    9             ------>     9 11      --20-->     9 11
        /     \                     /  | \                /  |  \
      8     10 11 15              8   10  15             8   10  15 20


--17-->  9 11                         9    11    17                              11
        /  |    \         ------>    /   |    \  |      ------>               /      \
      8   10   15 17 20             8    10   15 20                          9        17
                                                                            / \      /  \
                                                                           8   10   15  20

                            Inserting elements into a B-tree


Algorithm for Inserting an Element
BTreeInsertion(T, k)
r  root[T]
if n[r] = 2t - 1
    s = AllocateNode()
    root[T] = s
    leaf[s] = FALSE
    n[s] <- 0
    c1[s] <- r
    BtreeSplitChild(s, 1, r)
    BtreeInsertNonFull(s, k)
else BtreeInsertNonFull(r, k)
BtreeInsertNonFull(x, k)
i = n[x]
if leaf[x]
    while i ≥ 1 and k < keyi[x]
        keyi+1 [x] = keyi[x]
        i = i - 1
    keyi+1[x] = k
    n[x] = n[x] + 1
else while i ≥ 1 and k < keyi[x]
        i = i - 1
    i = i + 1
    if n[ci[x]] == 2t - 1
        BtreeSplitChild(x, i, ci[x])
        if k &rt; keyi[x]
            i = i + 1
    BtreeInsertNonFull(ci[x], k)
BtreeSplitChild(x, i)
BtreeSplitChild(x, i, y)

"""


# Inserting a key on a B-tree in Python


# Create a node
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


# Tree
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    # Insert node
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    # Insert none full
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    # Split the child
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    # Print the tree
    def print_tree(self, x, l1=0):
        print("Level ", l1, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l1 += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l1)


def main():
    B = BTree(3)

    for i in range(10):
        B.insert((i, 2 * i))

    B.print_tree(B.root)


if __name__ == '__main__':
    main()
