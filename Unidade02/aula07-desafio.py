import random

class Carta:
    def __init__(self, naipe, valor, virada_para_cima=True):
        self.naipe = naipe
        self.valor = valor
        self.virada_para_cima = virada_para_cima

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Pilha:
    def __init__(self):
        self.cartas = []

    def adicionar_carta(self, carta):
        self.cartas.append(carta)

    def __str__(self):
        if self.cartas:
            return str(self.cartas[-1])  # Mostra apenas a carta do topo
        else:
            return "[Vazio]"

def distribuir_cartas():
    baralho = []
    naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
    valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

    for naipe in naipes:
        for valor in valores:
            baralho.append(Carta(naipe, valor))

    random.shuffle(baralho)

    pilhas = [Pilha() for _ in range(8)]

    for i in range(7):
        for j in range(i + 1):
            pilhas[i].adicionar_carta(baralho.pop())

    for _ in range(len(baralho)):
        pilhas[7].adicionar_carta(baralho.pop())

    return pilhas

def exibir_mesa(pilhas):
    print("Configuração atual da mesa:")
    for i, pilha in enumerate(pilhas):
        print(f"Pilha {i + 1}: {pilha}")
    print("")

# Criar as pilhas e distribuir as cartas
pilhas = distribuir_cartas()

# Exibir a configuração atual da mesa
exibir_mesa(pilhas)
