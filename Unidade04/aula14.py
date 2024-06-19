class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Função para imprimir todos os nós da arvore
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=' ')
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

# Função para calcular a altura da árvore
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

# Função para imprimir a árvore.
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
        print()  

# Função principal para testar o código
if __name__ == '__main__':
    # Exemplos para construir a arvore
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Caminhamento em ordem de nível da árvore binária é:")
    printLevelOrder(root)
