from trees.bst import BinarySearchTree

if __name__ == "__main__":
    tree = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14]:
        tree.insert(value)

    print("Inorder:", tree.inorder())      # [1, 3, 6, 8, 10, 14]
    print("Find 6:", tree.find(6))         # True
    print("Find 100:", tree.find(100))     # False
    print("delete 6:", tree.delete(6))    
    print("Inorder:", tree.inorder())      # [1, 3, 6, 8, 10, 14]
