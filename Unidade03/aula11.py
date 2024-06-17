def ordena_alunos_por_notas(ordem_chegada, notas):
    alunos = list(zip(ordem_chegada, notas))
    
    trocas = 0

    for i in range(1, len(alunos)):
        chave = alunos[i]
        j = i - 1
        while j >= 0 and (alunos[j][1] < chave[1] or (alunos[j][1] == chave[1] and alunos[j][0] > chave[0])):  
            alunos[j + 1] = alunos[j]
            j -= 1
            trocas += 1
        alunos[j + 1] = chave

    ordem_chegada_ordenada = [aluno[0] for aluno in alunos]
    notas_ordenadas = [aluno[1] for aluno in alunos]
    
    return ordem_chegada_ordenada, notas_ordenadas, trocas

ordem_chegada = ["Alice", "Bob", "Charlie", "David"]
notas = [85, 95, 70, 90]

ordem_chegada_ordenada, notas_ordenadas, total_trocas = ordena_alunos_por_notas(ordem_chegada, notas)

print("Ordem de chegada ordenada:", ordem_chegada_ordenada)
print("Notas ordenadas:", notas_ordenadas)
print("Total de trocas:", total_trocas)
