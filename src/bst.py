import Trees

# BST or a Binary Search Tree is a type of tree data structure in which,
# left_node.value < parent_node.value < right_node.value

def insert(root, key):
    """
    Insert a key into a binary tree rooted at 'root'.

    Parameters:
    - root: The root of the binary tree to insert the key into.
    - key: The value to be inserted into the binary tree.

    Returns:
    The root of the modified binary tree after the key is inserted.

    Note:
    This function inserts a new node with the given key into a binary tree. If the key is already present, it will not create a duplicate.
    
    Example:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    key = 7
    result = insert(root, key)
    # Result: The root of the modified tree with a new node containing value 7.
    """
    if root is None:
        return Trees.node(key)

    if root.val < key:
        root.right = insert(root.right, key)
    elif root.val > key:
        root.left = insert(root.left, key)

    return root

def search(root, key):
    """
    Search for a key in a binary tree rooted at 'root'.

    Parameters:
    - root: The root of the binary tree to search in.
    - key: The value to search for in the binary tree.

    Returns:
    If the key is found in the binary tree:
    Returns the node with the matching key.
    
    If the key is not found in the binary tree:
    Returns None.

    Note:
    This function performs a binary search on a binary tree to find a specific key.
    If the key exists in the tree, the function returns the node containing the key.
    If the key is not found, it returns None.

    Example:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    key = 5
    result = search(root, key)
    # Result: Node with value 5
    """
    if root is None or root.val == key:
        return root

    if root.val > key:
        return search(root.left, key)
    else:
        return search(root.right, key)


if __name__ == '__main__':
    root = Trees.node(1)
    for i in range(2, 8):
        insert(root, i)
    if search(root, 11) is not None:
        print('found')
    else:
        print('not found')