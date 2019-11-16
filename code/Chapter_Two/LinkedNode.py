class LinkedNode:
    def __init__(self, data):
        self.next = None
        self.data = data

    def append_to_tail(self, data):
        end = LinkedNode(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def size(self):
        result = 0
        node = self
        while node is not None:
            result += 1
            node = node.next
        return result
