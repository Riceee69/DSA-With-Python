class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current_node = self.root
            new_node = Node(value)

            while(True):
                # right
                if value > current_node.value:
                    if current_node._right == None:
                        current_node._right = new_node
                        break
                    else:
                        current_node = current_node._right
                # left
                else:
                    if current_node._left == None:
                        current_node._left = new_node
                        break
                    else:
                        current_node = current_node._left

    def lookup(self, value):
        if not self.root:
            return None
        
        current_node = self.root
        while(current_node):
            if value > current_node.value:
                current_node = current_node._right
            elif value < current_node.value:
                current_node = current_node._left
            elif value == current_node.value:
                return current_node
        return None

    def remove(self, value) -> bool:
        if not self.root:
            return False

        current_node = self.root
        parent_node = None
        while(current_node):
            if value > current_node.value:
                parent_node = current_node
                current_node = current_node._right
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node._left
            # Found the Node to be deleted
            elif value == current_node.value:
                # Option 1: If Current Node Has No Right Child
                if current_node._right == None:
                    # If the root is being deleted
                    if parent_node == None:
                        self.root = current_node._left
                    else:
                        if current_node.value < parent_node.value:
                            parent_node._left = current_node._left
                        else:
                            parent_node._right = current_node._left

                # Option 2: If Current Node Right Child has No Left Child
                elif current_node._right._left == None:
                    current_node._right._left = current_node._left
                    if parent_node == None:
                        self.root = current_node._right
                    else:
                        if current_node.value < parent_node.value:
                            parent_node._left = current_node._right
                        else:
                            parent_node._right = current_node._right                       

                #Option 3: If Current Node Right Child Has a Left Child
                else:
                    # Step 1: Find the Right Child's left most parent and child
                    # Basically Finding the Smallest - Largest Value to Replace the Current/Target Node
                    leftmost_parent = current_node._right
                    leftmost_child = leftmost_parent._left
                    while(leftmost_child._left):
                        leftmost_parent = leftmost_child
                        leftmost_child = leftmost_child._left

                    # Step 2: Left most child's right Node is handed over to it's parent
                    leftmost_parent._left = leftmost_child._right
                    # Step 3: The left most child replaces the current node
                    leftmost_child._left = current_node._left
                    leftmost_child._right = current_node._right

                    # Finally, handle the parent node referencing
                    if parent_node == None:
                        self.root = leftmost_child
                    else:
                        if current_node.value < parent_node.value:
                            parent_node._left = leftmost_child
                        else:
                            parent_node._right = leftmost_child
                return True
        return False


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print_tree(node._right, level + 1, "R: ")
        print("    " * level + prefix + str(node.value))
        print_tree(node._left, level + 1, "L: ")

def inorder(node):
    if node is not None:
        inorder(node._left)
        print(node.value, sep=',', end=" ")
        inorder(node._right)