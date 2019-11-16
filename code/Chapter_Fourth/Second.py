from Chapter_Fourth.TreeNode import TreeNode


def create_minimal_bst(values, start, end):
    if end < start:
        return None
    mid = round((start + end) / 2)
    n = TreeNode(values[mid])
    n.left = create_minimal_bst(values, start, mid - 1)
    n.right = create_minimal_bst(values, mid + 1, end)
    return n


def create_bst(values):
    return create_minimal_bst(values, 0, len(values) - 1)


def print_tree(tree):
    if tree is None:
        return
    print(tree.value)
    print_tree(tree.left)
    print_tree(tree.right)


if __name__ == "__main__":
    tree = create_bst([1, 3, 5, 6, 7, 9, 10])
    print_tree(tree)
