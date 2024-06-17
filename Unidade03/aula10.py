def complex_hash(key, table_size):
    hash_value = 0

    for char in str(key):
        hash_value = (hash_value * 31) + ord(char)
    index = hash_value % table_size
    
    return index

table_size = 10
keys = [45, 23, 7, 88, 33, 19, 72, 95, 54]

for key in keys:
    hashed_index = complex_hash(key, table_size)
    print(f"Chave {key} -> Índice {hashed_index}")
