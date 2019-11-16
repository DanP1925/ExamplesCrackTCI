from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


def delete_middle_node(node):
    if node is None or node.next is None:
        return False
    node.data = node.next.data
    node.next = node.next.next
    return True


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = LinkedNode('a')
    linked_list.head.append_to_tail('b')
    linked_list.head.append_to_tail('c')
    n = linked_list.head
    while n.next is not None:
        n = n.next
    linked_list.head.append_to_tail('d')
    linked_list.head.append_to_tail('e')
    linked_list.head.append_to_tail('f')
    linked_list.list_print()
    delete_middle_node(n)
    linked_list.list_print()
