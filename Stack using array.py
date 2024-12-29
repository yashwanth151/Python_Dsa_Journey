class Stack:
    def __init__(self):
        self.stack = []  # Array to hold stack elements

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        return self.stack.pop()

    def peek(self):
        """Return the top item without removing it."""
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

# Example Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())
print(stack.pop())
print(stack.size())
print(stack.is_empty())
