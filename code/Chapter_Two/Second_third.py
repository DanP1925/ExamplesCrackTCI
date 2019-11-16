from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


def kth_to_last(head, k):
    first = head
    second = head

    for i in range(0, k):
        if second is None:
            return None
        second = second.next

    while second is not None:
        first = first.next
        second = second.next
    return first.data


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = LinkedNode(1)
    linked_list.head.append_to_tail(3)
    linked_list.head.append_to_tail(5)
    linked_list.head.append_to_tail(7)
    linked_list.head.append_to_tail(9)
    linked_list.list_print()
    print(kth_to_last(linked_list.head, 2))
