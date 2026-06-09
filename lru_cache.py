class Node:
    def __init__(self, key, value):
        self.key   = key
        self.value = value
        self.prev  = None
        self.next  = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache    = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        node.next           = self.head.next
        node.prev           = self.head
        self.head.next.prev = node
        self.head.next      = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


# ─── TEST ─────────────────────────────────
print("=" * 40)
print("LRU CACHE (capacity = 3)")
print("=" * 40)
cache = LRUCache(3)
cache.put(1, 10); print("put(1, 10)")
cache.put(2, 20); print("put(2, 20)")
cache.put(3, 30); print("put(3, 30)")
print("get(1)  →", cache.get(1))
cache.put(4, 40); print("put(4, 40)  ← evicts key 2")
print("get(2)  →", cache.get(2))
print("get(3)  →", cache.get(3))
cache.put(5, 50); print("put(5, 50)  ← evicts key 4")
print("get(4)  →", cache.get(4))