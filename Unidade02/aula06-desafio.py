class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def find_pairs_with_sum(self, target_sum):
        pairs = []
        current = self.head
        while current:
            complement = target_sum - current.data
            search = current.next
            while search:
                if search.data == complement:
                    pairs.append((search.data, current.data))  # Invertendo a ordem
                search = search.next
            current = current.next
        return pairs

# Exemplo de uso
dll = DoublyLinkedList()
prices = [1, 2, 4, 5, 6, 8, 9]
for price in prices:
    dll.append(price)

pairs = dll.find_pairs_with_sum(7)
print(pairs)  # Saída esperada: [(6, 1), (5, 2)]
