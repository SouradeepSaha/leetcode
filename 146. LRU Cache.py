# 146. LRU Cache using Dictionary and Doubly Linked List

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class LRUCache:
    def insert_front(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.tail is self.head:
            self.tail.left = node
            node.right = self.tail
            self.head = node
        else:
            self.head.left = node
            node.right = self.head
            self.head = node

    def pop(self, node: Node):
        if node is self.head and self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.right
            self.head.left = None
        elif node is self.tail:
            self.tail = node.left
            self.tail.right = None
        else:
            left = node.left
            right = node.right
            node.left.right = right
            node.right.left = left

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.tail = None
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        cur = self.cache[key]
        newnode = Node(key)
        self.pop(cur["ref"])
        self.insert_front(newnode)
        cur["ref"] = newnode

        return cur["val"]

    def put(self, key: int, value: int) -> None:
        newNode = Node(key)
        if key in self.cache:
            self.pop(self.cache[key]["ref"])
            self.length -= 1

        elif self.length == self.capacity:
            del self.cache[self.tail.key]
            self.pop(self.tail)
            self.length -= 1

        self.insert_front(newNode)
        self.cache[key] = {"val": value, "ref": newNode}
        self.length += 1
