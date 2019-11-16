from Chapter_Fourth.TreeNode import TreeNode
from Chapter_Two.LinkedNode import LinkedNode


def list_depth(tree):
    result = list()
    current = None
    if tree is not None:
        current = LinkedNode(tree)
    while current is not None and current.size() > 0:
        result.append(current)
        parents = current
        for i in range(0, parents.size()):
            node = parents
            for j in range(0, i - 1):
                node = node.next
            current = None
            if node.data.left is not None:
                if current is None:
                    current = LinkedNode(node.data.left)
                else:
                    current.next = LinkedNode(node.data.left)
            if node.data.right is not None:
                if current is None:
                    current = LinkedNode(node.data.right)
                else:
                    current.next = LinkedNode(node.data.right)
    return result


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
        print(list.size())
        '''
        node = list.data
        while node is not None:
            print(node.value, " ")
            node = node.next
        print()
        '''
