class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.cabeca = None

    def esta_vazia(self):
        return self.cabeca is None

    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            novo_no.proximo = novo_no.anterior = novo_no
            self.cabeca = novo_no
        else:
            cauda = self.cabeca.anterior
            novo_no.proximo = self.cabeca
            novo_no.anterior = cauda
            cauda.proximo = self.cabeca.anterior = novo_no
            self.cabeca = novo_no

    def inserir_no_final(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            novo_no.proximo = novo_no.anterior = novo_no
            self.cabeca = novo_no
        else:
            cauda = self.cabeca.anterior
            cauda.proximo = novo_no
            novo_no.anterior = cauda
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no

    def inserir_no_indice(self, indice, dado):
        if indice == 0:
            self.inserir_no_inicio(dado)
        else:
            novo_no = No(dado)
            atual = self.cabeca
            for _ in range(indice - 1):
                if atual.proximo == self.cabeca:
                    return False
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            novo_no.anterior = atual
            atual.proximo.anterior = novo_no
            atual.proximo = novo_no

    def remover_do_inicio(self):
        if not self.esta_vazia():
            if self.cabeca.proximo == self.cabeca:
                self.cabeca = None
            else:
                cauda = self.cabeca.anterior
                self.cabeca = self.cabeca.proximo
                self.cabeca.anterior = cauda
                cauda.proximo = self.cabeca

    def remover_do_final(self):
        if not self.esta_vazia():
            if self.cabeca.proximo == self.cabeca:
                self.cabeca = None
            else:
                cauda = self.cabeca.anterior
                cauda.anterior.proximo = self.cabeca
                self.cabeca.anterior = cauda.anterior

    def remover_do_indice(self, indice):
        if not self.esta_vazia():
            if indice == 0:
                self.remover_do_inicio()
            else:
                atual = self.cabeca
                for _ in range(indice):
                    if atual.proximo == self.cabeca:
                        return False
                    atual = atual.proximo
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior

    def mostrar(self):
        if self.esta_vazia():
            print("Lista vazia")
            return
        atual = self.cabeca
        print("Início ->", end=" ")
        while True:
            print(atual.dado, end=" <-> ")
            atual = atual.proximo
            if atual == self.cabeca:
                break
        print("Fim")

# Criação de uma instância da ListaDuplamenteEncadeadaCircular
lista = ListaDuplamenteEncadeadaCircular()

# Testes de Inserção
lista.inserir_no_inicio(10)
lista.inserir_no_inicio(20)
print("Inserção no início:")
lista.mostrar()
lista.inserir_no_final(30)
print("Inserção no final:")
lista.mostrar()
lista.inserir_no_indice(1, 15)
print("Inserção em um índice específico:")
lista.mostrar()

# Testes de remoção
lista.remover_do_inicio()
print("Remoção no início:")
lista.mostrar()
lista.remover_do_final()
print("Remoção no final:")
lista.mostrar()
lista.inserir_no_final(25)
print("Inserção no final:")
lista.mostrar()
lista.remover_do_indice(1)
print("Remoção em um índice específico:")
lista.mostrar()

# Testes de borda
lista.remover_do_inicio()
lista.remover_do_inicio()
print("Remoção de todos os elementos:")
lista.mostrar()
