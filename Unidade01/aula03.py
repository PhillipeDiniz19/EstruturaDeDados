class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
class ListaEncadeada: 
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None
        
    def __repr__(self):
        return "[" + str(self.cabeca) + "]" 
    
def insereNoInicio(lista, novo_dado):
    # 1) Cria um novo nodo com dado a ser armazenado.
    novoNodo = NodoLista(novo_dado)
    # 2) Faz com que o novo nodo seja a cabeça da lista
    novoNodo.proximo = lista.cabeca
    # 3) Faz com que a cabeça da lista referencie o novo nodo.
    lista.cabeca = novoNodo

lista = ListaEncadeada()
print("Lista vazia:", lista)   
    
insereNoInicio(lista, 5)
print("Lista contém um único elemento:", lista)
    
insereNoInicio(lista, 10)
print("Inserindo um novo elemento:", lista)
