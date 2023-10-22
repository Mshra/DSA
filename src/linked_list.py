import time


class node:
    """
    Represents a node in a singly-linked list.

    Attributes:
    - val: The value stored in this node.
    - next: The reference to the next node in the linked list.

    Methods:
    - __init__(val, next=None): Initializes a new node with the given value and optional reference to the next node.
    - __str__(): Returns a string representation of the node's value.

    Example:
    # Create a node with a value of 10
    my_node = node(10)
    print(my_node)  # Output: "10"
    """
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

def search(head, key):
    """
    Search for a key in a singly-linked list starting at 'head'.

    Parameters:
    - head: The head node of the linked list to search.
    - key: The value to search for in the linked list.

    Returns:
    True if the key is found in the linked list; False otherwise.

    Note:
    This function iterates through a singly-linked list starting from the 'head' node and searches for the specified 'key'. It returns True if the key is found in any of the nodes within the list; otherwise, it returns False.

    Example:
    # Create a linked list: 1 -> 3 -> 5 -> 7
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(7)
    key = 5
    result = search(head, key)
    # Result: True (5 is found in the linked list)
    """
    while head:
        if head.val == key:
            return True

        head = head.next
    return False

def insert(head, key):
    """
    Insert a new node with the given 'key' at the end of a singly-linked list starting at 'head'.

    Parameters:
    - head: The head node of the linked list where the new node will be inserted.
    - key: The value to be inserted into the linked list as a new node.

    Returns:
    None

    Note:
    This function iterates through the singly-linked list, starting from the 'head' node, until it reaches the last node. It then adds a new node with the specified 'key' as the next node.

    Example:
    # Create a linked list: 1 -> 3 -> 5
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    key = 7
    insert(head, key)
    # The linked list is now: 1 -> 3 -> 5 -> 7
    """
    while head.next:
        head = head.next

    head.next = node(key)

def insert_after(head, nxt, key):
    """
    Insert a new node with the given 'key' immediately after the node with value 'nxt' in a singly-linked list starting at 'head'.

    Parameters:
    - head: The head node of the linked list where the new node will be inserted.
    - nxt: The value of the node after which the new node will be inserted.
    - key: The value to be inserted into the linked list as a new node.

    Returns:
    None

    Note:
    This function iterates through the singly-linked list, starting from the 'head' node, and searches for a node with the value 'nxt'. Once found, it inserts a new node with the value 'key' immediately after that node.

    Example:
    # Create a linked list: 1 -> 3 -> 5
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    nxt_value = 3
    key = 7
    insert_after(head, nxt_value, key)
    # The linked list is now: 1 -> 3 -> 7 -> 5
    """
    while head:
        if head.val == nxt:
            temp = head.next
            head.next = node(key)
            head.next.next = temp
            return
        head = head.next

def delete(head, key):
    """
    Delete the first occurrence of a node with the specified 'key' from a singly-linked list starting at 'head'.

    Parameters:
    - head: The head node of the linked list from which to delete the node.
    - key: The value to be deleted from the linked list.

    Returns:
    None

    Note:
    This function iterates through the singly-linked list, starting from the 'head' node, and searches for the first occurrence of a node with the value 'key'. Once found, it removes the node from the list by updating the 'next' references.

    Example:
    # Create a linked list: 1 -> 3 -> 5 -> 7
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(7)
    key = 5
    delete(head, key)
    # The linked list is now: 1 -> 3 -> 7
    """
    prev = None
    while head:
        if head.val == key:
            if prev:
                prev.next = head.next
            else:
                # Handle the case where the node to be deleted is the head.
                head = head.next
            return
        prev = head
        head = head.next

def show(head):
    """
    Display the contents of a singly-linked list starting at 'head'.

    Parameters:
    - head: The head node of the linked list to display.

    Returns:
    None

    Note:
    This function iterates through a singly-linked list starting from the 'head' node and displays the values of each node. It prints the values in a format where each value is followed by an arrow (->) unless it's the last node, in which case only the value is printed.

    Example:
    # Create a linked list: 1 -> 3 -> 5 -> 7
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(7)
    show(head)
    # Output: "1 -> 3 -> 5 -> 7"
    """
    while head:
        if head.next is None:
            print(head.val)
        else:
            print(head.val, end=' -> ')
        head = head.next

if __name__ == '__main__':
    head = node(1)
    for i in range(2, 8):
        insert(head, i)