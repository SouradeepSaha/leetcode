from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key=None, val=None, count = 1):
        self.key = key
        self.val = val
        self.count = count

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_size = 0
        self.nodes = dict() # Contains all the nodes
        self.freq = defaultdict(OrderedDict) # Contains freq-based dictionaries with key
        self.least_freq = 1
        
    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        cur_node = self.nodes[key]
        del self.freq[cur_node.count][key]
        cur_node.count += 1
        self.freq[cur_node.count][key] = cur_node
        if not len(self.freq[self.least_freq]):
            self.least_freq += 1
        return cur_node.val

    def create_new(self, key, value) -> None:
        new_node = Node(key, value)
        self.nodes[key] = new_node
        self.freq[1][key] = new_node
        self.least_freq = 1
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.nodes:
            cur_node = self.nodes[key]
            cur_node.val = value
            del self.freq[cur_node.count][key]
            cur_node.count += 1
            self.freq[cur_node.count][key] = cur_node
            if not len(self.freq[self.least_freq]):
                self.least_freq += 1
            
        elif self.cur_size == self.capacity :
            it = iter(self.freq[self.least_freq])
            last = next(it)
            del self.freq[self.least_freq][last]
            del self.nodes[last]
            self.create_new(key, value)
            
        else:
            self.create_new(key, value)
            self.cur_size += 1
            
            
            
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
