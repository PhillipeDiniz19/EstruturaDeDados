import time
import matplotlib.pyplot as plt
import random

# Implementação dos algoritmos de ordenação

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def medir_tempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr)
    fim = time.time()
    return fim - inicio

def plotar_tempos(algoritmos, tamanhos):
    tempos = {alg: {'Melhor Caso': [], 'Caso Médio': [], 'Pior Caso': []} for alg in algoritmos}

    for tamanho in tamanhos:
        melhor_caso = list(range(tamanho))
        caso_medio = random.sample(range(tamanho), tamanho)
        pior_caso = list(range(tamanho, 0, -1))

        for nome, algoritmo in algoritmos.items():
            # Melhor caso
            arr = melhor_caso.copy()
            tempo = medir_tempo(algoritmo, arr)
            tempos[nome]['Melhor Caso'].append(tempo)

            # Caso médio
            arr = caso_medio.copy()
            tempo = medir_tempo(algoritmo, arr)
            tempos[nome]['Caso Médio'].append(tempo)

            # Pior caso
            arr = pior_caso.copy()
            tempo = medir_tempo(algoritmo, arr)
            tempos[nome]['Pior Caso'].append(tempo)

    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    for nome in algoritmos.keys():
        axs[0].plot(tamanhos, tempos[nome]['Melhor Caso'], label=nome)
        axs[1].plot(tamanhos, tempos[nome]['Caso Médio'], label=nome)
        axs[2].plot(tamanhos, tempos[nome]['Pior Caso'], label=nome)

    axs[0].set_title('Melhor Caso')
    axs[1].set_title('Caso Médio')
    axs[2].set_title('Pior Caso')

    for ax in axs:
        ax.set_xlabel('Tamanho da Lista')
        ax.set_ylabel('Tempo (s)')
        ax.legend()

    plt.tight_layout()
    plt.show()

# Algoritmos de ordenação a serem comparados
algoritmos = {
    'Bubble Sort': bubbleSort,
    'Insertion Sort': insertionSort,
    'Selection Sort': selectionSort,
    'Quick Sort': quickSort,
    'Merge Sort': mergeSort
}

# Tamanhos das listas para teste
tamanhos = [100, 500, 1000, 5000]

# Executando a comparação e plotagem dos tempos de execução
plotar_tempos(algoritmos, tamanhos)
