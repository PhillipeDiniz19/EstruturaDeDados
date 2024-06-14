def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Função de apoio para facilitar a chamada do quickSort
def quick_sort(arr):
    quickSort(arr, 0, len(arr) - 1)
    return arr

# Testando a implementação com diferentes listas de números
test_lists = [
    [38, 27, 43, 3, 9, 82, 10],
    [1, 2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1],
    [1],
    [],
    [12, 11, 13, 5, 6, 7],
    [3, 5, 2, 9, 10, 14, 7, 6]
]

for test_list in test_lists:
    print(f"Original: {test_list}")
    sorted_list = quick_sort(test_list.copy())
    print(f"Sorted:   {sorted_list}\n")
