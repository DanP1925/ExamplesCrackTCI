from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


def print_kth_to_last(n, k):
    if n is None:
        return 0
    index = print_kth_to_last(n.next, k) + 1
    if index == k:
        print(n.data)
    return index


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = LinkedNode(1)
    linked_list.head.append_to_tail(3)
    linked_list.head.append_to_tail(5)
    linked_list.head.append_to_tail(7)
    linked_list.head.append_to_tail(9)
    linked_list.list_print()
    print_kth_to_last(linked_list.head, 2)
