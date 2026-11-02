class Node: #holder class
    def __init__(self, key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache={} #map key to node

        self.head=Node(0,0) 
        self.tail=Node(0,0) 
        self.head.next=self.tail
        self.tail.prev=self.head

    def _remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def _add_to_front(self, node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node

    def get(self, key):
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
            node=Node(key,value)
            self._add_to_front(node)
            self.cache[key]=node
        else:
            if len(self.cache)>=self.capacity:
                lru=self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            node=Node(key,value)
            self._add_to_front(node)
            self.cache[key]=node
