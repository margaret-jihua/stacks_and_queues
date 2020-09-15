class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
        
class Stack:
    def __init__(self):
       self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, new_node):
        self.stack.append(new_node.data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None
    
    def size(self):
        return len(self.stack)

    def __len__(self):
        return self.size()

    def is_empty(self):
        return len(self.stack) == 0

myStack = Stack()
myStack.push(Node('lettures'))
myStack.push(Node('patty'))
print(myStack)

myStack.pop()
print(myStack)

myStack.push(Node('Tomato'))
print(myStack)

print(myStack.size())
print(myStack.is_empty())