from collections import deque

def verifica_palindromo(s):
    fila = deque(s)
    esquerda = 0
    direita = len(fila) - 1

  
    while esquerda < direita:
        if fila[esquerda] != fila[direita]:
            return False   
        esquerda += 1
        direita -= 1
    return True

entrada = input("Digite a string para verificar se é um palíndromo: ").strip()

if verifica_palindromo(entrada):
    print(f"A string '{entrada}' é um palíndromo.")
else:
    print(f"A string '{entrada}' não é um palíndromo.")
