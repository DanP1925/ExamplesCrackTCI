from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


def partition(head, value):
    n = head
    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while n is not None:
        next = n.next
        n.next = None
        if n.data < value:
            if before_start is None:
                before_start = n
                before_end = before_start
            else:
                before_end.next = n
                before_end = n
        else:
            if after_start is None:
                after_start = n
                after_end = after_start
            else:
                after_end.next = n
                after_end = n
        n = next

    if before_start is None:
        return

    before_end.next = after_start


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = LinkedNode(3)
    linked_list.head.append_to_tail(5)
    linked_list.head.append_to_tail(8)
    linked_list.head.append_to_tail(5)
    linked_list.head.append_to_tail(10)
    linked_list.head.append_to_tail(2)
    linked_list.head.append_to_tail(1)
    linked_list.list_print()
    partition(linked_list.head, 5)
    linked_list.list_print()
