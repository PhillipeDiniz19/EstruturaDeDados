class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        removed_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def display(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.value)
            current = current.next
        return elements

# Testando o código conforme as instruções
queue = Queue()

print("Dequeue:", queue.dequeue())  # Dequeue quando a fila está vazia

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("Tamanho da lista:", queue.display())  # Mostra todos os elementos da fila

print("Valor final do elemento:", queue.dequeue())  # Desenfileira um elemento

print("Primeiro elemento da fila:", queue.peek())  # Mostra o primeiro elemento da fila

print("Valor final do elemento:", queue.dequeue())  # Desenfileira um elemento

print("Tamanho da lista:", queue.display())  # Mostra todos os elementos da fila
