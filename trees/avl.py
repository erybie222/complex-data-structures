from .bst import BSTNode

def build_avl_from_sorted_array(array):
    if not array:
        return None
    mid = len(array) // 2
    root = BSTNode(array[mid])

    root.left = build_avl_from_sorted_array(array[:mid])
    root.right = build_avl_from_sorted_array(array[mid+1:])

    return root