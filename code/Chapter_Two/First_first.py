from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


def remove_duplicates(linked_list):
    hash_set = set()
    previous = None
    n = linked_list.head
    while n is not None:
        if n.data in hash_set:
            previous.next = n.next
        else:
            hash_set.add(n.data)
            previous = n
        n = n.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = LinkedNode("t")
    linked_list.head.append_to_tail("r")
    linked_list.head.append_to_tail("e")
    linked_list.head.append_to_tail("e")
    linked_list.head.append_to_tail("t")
    linked_list.head.append_to_tail("a")
    linked_list.list_print()
    remove_duplicates(linked_list)
    linked_list.list_print()
