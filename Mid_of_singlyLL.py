class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddleNode(head: ListNode) -> ListNode:
    """
    Finds the middle node of a singly linked list.
    Args:
    head (ListNode): Head of the linked list.
    Returns:
    ListNode: The middle node of the linked list.
    """
    slow = head
    fast = head
    # Move fast pointer two steps and slow pointer one step
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # When fast reaches the end, slow is at the middle
    return slow

def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print("Linked List:", result)



values = [1, 2, 3, 4, 5, 6]
head = create_linked_list(values)
print_linked_list(head)
middle_node = findMiddleNode(head)
print("Middle node value:", middle_node.val)
