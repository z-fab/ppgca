import time
from functools import wraps


def tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        tempo_execucao = (fim - inicio) * 1000  # Convertendo para milissegundos
        return resultado, tempo_execucao

    return wrapper


def check_balance(node):
    if node is None:
        return 0, True

    # Verificar balanceamento na subárvore esquerda
    left_height, left_balanced = check_balance(node.left)
    if not left_balanced:
        return 0, False

    # Verificar balanceamento na subárvore direita
    right_height, right_balanced = check_balance(node.right)
    if not right_balanced:
        return 0, False

    # Verificar a diferença de altura
    if abs(left_height - right_height) > 1:
        return 0, False

    # Retornar a altura atual e True indicando que está balanceada
    return 1 + max(left_height, right_height), True
