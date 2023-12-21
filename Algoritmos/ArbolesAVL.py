class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def binary_search(root, key):
    # Base case: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return binary_search(root.right, key)

    # Key is smaller than root's key
    return binary_search(root.left, key)

# Driver code
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

key = 15
result = binary_search(root, key)
if result:
    print(f"Elemento {key} encontrado")
else:
    print(f"Elemento {key} no encontrado")
