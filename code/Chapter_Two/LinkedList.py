class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            node = node.next
        print()

    def size(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result
