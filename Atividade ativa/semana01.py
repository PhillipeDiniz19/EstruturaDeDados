class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def show(self):
        current = self.head
        index = 0
        while current:
            print(f"Indice {index} Valor: {current.data}")
            current = current.next
            index += 1

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def delete_data(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def insert_at_index(self, data, index):
        if index < 0:
            return False
        if index == 0:
            self.insert_at_begin(data)
            return True
        current = self.head
        for _ in range(index - 1):
            if not current:
                return False
            current = current.next
        if not current:
            return False
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        return True

    def delete_at_index(self, index):
        if index < 0 or not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                return False
            current = current.next
        if not current.next:
            return False
        current.next = current.next.next
        return True

# Criação de uma instância da ListaEncadeada
lista1 = ListaEncadeada()

# Passo-a-passo de testes
lista1.insert_at_begin(10)
lista1.insert_at_begin(20)
lista1.insert_at_begin(30)
lista1.insert_at_begin(40)
print("Mostrar lista:")
lista1.show()
print("Tamanho da lista:", lista1.size())
print("Buscar elemento 40:", lista1.search(40))
print("Buscar elemento 50:", lista1.search(50))
print("Deletar elemento 20:", lista1.delete_data(20))
print("Deletar elemento no índice 0:", lista1.delete_at_index(0))
print("Inserir valor 50 no índice 0:", lista1.insert_at_index(50, 0))
print("Inserir valor 60 no índice 3:", lista1.insert_at_index(60, 3))
print("Mostrar lista final:")
lista1.show()
