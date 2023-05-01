class BinarySearchTree:
    def __init__(self, key=0, value=0):
        self.root = None
        self._size = 0

    class BSTNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.right = None
            self.left = None

    def size(self):
        return self._size

    def add(self, key, value):
        z = self.BSTNode(key, value)
        y = None
        x = self.root

        while (x != None):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right

        if (y == None):
            self.root = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z

        self._size += 1

    def search(self, key):
        x = self.root
        while x != None:
            if key == x.key:
                return x.value
            elif key < x.key:
                x = x.left
            else:
                x = x.right
        return False

    def smallest(self):
        x = self.root
        while x.left != None:
            x = x.left

        return (x.key, x.value)

    def largest(self):
        x = self.root
        while x.right != None:
            x = x.right

        return (x.key, x.value)

    def remove(self, key):
        x = self.root
        y = None

        while (x != None and x.key != key):
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right

        if x == None:
            return

        if x.left == None or x.right == None:
            z = None

            if x.left == None:
                z = x.right
            else:
                z = x.left

            if y == None:
                return

            if x == y.left:
                y.left = z
            else:
                y.right = z

            x = None

        else:
            p = None
            temp = None

            temp = x.right
            while (temp.left != None):
                p = temp
                temp = temp.left

            if p != None:
                p.left = temp.right
            else:
                x.right = temp.right

            x.key = temp.key
            temp = None
            self._size -= 1

    def inorder_walk(self):
       nodes = []
       self._inorder_walk(self.root, nodes)
       return nodes
   
    def _inorder_walk(self, subtree, nodes):
       if subtree:
           self._inorder_walk(subtree.left, nodes)
           nodes.append(subtree.key)
           self._inorder_walk(subtree.right, nodes)
           
           
    def postorder_walk(self):
       nodes = []
       self._postorder_walk(self.root, nodes)
       return nodes
   
    def _postorder_walk(self, subtree, nodes):
       if subtree:
           self._postorder_walk(subtree.left, nodes)
           self._postorder_walk(subtree.right, nodes)
           nodes.append(subtree.key)
    
    def preorder_walk(self):
       nodes = []
       self._preorder_walk(self.root, nodes)
       return nodes
   
    def _preorder_walk(self, subtree, nodes):
       if subtree:
           nodes.append(subtree.key)
           self._preorder_walk(subtree.left, nodes)
           self._preorder_walk(subtree.right, nodes)


bst = BinarySearchTree()
bst.add(5, "apple")
bst.add(3, "banana")
bst.add(7, "cherry")
bst.add(2, "date")
bst.add(4, "elderberry")
bst.add(6, "fig")
bst.add(8, "grape")

print("Inorder traversal: ", bst.inorder_walk())
print("Preorder traversal: ", bst.preorder_walk())
print("Postorder traversal: ", bst.postorder_walk())
print("Size of tree: ", bst.size())
print("Smallest key: ", bst.smallest())
print("Largest key: ", bst.largest())

key_to_remove = 7
bst.remove(key_to_remove)
print("Removed key:", key_to_remove)
print("Inorder traversal after removing", key_to_remove, ":", bst.inorder_walk())
print("Preorder traversal after removing", key_to_remove, ":", bst.preorder_walk())

key_to_search = 3
print("Value of key", key_to_search, ":", bst.search(key_to_search))
