def ordena_por_tamanho(strings):
    return sorted(strings, key=len, reverse=True)


strings = ["Um", "dia", "estou", "programando", "estrutura", "de", "dados"]
strings_ordenadas = ordena_por_tamanho(strings)

print("Strings ordenadas por tamanho (maior para menor):")
for string in strings_ordenadas:
    print(string)
