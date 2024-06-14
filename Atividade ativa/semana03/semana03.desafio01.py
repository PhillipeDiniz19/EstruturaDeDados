def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Adiciona os elementos restantes de left (se houver)
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Adiciona os elementos restantes de right (se houver)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

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
    print(f"ORIGINAL: {test_list}")
    sorted_list = mergeSort(test_list)
    print(f"sORTEIO:   {sorted_list}\n")
