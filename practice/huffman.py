from heapq import heappush, heappop, heapify
from collections import defaultdict

# Node class to represent a Huffman tree node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman tree
def build_huffman_tree(text):
    # Count the frequency of each character in the text
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    # Create a priority queue (min-heap) of Huffman nodes
    heap = []
    for char, freq in freq_dict.items():
        node = HuffmanNode(char, freq)
        heappush(heap, node)

    # Build the Huffman tree by merging nodes from the priority queue
    while len(heap) > 1:
        left_child = heappop(heap)
        right_child = heappop(heap)

        # Create a new parent node with the combined frequency
        parent = HuffmanNode(None, left_child.freq + right_child.freq)
        parent.left = left_child
        parent.right = right_child

        # Add the parent node back to the priority queue
        heappush(heap, parent)

    # Return the root of the Huffman tree
    return heappop(heap)

# Function to traverse the Huffman tree and build the codewords
def build_codewords(node, codeword, codewords):
    if node.char is not None:
        codewords[node.char] = codeword
    else:
        build_codewords(node.left, codeword + "0", codewords)
        build_codewords(node.right, codeword + "1", codewords)

# Function to encode text using the Huffman tree
def encode(text):
    huffman_tree = build_huffman_tree(text)
    codewords = {}
    build_codewords(huffman_tree, "", codewords)
    encoded_text = "".join(codewords[char] for char in text)
    return encoded_text, huffman_tree

# Function to decode encoded text using the Huffman tree
def decode(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text

text = "Huffman coding is a data compression algorithm."
encoded_text, huffman_tree = encode(text)
decoded_text = decode(encoded_text, huffman_tree)

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
