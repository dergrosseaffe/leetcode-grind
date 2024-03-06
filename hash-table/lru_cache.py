class Node:

    def __init__(self, key: int, data: int):
        self.key = key
        self.val = data
        self.next = None
        self.prev = None


class LRUCache:

    def _remove_node(self, node: Node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode


    def _add_node(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


    def __init__(self, capacity: int):
        self.map      = {}
        self.capacity = capacity
        self.head     = Node(-1, -1)
        self.tail     = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove_node(node)
            self._add_node(node)

            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)

        if not node:
            node = Node(key, value)
            self._add_node(node)
            self.map[key] = node

            if len(self.map) > self.capacity:
                # removes LRU key
                lru = self.tail.prev
                self._remove_node(lru)
                del self.map[lru.key]
        else:
            node.val = value
            self._remove_node(node)
            self._add_node(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)