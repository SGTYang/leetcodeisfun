class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.dict = {}
        
    def length(self):
        return len(self.dict)
    
    def pop(self, val):
        if val in self.dict:
            node = self.dict[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.dict.pop(val, None)
        
    def push_right(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.dict[val] = node
        self.right.prev = node
        node.prev.next = node
    
    def pop_left(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res
    
    def update(self, val):
        self.pop(val)
        self.push_right(val)
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfu_cnt = 0
        self.val_dict = {} # dict key -> val
        self.count_dict = collections.defaultdict(int) # dict key -> count
        self.list_dict = collections.defaultdict(LinkedList)
    
    def counter(self, key):
        cnt = self.count_dict[key]
        self.count_dict[key] += 1
        self.list_dict[cnt].pop(key)
        self.list_dict[cnt+1].push_right(key)
        
        if cnt == self.lfu_cnt and self.list_dict[cnt].length() == 0:
            self.lfu_cnt += 1

    def get(self, key: int) -> int:
        if key not in self.val_dict:
            return -1
        self.counter(key)
        return self.val_dict[key]
        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.val_dict and len(self.val_dict) == self.cap:
            res = self.list_dict[self.lfu_cnt].pop_left()
            self.val_dict.pop(res)
            self.count_dict.pop(res)
            
        
        self.val_dict[key] = value
        self.counter(key)
        self.lfu_cnt = min(self.lfu_cnt, self.count_dict[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)