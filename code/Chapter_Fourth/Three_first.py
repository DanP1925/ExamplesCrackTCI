from Chapter_Fourth.TreeNode import TreeNode
from Chapter_Two.LinkedList import LinkedList
from Chapter_Two.LinkedNode import LinkedNode


def create_level_linked_list(tree, node_lists, level):
    if tree is None:
        return
    node_list = None

    if len(node_lists) == level:
        node_list = LinkedList()
        node_lists.append(node_list)
    else:
        node_list = node_lists[level]

    if node_list.head is None:
        node_list.head = LinkedNode(tree.value)
    else:
        node_list.head.append_to_tail(tree.value)

    create_level_linked_list(tree.left, node_lists, level + 1)
    create_level_linked_list(tree.right, node_lists, level + 1)


def list_depth(tree):
    node_lists = list()
    create_level_linked_list(tree, node_lists, 0)
    return node_lists


if __name__ == "__main__":
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n0.left = n1
    n2 = TreeNode(2)
    n1.left = n2
    n3 = TreeNode(3)
    n0.right = n3
    n4 = TreeNode(4)
    n2.left = n4
    lists = list_depth(n0)
    for list in lists:
        node = list.head
        while node is not None:
            print(node.data, " ")
            node = node.next
        print()
