# Blockchain
import hashlib 
import datetime 

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode()
        sha.update(hash_str)
        return sha.hexdigest
    
class BlockNode:
    def __init__(self, data, previousHash):
        self.block = Block(data, previousHash)
        self.next = None
    
class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def appendBlock(self, data):
        previousHash = 0 if self.tail is None else self.tail.block.hash
        nextNode = BlockNode(data, previousHash)
        
        if not self.head:
            self.head = nextNode
            self.tail = self.head
            return
        
        self.tail.next = nextNode
        self.tail = nextNode
        
    def printBlockchain(self):
        if not self.head:
            print("blockchian is empty")
            return
        
        start = self.head
        count = 1
        while start:
            data = start.block.data
            time = start.block.timestamp
            previousHash = start.block.previous_hash
            Hash = start.block.hash
            
            print(f'Block: {count}, Data: {data}, Time: {time}, \
                \nSHA256 Hash: {hash}, \nPrevious Hash: {previousHash}\n')
            
            count += 1
            start = start.next
        

data = "block 1"
block = Block(data, 0)
print(block.data, block.hash)
print()

data = "blocknode"
blocknode = BlockNode(data, 0)
print(blocknode.block.data, blocknode.block.hash)
print()

blockchain = Blockchain()
blockchain.appendBlock("text1")
blockchain.appendBlock("text2")
blockchain.appendBlock("text3")

blockchain.printBlockchain()
