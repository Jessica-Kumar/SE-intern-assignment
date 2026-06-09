import threading

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

class ThreadSafeLRUCache(LRUCache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self._lock = threading.RLock()

    def get(self, key):
        with self._lock:
            return super().get(key)

    def put(self, key, value):
        with self._lock:
            super().put(key, value)

# ─── TEST ─────────────────────────────────
print("=" * 40)
print("THREAD-SAFE LRU CACHE (capacity = 3)")
print("=" * 40)
cache = ThreadSafeLRUCache(3)
cache.put(1, 100); print("put(1, 100)")
cache.put(2, 200); print("put(2, 200)")
cache.put(3, 300); print("put(3, 300)")
print("get(1)  →", cache.get(1))
cache.put(4, 400); print("put(4, 400)  ← evicts key 2")
print("get(2)  →", cache.get(2))
print("get(3)  →", cache.get(3))
print("get(4)  →", cache.get(4))