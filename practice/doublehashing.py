class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return 7 - (key % 7)  # Second hash function

    def insert(self, key):
        hash_value = self.hash_function(key)
        if self.hash_table[hash_value] is None:
            self.hash_table[hash_value] = key
        else:
            i = 1
            while True:
                next_hash = (hash_value + i * self.hash_function_2(key)) % self.size
                if self.hash_table[next_hash] is None:
                    self.hash_table[next_hash] = key
                    break
                i += 1
                if i == self.size:  # Reached end of the table, cannot find an empty slot
                    print("Hash table is full. Unable to insert key:", key)
                    break

    def search(self, key):
        hash_value = self.hash_function(key)
        if self.hash_table[hash_value] == key:
            return hash_value
        else:
            i = 1
            while True:
                next_hash = (hash_value + i * self.hash_function_2(key)) % self.size
                if self.hash_table[next_hash] == key:
                    return next_hash
                if self.hash_table[next_hash] is None or i == self.size:  # Key not found
                    return None
                i += 1

    def delete(self, key):
        hash_value = self.hash_function(key)
        if self.hash_table[hash_value] == key:
            self.hash_table[hash_value] = None
        else:
            i = 1
            while True:
                next_hash = (hash_value + i * self.hash_function_2(key)) % self.size
                if self.hash_table[next_hash] == key:
                    self.hash_table[next_hash] = None
                    break
                if self.hash_table[next_hash] is None or i == self.size:  # Key not found
                    print("Key not found:", key)
                    break
                i += 1

    def display(self):
        print("Hash Table:")
        for index, value in enumerate(self.hash_table):
            if value is not None:
                print(index, "-->", value)
            else:
                print(index, "-->", "None")


# Example usage
hash_table = DoubleHashingHashTable(10)
hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(35)
hash_table.insert(45)
hash_table.display()

print("Search result for key 15:", hash_table.search(15))
print("Search result for key 35:", hash_table.search(35))
print("Search result for key 55:", hash_table.search(55))

hash_table.delete(15)
hash_table.delete(35)
hash_table.delete(55)  # Key not found
hash_table.display()