def max_subsequence_sum(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]

    max_sum = dp[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        max_sum = max(max_sum, dp[i])

    return max_sum


# Leitura da entrada
n = int(input("Digite o tamanho da lista: "))
arr = list(map(int, input("Digite a sequência de números: ").split()))

# Certificando-se de que a entrada contém n elementos
if len(arr) != n:
    print(
        "Erro: o número de elementos na lista não corresponde ao valor informado para n."
    )
else:
    # Encontrando e imprimindo a soma máxima da subsequência contínua
    result = max_subsequence_sum(arr)
    print("Soma máxima =", result)
