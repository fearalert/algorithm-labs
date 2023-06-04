class FibonacciHeap:
    class Node:
        def __init__(self, key):
            self.key = key
            self.degree = 0
            self.parent = None
            self.child = None
            self.marked = False
            self.left = self
            self.right = self
    
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0
    
    def is_empty(self):
        return self.min_node is None
    
    def insert(self, key):
        new_node = self.Node(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._link(self.min_node, new_node)
            if new_node.key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1
    
    def get_min(self):
        if self.min_node is None:
            return None
        return self.min_node.key
    
    def extract_min(self):
        if self.min_node is None:
            return None
        min_node = self.min_node
        if min_node.child is not None:
            child = min_node.child
            while True:
                next_child = child.right
                self._add_node(child)
                child.parent = None
                child = next_child
                if child == min_node.child:
                    break
        self._remove_node(min_node)
        if min_node == min_node.right:
            self.min_node = None
        else:
            self.min_node = min_node.right
            self._consolidate()
        self.num_nodes -= 1
        return min_node.key
    
    def _link(self, node1, node2):
        node2.left.right = node2.right
        node2.right.left = node2.left
        node2.parent = node1
        if node1.child is None:
            node1.child = node2
            node2.left = node2
            node2.right = node2
        else:
            node2.left = node1.child
            node2.right = node1.child.right
            node1.child.right.left = node2
            node1.child.right = node2
        node1.degree += 1
        node2.marked = False
    
    def _add_node(self, node):
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right.left = node
        self.min_node.right = node
    
    def _remove_node(self, node):
        node.left.right = node.right
        node.right.left = node.left
    
    def _consolidate(self):
        max_degree = (self.num_nodes.bit_length() + 1).bit_length()
        degree_table = [None] * max_degree
        nodes = []
        current_node = self.min_node
        while True:
            nodes.append(current_node)
            current_node = current_node.right
            if current_node == self.min_node:
                break
        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if other.key < node.key:
                    node, other = other, node
                self._link(node, other)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node
            if node.key < self.min_node.key:
                self.min_node = node
# Create an instance of FibonacciHeap
fib_heap = FibonacciHeap()

# Insert values into the heap
values = [4, 2, 7, 1, 5]
for value in values:
    fib_heap.insert(value)

# Extract the minimum value
min_value = fib_heap.extract_min()
print("Minimum value extracted:", min_value)

# Get the minimum value without extraction
current_min = fib_heap.get_min()
print("Current minimum value:", current_min)
