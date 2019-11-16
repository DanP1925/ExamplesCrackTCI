from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


def remove_duplicates(linked_list):
    current = linked_list.head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


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
