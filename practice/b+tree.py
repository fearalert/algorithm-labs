class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.child = []
        self.leaf = leaf
        self.next = None

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BPlusTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BPlusTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.child = y.child[t:(2 * t)]
            y.child = y.child[0:t - 1]

    def search(self, k, x=None):
        if isinstance(x, BPlusTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if x.leaf:
                if i < len(x.keys) and k == x.keys[i][0]:
                    return x.keys[i][1]
                else:
                    return None
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)

    def display(self, x, lvl=0):
        print("Level", lvl, ":", len(x.keys), end=" ")
        for key in x.keys:
            print(key[0], end=" ")
        print()
        lvl += 1
        if not x.leaf:
            for child in x.child:
                self.display(child, lvl)


bplus_tree = BPlusTree(3)
bplus_tree.insert((5, "A"))
bplus_tree.insert((9, "B"))
bplus_tree.insert((10, "C"))
bplus_tree.insert((15, "D"))
bplus_tree.insert((20, "E"))

bplus_tree.display(bplus_tree.root)
