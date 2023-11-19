class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        #frequency of symbol
        self.freq = freq
        
        # symbol name (character)
        self.symbol = symbol
        
        #node left of current node
        self.left = left

        #node right of current node
        self.right = right

        #tree direction (0/1)
        self.huff = ""

def print_nodes(node, code = ""):
    new_code = code + str(node.huff)

    if node.left:
        print_nodes(node.left, new_code)
    if node.right:
        print_nodes(node.right, new_code)
    
    if not node.left and not node.right:
        print(f"{node.symbol} --> {new_code}")
        

chars = ["a","b","c","d","e","f"]
freq = [10,9,1,13,11,45]

# array of nodes not in sorted order yet
nodes = [Node(freq[x],chars[x]) for x in range (len(chars))]

while len(nodes) > 1:
    nodes = sorted(nodes, key=lambda node:node.freq)

    left = nodes[0]
    right = nodes[1]

    left.huff = 0
    right.huff = 1

    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

print(chars)
print(freq)
print("Huffman Encoding:")
print_nodes(nodes[0])