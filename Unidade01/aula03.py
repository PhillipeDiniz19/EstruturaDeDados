class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""

    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        nodos = []
        atual = self.cabeca
        while atual:
            nodos.append(str(atual.dado))
            atual = atual.proximo
        return "[" + " -> ".join(nodos) + "]"

    
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

# Desafio da aula 03.

class Produto:
    def __init__(self, codigo=0, proximo_nodo=None):
        self.codigo = codigo
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return "%s -> %s" % (self.codigo, self.proximo)
    
class ListaEncadeada: 
    def __init__(self):
        self.cabeca = None
    
    def __repr__(self):
        return "[ " + str(self.cabeca) + "]"
    
    def AddFinal(self, novoCod):
        novoProduto = Produto(novoCod)
        if not self.cabeca:
            self.cabeca = novoProduto
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novoProduto

# Testar o funcionamento
lista = ListaEncadeada()
print("Lista vazia:", lista)
lista.AddFinal(1111)
print(lista)
lista.AddFinal(2222)
print(lista)

