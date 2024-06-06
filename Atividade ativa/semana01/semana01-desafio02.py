class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
    
    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next
        
    def get_next(self):
        return self.next
    
class ListaEncadeada:
    def __init__(self):
        self.head = None
    
    def empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def insertAtBegin(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
    
    def insertAtIndex(self, index, data):
        if index < 0 or index > self.size():
            raise IndexError("Índice fora dos limites da lista")
        if index == 0:
            self.insertAtBegin(data)
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Índice fora dos limites da lista")
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
    
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def deleteData(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
    
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Índice fora dos limites da lista")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
    
    def show(self):
        current = self.head
        count = 0
        while current != None:
            print("Índice", count, "valor:", str(current.get_data()))
            current = current.get_next()
            count += 1

# Criando uma lista encadeada e testando os métodos
lista1 = ListaEncadeada()
lista1.insertAtBegin(10)
lista1.insertAtBegin(20)
lista1.insertAtBegin(30)
lista1.insertAtBegin(40)

print("Lista inicial:")
lista1.show()
print("Tamanho da lista:", lista1.size())
print("Pesquisar 40 na lista:", lista1.search(40))
print("Pesquisar 50 na lista:", lista1.search(50))

lista1.deleteData(20)
print("Lista após excluir 20:")
lista1.show()

lista1.deleteAtIndex(0)
print("Lista após excluir o elemento no índice 0:")
lista1.show()


