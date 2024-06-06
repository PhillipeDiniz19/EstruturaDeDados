class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        removed_value = self.top.value
        self.top = self.top.next
        return removed_value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def display(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def is_empty(self):
        return self.top is None

# Testando o código conforme as instruções
stack = Stack()

print("Pop:", stack.pop())  # Pop quando a pilha está vazia
print("IsEmpty:", stack.is_empty())  # Verifica se a pilha está vazia

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("Display after pushes:", stack.display())  # Mostra todos os elementos da pilha

print("Pop:", stack.pop())  # Desempilha um elemento

print("Top:", stack.peek())  # Mostra o elemento do topo da pilha

print("Pop:", stack.pop())  # Desempilha um elemento

print("Display after pops:", stack.display())  # Mostra todos os elementos da pilha
