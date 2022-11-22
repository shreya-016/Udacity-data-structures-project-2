# LRU Cache
from collections import OrderedDict
        
class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.lruKey = None
        self.cacheSize = 0
        
    def get(self, key):
        if key in self.cache:
            self.lruKey = self.cache[key]
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if self.cacheSize == self.capacity:
            # remove the least recently used cache entry
            #self.cache.pop(self.lruKey)
            del self.cache[key]
            self.cacheSize -= 1
        
        # updating the value if key is present in cache
        if key in self.cache:
            self.cache[key] = value
            self.lruKey = key
        
        if key not in self.cache:
            self.cache[key] = value
            self.cacheSize += 1
            self.lruKey = key
            
            
cache = LRU_Cache(5)

cache.put('a', 'apple')
cache.put('b', 'ball')
cache.put('c', 'cat')
cache.put('d', 'dog')

print(cache.get('a'))
print(cache.get('c'))   
print(cache.get('t'))

cache.put('j', 'jack')

print(cache.get('j'))

cache.put('c', 'cache')
cache.put('j', 'jasmine')

print(cache.get('j'))
print(cache.get('c'))
