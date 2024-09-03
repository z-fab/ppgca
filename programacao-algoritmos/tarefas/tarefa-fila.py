from queue import Queue
from random import randint
import time


class Cliente:
    def __init__(self, nome, tempo_atendimento, tempo_chegada):
        self.nome = nome
        self.tempo_atendimento = tempo_atendimento
        self.tempo_chegada = tempo_chegada

    def __str__(self):
        return self.nome


fila_cliente = Queue()
horario = 0
tempo_atendimento = 0


novo_cliente = Cliente(f"Cliente {1}", randint(1, 5), 0)
fila_cliente.put(novo_cliente)
print(
    f"{novo_cliente} | Chegou 14:{novo_cliente.tempo_chegada:02d} | Tempo de atendimento: {novo_cliente.tempo_atendimento} minutos"
)
time.sleep(1)

# Gerando clientes com tempo de atendimento aleatórios
n_clientes = randint(3, 8)
for i in range(1, n_clientes):
    horario += randint(1, 3)  # Horario que chegou
    novo_cliente = Cliente(f"Cliente {i+1}", randint(1, 5), horario)
    fila_cliente.put(novo_cliente)
    print(
        f"{novo_cliente} | Chegou 14:{novo_cliente.tempo_chegada:02d} | Tempo de atendimento: {novo_cliente.tempo_atendimento} minutos"
    )
    time.sleep(1)

print("------")
# Atendendo os clientes
while not fila_cliente.empty():
    cliente = fila_cliente.get()
    tempo_fila = tempo_atendimento - cliente.tempo_chegada
    if tempo_fila > 0:
        print(f"{cliente} | Atendido após {tempo_fila} minutos na fila")
    else:
        print(f"{cliente} | Atendido imediatamente")
    tempo_atendimento += cliente.tempo_atendimento
    time.sleep(1)

###########
# O algoritmo roda em O(n) onde n é o número de clientes
###########
