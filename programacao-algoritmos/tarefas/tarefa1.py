# a. Função para achar o resto de dois números inteiros positivos
def resto(a, b):
    if a < b:
        return a
    else:
        return resto(a - b, b)


# b. Função para achar a divisão inteira de dois números inteiros positivos
def divisao_inteira(a, b):
    if a < b:
        return 0
    else:
        return 1 + divisao_inteira(a - b, b)


# c. Função para achar o MDC de dois números inteiros positivos
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


# d. Função para fazer a busca sequencial de um número dentro de um vetor
def busca_sequencial(vetor, alvo, indice=0):
    if indice >= len(vetor):
        return -1
    if vetor[indice] == alvo:
        return indice
    return busca_sequencial(vetor, alvo, indice + 1)


# e. Função para fazer a busca binária de um número dentro de um vetor
def busca_binaria(vetor, alvo, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if vetor[meio] == alvo:
        return meio
    elif vetor[meio] > alvo:
        return busca_binaria(vetor, alvo, inicio, meio - 1)
    else:
        return busca_binaria(vetor, alvo, meio + 1, fim)
