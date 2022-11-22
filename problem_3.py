# HuffMan Coding
import sys

class huffmanTree():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        
    def children(self):
        return (self.left, self.right)
        
def tree(node, binString = ''):
    if type(node) is str:
        return {node : binString}
    left, right = node.children()
    d = dict()
    d.update(tree(left, binString + '0'))
    d.update(tree(left, binString + '1'))
    return d
        
def huffman_encoding(data):
    freq = {}
    for i in data:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    # if only same letters in data like 'dddddd' 
    if len(freq) == 1:
        huffmanDict = {data[0] : '0'}
    else:
        freq = sorted(freq.items(), key=lambda x:-x[1])
        nodes = freq
        
        # we can also use heap to more efficiently perform this algorithm
        while len(nodes) > 1:
            (key1, val1) = nodes[-1]
            (key2, val2) = nodes[-2]
            nodes = nodes[:-2]
            node = huffmanTree(key1, key2)
            nodes.append((node, val1+val2))
            nodes = sorted(nodes, key=lambda x:-x[1])
        huffmanDict = tree(nodes[0][0])
        
    huffmanCode = ""
    for char in data:
        huffmanCode += huffmanDict[char]
        
    return huffmanCode, huffmanDict

def huffman_decoding(data,tree):
    decodedData = ""
    while len(data) > 0:
        for char in tree:
            code = tree[char]
            if data.startswith(code):
                decodedData += char
                data = data[len(code)]
    return decodedData
    

def helperTest(data):
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    encoded_data, tree = huffman_encoding(data)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    data = "This is huffman encoding and decoding."
    helperTest(data)
    
    data = "DDDDDD"
    helperTest(data)
    
    data = "Other types of encoding and decoding techniques."
    helperTest(data)
    
