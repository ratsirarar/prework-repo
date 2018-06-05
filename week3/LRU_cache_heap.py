class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
# class PriorityQueue(object):
#     root = None
#     last = None
#     def add(self, key):
#         if not self.root:
#             self.root = self.Node(key)
#         else:
            
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.cache = {}
        self.root = None
        self.last = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        res = -1
        if key in self.cache:
            node = self.cache[key]
            self.update_order(node)
            res = self.cache[key].value
        return res
    
    
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_order(node)
        else:
            node = Node(key, value)
            if self.is_full():
                self.top()
            self.cache[key] = node
            self.append(node)
            
    def print_d(self):
        node = self.root
        res = []
        while node:
            res.append(node.key)
            node = node.next
        return res
    
    def top(self):
        del(self.cache[self.root.key])
        if self.root.next:
            self.root = self.root.next
            self.root.prev = None
        else:
            self.root = None
            self.last = None
    
    def append(self, node):
        if not self.root:
            self.root = node
            self.last = node
        else:
            curr_last = self.last
            curr_last.next = node
            node.next = None
            node.prev = curr_last
            self.last = node
        
    def update_order(self, node):
        if self.last.key == node.key:
            return
        if node.prev != None:
            node.prev.next = node.next  
        if node.next != None:
            node.next.prev = node.prev
            if node == self.root:
                self.root = node.next
        self.append(node)
    
    def is_full(self):
        return len(self.cache) >= self.size
