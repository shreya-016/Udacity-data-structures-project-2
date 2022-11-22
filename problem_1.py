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
            self.lruKey = key
            return self.cache[key]
        return -1

    def put(self, key, value):
        if self.cacheSize == self.capacity:
            self.cache.pop(self.lruKey)
            self.cacheSize -= 1

        if key in self.cache:
            self.cache[key] = value
            self.lruKey = key

        else:
            self.cache[key] = value
            self.cacheSize += 1
            self.lruKey = key
            
    def getLruKey(self):
        return self.lruKey
            
cache = LRU_Cache(5)

cache.put('a', 'apple')
cache.put('b', 'ball')
cache.put('c', 'cat')
cache.put('d', 'dog')

print(cache.getLruKey)

print(cache.get('a'))
print(cache.get('c'))   
print(cache.get('t'))

cache.put('j', 'jack')

print(cache.get('j'))

cache.put('c', 'cache')
cache.put('l', 'lost')
cache.put('j', 'jasmine')

print(cache.get('j'))
print(cache.get('c'))
