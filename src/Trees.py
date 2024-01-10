from collections import deque


class node:
    """
    Represents a node in a binary tree.

    Attributes:
    - val: The value stored in this node.
    - left: The left child node.
    - right: The right child node.

    Methods:
    - __init__(val, left=None, right=None): Initializes a new node with the given value and optional left and right child nodes.
    - __str__(): Returns a string representation of the node's value.

    Example:
    # Create a node with a value of 10
    my_node = node(10)
    print(my_node)  # Output: "10"
    """

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

# inorder, preorder and postorder are depth first search traversal techniques(DFS)


def inorder(root):
    """
    Perform an in-order traversal of a binary tree rooted at 'root'.

    Parameters:
    - root: The root of the binary tree to traverse.

    Returns:
    None

    Note:
    This function performs an in-order traversal of a binary tree, which means it visits the nodes in the following order: left subtree, current node, right subtree. The values of the nodes are printed to the console with a space between them.

    Example:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    inorder(root)
    # Output: "3 5 7 10 15"
    """
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


def preorder(root):
    """
    Perform a pre-order traversal of a binary tree rooted at 'root'.

    Parameters:
    - root: The root of the binary tree to traverse.

    Returns:
    None

    Note:
    This function performs a pre-order traversal of a binary tree, which means it visits the nodes in the following order: current node, left subtree, right subtree. The values of the nodes are printed to the console with a space between them.

    Example:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    preorder(root)
    # Output: "10 5 3 7 15"
    """
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    """
    Perform a post-order traversal of a binary tree rooted at 'root'.

    Parameters:
    - root: The root of the binary tree to traverse.

    Returns:
    None

    Note:
    This function performs a post-order traversal of a binary tree, which means it visits the nodes in the following order: left subtree, right subtree, current node. The values of the nodes are printed to the console with a space between them.

    Example:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    postorder(root)
    # Output: "3 7 5 15 10"
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

# Level order traversal or breadth first search(BFS)


def bfs(root):
    """
    Perform a breadth-first traversal of a binary tree rooted at 'root'.

    Parameters:
    - root: The root of the binary tree to traverse.

    Returns:
    None

    Note:
    This function performs a breadth-first traversal of a binary tree, which means it visits the nodes level by level, starting from the root. The values of the nodes are printed to the console with a space between them.

    Example:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    bfs(root)
    # Output: "10 5 15 3 7"
    """
    if root:
        queue = deque()
        queue.append(root)

        while len(queue):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            print(node.val, end=' ')


def height(root):
    """
    Calculate the height of a binary tree rooted at 'root'.

    Parameters:
    - root: The root of the binary tree for which you want to determine the height.

    Returns:
    The height of the binary tree.

    Note:
    This function calculates the height of a binary tree, which is defined as the maximum number of edges on the longest path from the root to a leaf node. If the tree is empty (root is None), the height is considered to be 0.

    Example:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    tree_height = height(root)
    # Result: 3 (Longest path: 10 -> 5 -> 7)
    """
    if not root:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


if __name__ == '__main__':
    root = node(10)

    root.left = node(11)
    root.left.left = node(7)
    root.right = node(9)
    root.right.left = node(15)
    root.right.right = node(8)

    print('hello, world')
