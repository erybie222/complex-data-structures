# drzewa/bst.py

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Wstawia nowy element do drzewa BST"""
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        if value > node.value:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
            
    def find(self, value):
        """Zwraca True jeśli wartość istnieje w drzewie"""
        if self.root is None:
            return False
        else:
            return self._find_recursive(self.root, value)

    def _find_recursive(self, node, value):
        if node is None:
            return False
        elif node.value == value:
                return True
        elif node.value > value:
            return self._find_recursive(node.left, value)
        else:
            return self._find_recursive(node.right, value)

    def delete(self, value):
      self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left , value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right , value)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node


    def inorder(self):
       return self._inorder_recursive(self.root)
    
    def _inorder_recursive(self, node):
        if node is None:
            return []
        return (
            self._inorder_recursive(node.left) + [node.value] + self._inorder_recursive(node.right) 
        )