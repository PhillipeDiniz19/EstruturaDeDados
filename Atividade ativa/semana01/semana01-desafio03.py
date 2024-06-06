import time
class SimpleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_begin(self, data):
        new_node = SimpleNode(data)
        new_node.next = self.head
        self.head = new_node

    def remove_at_end(self):
        if self.is_empty():
            return
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = self.head.prev = new_node
            self.head = new_node

    def remove_at_end(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            else:
                tail = self.head.prev
                tail.prev.next = self.head
                self.head.prev = tail.prev

# Função que recebe as classes da questão 1 (sll = Single Linked List)
# e questão 2 (dll = Doubly Linked List) e calcula o tempo de testes
# de inserção e exclusão no início e no final das listas.
def tests(sll, dll):
    # Teste de desempenho de inserção no início para lista simplesmente encadeada
    start = time.time()  # Registra o tempo de início
    for i in range(10000):
        sll.insert_at_begin(i)  # Insere 10000 elementos no início da lista
    end = time.time()  # Registra o tempo de término
    print("Tempo de inserção no início (simples):", round(end - start, 5), "(s)")  # Calcula e imprime o tempo total de inserção

    # Teste de desempenho de inserção no início para lista duplamente encadeada
    start = time.time()  # Registra o tempo de início
    for i in range(10000):
        dll.insert_at_begin(i)  # Insere 10000 elementos no início da lista
    end = time.time()  # Registra o tempo de término
    print("Tempo de inserção no início (dupla):", round(end - start, 5), "(s)")  # Calcula e imprime o tempo total de inserção

    # Teste de desempenho de remoção no final para lista simplesmente encadeada
    start = time.time()  # Registra o tempo de início
    for i in range(10000):
        sll.remove_at_end()  # Remove 10000 elementos do final da lista
    end = time.time()  # Registra o tempo de término
    print("Tempo de remoção no final (simples):", round(end - start, 5), "(s)")  # Calcula e imprime o tempo total de remoção

    # Teste de desempenho de remoção no final para lista duplamente encadeada
    start = time.time()  # Registra o tempo de início
    for i in range(10000):
        dll.remove_at_end()  # Remove 10000 elementos do final da lista
    end = time.time()  # Registra o tempo de término
    print("Tempo de remoção no final (dupla):", round(end - start, 5), "(s)")  # Calcula e imprime o tempo total de remoção

# Executa os testes passando instâncias das classes SinglyLinkedList e DoublyLinkedList
tests(SinglyLinkedList(), DoublyLinkedList())
