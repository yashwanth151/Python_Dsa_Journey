class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A class to represent a singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first occurrence of a node with the given data."""
        if not self.head:
            return  # List is empty
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:  # Node with the data found
            current.next = current.next.next

    def display(self):
        """Print the linked list elements."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.display()  # Output: 1 -> 2 -> 3 -> None

    sll.prepend(0)
    sll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

    sll.delete(2)
    sll.display()  # Output: 0 -> 1 -> 3 -> None
