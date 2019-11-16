from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


class Index:

    def __init__(self):
        self.value = 0


def print_kth_to_last(head, k, idx):
    if head is None:
        return None
    node = print_kth_to_last(head.next, k, idx)
    idx.value = idx.value + 1
    if idx.value == k:
        return head
    return node


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = LinkedNode(1)
    linked_list.head.append_to_tail(3)
    linked_list.head.append_to_tail(5)
    linked_list.head.append_to_tail(7)
    linked_list.head.append_to_tail(9)
    linked_list.list_print()
    print(print_kth_to_last(linked_list.head, 2, Index()).data)
