class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Top of the stack

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def push(self, data):
        """Push an element onto the stack."""
        new_node = Node(data)
        new_node.next = self.top  # Point the new node to the current top
        self.top = new_node       # Update the top to the new node

    def pop(self):
        """Pop an element from the stack."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_data = self.top.data  # Get data from the top node
        self.top = self.top.next     # Move the top pointer to the next node
        return popped_data

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def display(self):
        """Display all elements in the stack."""
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack:", stack.display())
print("Top element:", stack.peek()) 
print("Popped element:", stack.pop())
print("Stack after pop:", stack.display())
