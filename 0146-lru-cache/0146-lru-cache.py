class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def add(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev
        
        self.right.prev = node
        node.next = self.right
         
    def remove(self, node):
        prev = node.prev 
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.add(self.dict[key])
            return self.dict[key].val
        
        return - 1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        self.dict[key] = Node(key, value)
        self.add(self.dict[key])
        
        if len(self.dict) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.dict[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)