class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node is not None

        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


bst = BinarySearchTree()

produtos = [70, 4, 90, 2, 83, 23, 72, 15, 114, 85, 63, 116, 89]
for produto in produtos:
    bst.insert(produto)


valores_para_pesquisar = [85, 25, 63, 90, 100,116] # valores da arvore.

for valor in valores_para_pesquisar:
    if bst.search(valor):
        print(f"Produto {valor} está disponível.")
    else:
        print(f"Produto {valor} não está disponível.")
