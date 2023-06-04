class BinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    
    def Heapify_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
    
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.Heapify_up(self.current_size)
    
    def Heapify_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
    
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.Heapify_down(i)
            i = i - 1
    
    def delete_min(self):
        if self.current_size == 0:
            print("Heap is empty.")
            return
        
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.Heapify_down(1)
        
        return min_val
    
    def heap_sort(self):
        sorted_list = []
        while self.current_size > 0:
            min_val = self.delete_min()
            sorted_list.append(min_val)
        
        return sorted_list


# Create an instance of BinHeap and insert 5 elements
bh = BinHeap()
elements = [9, 5, 2, 7, 3]
for element in elements:
    bh.insert(element)

# Display the contents of the BinHeap
print("Contents of BinHeap after inserting 5 elements:", bh.heap_list[1:])

# Initialize a list with 10 values and build the heap tree
list_values = [14, 8, 1, 10, 6, 4, 12, 9, 3, 5]
bh.build_heap(list_values)
print("Contents of BinHeap after building the heap tree:", bh.heap_list[1:])

# Delete the minimum value from the heap tree
min_value = bh.delete_min()
print("Minimum value deleted:", min_value)
print("Contents of BinHeap after deleting the minimum value:", bh.heap_list[1:])

# Perform heap sort on the heap tree
sorted_list = bh.heap_sort()
print("Sorted list:", sorted_list)
