from trees.bst import BinarySearchTree
from trees.tree_utils import tree_height
from data.gerenator import generate_unique_numbers
if __name__ == "__main__":

    tree = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14]:
        tree.insert(value)

    print("Inorder:", tree.inorder())
    print("Wysokość drzewa:", tree_height(tree.root))
    print(generate_unique_numbers(5, seed=123))