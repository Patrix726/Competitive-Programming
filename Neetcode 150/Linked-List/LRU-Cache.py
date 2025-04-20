class Node:
    def __init__(self,key:int, val:int,prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_head = None
        self.lru_tail = None
        self.store = {}
        

    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            parent = node.prev
            if parent:
                parent.next = node.next
                if node.next:
                    node.next.prev = parent
                else:
                    self.lru_tail = parent
                node.next = self.lru_head
                if node.next:
                    node.next.prev = node
            node.prev = None
            self.lru_head = node
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.val = value
            parent = node.prev
            if parent:
                parent.next = node.next
                if node.next:
                    node.next.prev = parent
                else:
                    self.lru_tail = parent
                node.next = self.lru_head
                if node.next:
                    node.next.prev = node
            node.prev = None
            self.lru_head = node
            return
        node = Node(key=key, val=value,next=self.lru_head)
        if self.lru_head:
            self.lru_head.prev = node
        self.lru_head = node
        if not self.lru_tail:
            self.lru_tail = node
        if len(self.store) >= self.capacity:
            del self.store[self.lru_tail.key]
            parent = self.lru_tail.prev
            if parent:
                parent.next = None
            del self.lru_tail
            self.lru_tail = parent
        self.store[key] = node
        
        
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
