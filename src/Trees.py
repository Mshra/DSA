from collections import deque


'''
Basic operations in tree data structure
1. Create: 
2. Insert:
3. Search:
4. Traversal
    1. Depth first search
        1. Preorder:
        2. In-order:
        3. Post-order:
    2. Breadth first search

provides efficient searching[O(log n)]
High in memory usage 
recursion friendly
'''
class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left 
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

# inorder, preorder and postorder are depth first search traversal techniques(DFS)
def inorder(root):
    '''
    1. traverse left subtree 
    2. visit root 
    3. traverse right subtree
    
    use: In case of BST, inorder traversal tree gives nodes in decreasing order, for increasing reverse the algorithm
    '''
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    '''
    1. visit root
    2. traverse left subtree
    3. traverse right subtree

    use: used to create copy of tree
    '''
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    '''
    1. traverse left subtree
    2. traverse right subtree
    3. visit root
    '''
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

# Level order traversal or breadth first search(BFS)
def levelorder(root):
    '''
    For each node, first, the node is visited and then it's child nodes are put in a FIFO queue. Then again the first node is popped out and then it's child nodes are put in a FIFO queue and repeat until queue becomes empty.
    '''
    if root:
        queue = deque()
        queue.append(root)

        while len(queue):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            print(node.val)

def height(root):
    if not root:
        return 0 
    else:
        return 1 + max(height(root.left), height(root.right)) 

if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    root.left = node1
    root.right = node2
    root.left.left= node3
    root.left.right = node4

    print(height(root))
